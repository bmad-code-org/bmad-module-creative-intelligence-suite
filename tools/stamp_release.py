#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Release version stamper for the Creative Intelligence Suite.

Writes a human-supplied SemVer version into the module record: the `version`
line inside the `[bmod]` table of each skills/*/bmod.toml that has one. Member
skills carry no version and are not written. Used by tools/release.md to stamp
releases and the next placeholder on `dev`.

Before writing anything it checks every bmod.toml: each skill folder has one,
a module record carries a known code, a string version and the one known
update source, the record's `skills` list and the folders that name the record
agree, the record folder ships `SKILL.md` and `help/help.md`, every
`help/<topic>.md` that `help.md` names exists and every topic file is named
there, `roster.toml` parses when present, and `required_skills` and
`recommended_skills` are well formed. `npm test` runs the same checks with
`--check`. CI also runs BMAD-METHOD's own tools/validate_manifests.py against
this repository, which is the runtime's view of the same files.

A file may carry keys and tables this script does not know. The runtime ignores
them, so a release must not refuse them; they are left exactly as written. The
version line is rewritten textually and nothing else is touched.

Nothing is written unless every file passes first. After writing, the script
re-reads every record and fails naming the offending path if anything is off.

Usage:
  uv run --python 3.11 tools/stamp_release.py 0.4.0
  uv run --python 3.11 tools/stamp_release.py --check
"""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from pathlib import Path

sys.dont_write_bytecode = True

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MANIFEST_NAME = "bmod.toml"
RECORD_PREFIX = "bmod-"
HELP_NAME = "help/help.md"
ROSTER_NAME = "roster.toml"

MODULES = frozenset({"cis"})
UPDATE_SOURCE = "github:bmad-code-org/bmad-module-creative-intelligence-suite/skills"
REQUIREMENT_KEYS = ("required_skills", "recommended_skills")

TABLE_HEADER = re.compile(r"[ \t]*\[")
BMOD_HEADER = re.compile(r"[ \t]*\[[ \t]*bmod[ \t]*\][ \t]*(?:#.*)?$")
VERSION_LINE = re.compile(r'(?P<head>[ \t]*version[ \t]*=[ \t]*)"[^"\n]*"(?P<tail>[ \t]*(?:#.*)?)$')
TOPIC_REFERENCE = re.compile(r"`help/([^`/<>]+\.md)`")

# Mirrors the SEMVER regex in setup.py, the `bmad` hub skill's installer. That
# script also refuses to order any version containing "-dev", so such a version
# can never compare as current or outdated for installed copies — reject it
# here. It likewise drops build metadata when ordering, so "1.2.0+x" compares
# equal to "1.2.0"; a release stamped that way is invisible, so reject that too.
SEMVER = re.compile(
    r"(?P<major>0|[1-9][0-9]*)\."
    r"(?P<minor>0|[1-9][0-9]*)\."
    r"(?P<patch>0|[1-9][0-9]*)"
    r"(?:-(?P<prerelease>"
    r"(?:0|[1-9][0-9]*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9][0-9]*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*))*"
    r"))?"
    r"(?:\+(?P<build>[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?\Z"
)


class StampError(Exception):
    pass


def validate_version(version: str) -> None:
    match = SEMVER.fullmatch(version)
    if match is None:
        raise StampError(
            f"invalid version {version!r}: must be SemVer "
            "(MAJOR.MINOR.PATCH, optional prerelease), e.g. 0.4.0"
        )
    if "-dev" in version.casefold():
        raise StampError(
            f"invalid version {version!r}: setup.py cannot order \"-dev\" "
            "versions, so installed copies would never compare as current — "
            "pick a different prerelease label"
        )
    if match.group("build") is not None:
        base = version.split("+", 1)[0]
        raise StampError(
            f"invalid version {version!r}: setup.py ignores build metadata when "
            f"ordering, so this compares equal to {base!r} and installed copies "
            "would never see the release — change the major, minor, patch, or "
            "prerelease part"
        )


def read_toml(path: Path, rel: str) -> dict[str, object]:
    try:
        return tomllib.loads(path.read_bytes().decode("utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise StampError(f"{rel}: cannot read: {error}") from error


def table(data: dict[str, object], name: str, rel: str) -> dict[str, object] | None:
    value = data.get(name)
    if value is not None and not isinstance(value, dict):
        raise StampError(f"{rel}: [{name}] must be a table")
    return value


def validate_requirements(owner: dict[str, object], where: str, rel: str, shipped: set[str]) -> None:
    """An entry is a skill name, or `{ skill, version?, source? }`; a skill from another repo must say where it comes from."""
    for key in REQUIREMENT_KEYS:
        entries = owner.get(key, [])
        if not isinstance(entries, list):
            raise StampError(f"{rel}: {where}.{key} must be a list")
        for entry in entries:
            plain = isinstance(entry, str)
            if plain:
                entry = {"skill": entry}
            if not isinstance(entry, dict) or not isinstance(entry.get("skill"), str) or not entry["skill"]:
                raise StampError(f"{rel}: {where}.{key} entry {entry!r} must be a skill name or a table with `skill`")
            if not set(entry) <= {"skill", "version", "source"}:
                raise StampError(f"{rel}: {where}.{key} entry for {entry['skill']} allows only skill, version and source")
            minimum = entry.get("version")
            if minimum is not None and (
                not isinstance(minimum, str) or SEMVER.fullmatch(minimum) is None or "+" in minimum
            ):
                raise StampError(f"{rel}: {where}.{key} {entry['skill']}: version must be plain SemVer; found {minimum!r}")
            source = entry.get("source")
            if source is not None and (not isinstance(source, str) or not source):
                raise StampError(f"{rel}: {where}.{key} {entry['skill']}: source must be a string")
            if source is None and (not plain or entry["skill"] not in shipped):
                raise StampError(
                    f"{rel}: {where}.{key} {entry['skill']} needs a source: only a plain name of a skill in this repository goes without one"
                )


def validate_record_folder(folder: Path, rel: str) -> None:
    for name in ("SKILL.md", HELP_NAME):
        path = folder / name
        if path.is_symlink() or not path.is_file():
            raise StampError(f"{rel}: the record folder must ship {name} as a plain file")
    help_dir = (folder / HELP_NAME).parent
    topics = {path.name for path in help_dir.glob("*.md")} - {Path(HELP_NAME).name}
    for name in sorted(topics):
        if (help_dir / name).is_symlink():
            raise StampError(f"{rel}: help/{name} must not be a symlink")
    try:
        named = set(TOPIC_REFERENCE.findall((folder / HELP_NAME).read_text(encoding="utf-8")))
        for name in sorted(topics):
            for other in TOPIC_REFERENCE.findall((help_dir / name).read_text(encoding="utf-8")):
                if other not in topics and other != Path(HELP_NAME).name:
                    raise StampError(f"{rel}: help/{name} names help/{other}, which does not exist")
    except (OSError, UnicodeError) as error:
        raise StampError(f"{rel}: cannot read a help file: {error}") from error
    named.discard(Path(HELP_NAME).name)
    for name in sorted(named - topics):
        raise StampError(f"{rel}: {HELP_NAME} names help/{name}, which does not exist")
    for name in sorted(topics - named):
        raise StampError(f"{rel}: help/{name} is not named in {HELP_NAME}, so help would never find it")
    roster = folder / ROSTER_NAME
    if roster.is_symlink():
        raise StampError(f"{rel}: {ROSTER_NAME} must not be a symlink")
    if roster.is_file():
        read_toml(roster, f"{rel[: -len(MANIFEST_NAME)]}{ROSTER_NAME}")


def collect_records(project_root: Path) -> list[Path]:
    """Check every bmod.toml and return the module records, the only files that carry a version."""
    folders = sorted(path for path in (project_root / "skills").glob("*") if path.is_dir())
    if not folders:
        raise StampError(f"no skills/*/{MANIFEST_NAME} found under {project_root}: run from a checkout of this repository")
    shipped = {folder.name for folder in folders}
    parsed: dict[str, dict[str, object]] = {}
    for folder in folders:
        manifest = folder / MANIFEST_NAME
        if not manifest.is_file():
            raise StampError(f"skills/{folder.name}: missing {MANIFEST_NAME}")
        parsed[folder.name] = read_toml(manifest, f"skills/{folder.name}/{MANIFEST_NAME}")

    records: list[Path] = []
    listed: dict[str, set[str]] = {}
    for name, data in parsed.items():
        rel = f"skills/{name}/{MANIFEST_NAME}"
        bmod, skill = table(data, "bmod", rel), table(data, "skill", rel)
        if bmod is None and skill is None:
            raise StampError(f"{rel}: needs a [bmod] table, a [skill] table, or both")
        if name.startswith(RECORD_PREFIX) and bmod is None:
            raise StampError(f"{rel}: a {RECORD_PREFIX}* folder must hold a [bmod] table")
        if bmod is not None:
            if bmod.get("code") not in MODULES:
                raise StampError(f"{rel}: unknown module code {bmod.get('code')!r} (expected one of {', '.join(sorted(MODULES))})")
            if not isinstance(bmod.get("version"), str) or SEMVER.fullmatch(bmod["version"]) is None:
                raise StampError(f"{rel}: bmod.version must be a SemVer string; found {bmod.get('version')!r}")
            if bmod.get("update_source") != UPDATE_SOURCE:
                raise StampError(f"{rel}: bmod.update_source must be exactly {UPDATE_SOURCE!r}; found {bmod.get('update_source')!r}")
            members = bmod.get("skills", [])
            if not isinstance(members, list) or not all(isinstance(member, str) for member in members):
                raise StampError(f"{rel}: bmod.skills must be a list of skill names")
            if len(set(members)) != len(members):
                raise StampError(f"{rel}: bmod.skills lists a skill twice")
            listed[name] = set(members)
            validate_requirements(bmod, "bmod", rel, shipped)
            validate_record_folder(project_root / "skills" / name, rel)
            records.append(project_root / "skills" / name / MANIFEST_NAME)
        if skill is not None:
            validate_requirements(skill, "skill", rel, shipped)

    for name, data in parsed.items():
        rel = f"skills/{name}/{MANIFEST_NAME}"
        skill = data.get("skill")
        if skill is None or "bmod" in data:
            continue
        if skill.get("source") != UPDATE_SOURCE:
            raise StampError(f"{rel}: skill.source must be exactly {UPDATE_SOURCE!r}; found {skill.get('source')!r}")
        record = skill.get("bmod")
        if record not in listed:
            raise StampError(f"{rel}: skill.bmod names {record!r}, which is not a module record in this repository")
        if name not in listed[record]:
            raise StampError(f"{rel}: names {record}, but that record's skills list leaves it out")
    for record, members in listed.items():
        for member in sorted(members):
            skill = parsed.get(member, {}).get("skill")
            if not isinstance(skill, dict) or skill.get("bmod") != record:
                raise StampError(f"skills/{record}/{MANIFEST_NAME}: lists {member}, which does not name this record back")
    return records


def stamp_text(original: str, rel: str, version: str) -> str:
    """Rewrite the one `version` line inside `[bmod]`; another table may have a `version` of its own."""
    lines = original.splitlines(keepends=True)
    inside = False
    matches: list[int] = []
    for index, line in enumerate(lines):
        bare = line.rstrip("\r\n")
        if TABLE_HEADER.match(bare):
            inside = BMOD_HEADER.match(bare) is not None
        elif inside and VERSION_LINE.match(bare):
            matches.append(index)
    if len(matches) != 1:
        raise StampError(f"{rel}: expected exactly one 'version = \"...\"' line inside [bmod], found {len(matches)}")
    line = lines[matches[0]]
    ending = line[len(line.rstrip("\r\n")) :]
    match = VERSION_LINE.match(line.rstrip("\r\n"))
    lines[matches[0]] = f'{match.group("head")}"{version}"{match.group("tail")}{ending}'
    return "".join(lines)


def run(project_root: Path, version: str | None) -> int:
    try:
        if version is None:
            records = collect_records(project_root)
            for record in records:
                rel = record.relative_to(project_root).as_posix()
                stamp_text(record.read_bytes().decode("utf-8"), rel, "0.0.0")
            print(f"bmod files valid: {len(records)} module record(s).")
            return 0
        validate_version(version)
        records = collect_records(project_root)

        # Nothing is written if any file fails.
        planned: list[tuple[Path, str]] = []
        expected: dict[str, dict[str, object]] = {}
        for record in records:
            rel = record.relative_to(project_root).as_posix()
            data = read_toml(record, rel)
            content = stamp_text(record.read_bytes().decode("utf-8"), rel, version)
            expected[rel] = {**data, "bmod": {**data["bmod"], "version": version}}
            if tomllib.loads(content) != expected[rel]:
                raise StampError(f"{rel}: stamping would change something other than the version")
            planned.append((record, content))

        for path, content in planned:
            try:
                path.write_bytes(content.encode("utf-8"))
            except OSError as error:
                raise StampError(f"{path.relative_to(project_root).as_posix()}: cannot write: {error}") from error
        for record in records:
            rel = record.relative_to(project_root).as_posix()
            if read_toml(record, rel) != expected[rel]:
                raise StampError(f"{rel}: stamping changed something other than the version")
        collect_records(project_root)
    except StampError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Stamped version {version} into {len(planned)} files:")
    for path, _ in planned:
        print(f"  {path.relative_to(project_root).as_posix()}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Stamp a release version into the module record.")
    parser.add_argument("version", nargs="?", help='SemVer release version, e.g. "0.4.0"')
    parser.add_argument("--check", action="store_true", help="check every bmod.toml and write nothing")
    parser.add_argument("--project-root", type=Path, default=PROJECT_ROOT, help="repository to stamp (default: this one)")
    args = parser.parse_args(argv)
    if args.check == (args.version is not None):
        parser.error("give a version to stamp, or --check, but not both")
    return run(args.project_root.resolve(), args.version)


if __name__ == "__main__":
    sys.exit(main())
