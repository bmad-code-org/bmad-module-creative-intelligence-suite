#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Release version stamper for the cis-skills mirror.

Writes a human-supplied SemVer version into every skills/*/module-manifest.toml,
then verifies the result. Used by tools/release.md to cut a stamped release
commit; never run on the unstamped `dev` branch itself. The manifests are the
only version source the distributed tree carries.

Before writing anything it validates every manifest: the keys module, version,
update_source and knowledge are present, module is a known module,
update_source carries its one known value, knowledge and roster list files the
skill ships, and requires and recommends are well formed.

A manifest may carry keys this script does not know. The runtime ignores them,
so a release must not refuse them; they are left exactly as written. The
top-level `version = "..."` line is rewritten textually and nothing else is
touched.

Nothing is written unless every file passes validation first. After writing,
the script re-reads every file and fails naming the offending path if
anything is off.

Usage:
  uv run --python 3.11 tools/stamp_release.py 0.3.1
"""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from pathlib import Path, PurePosixPath

sys.dont_write_bytecode = True

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MANIFEST_NAME = "module-manifest.toml"

MODULES = frozenset({"cis"})
UPDATE_SOURCE = "github:bmad-code-org/cis-skills/skills"
MANIFEST_KEYS = frozenset({"module", "version", "update_source", "knowledge"})
DEPENDENCY_TABLES = ("recommends", "requires")

VERSION_LINE = re.compile(r'^version\s*=\s*".*"\s*$')

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
            "(MAJOR.MINOR.PATCH, optional prerelease), e.g. 0.3.1"
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


def read_manifest_module(path: Path, rel: str) -> str:
    """Validate a skill manifest's exact schema and return its module."""
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise StampError(f"{rel}: cannot read manifest: {error}") from error
    missing = MANIFEST_KEYS - set(data)
    if missing:
        raise StampError(f"{rel}: manifest is missing {', '.join(sorted(missing))}")
    module = data["module"]
    if module not in MODULES:
        raise StampError(
            f"{rel}: unknown module {module!r} "
            f"(expected one of {', '.join(sorted(MODULES))})"
        )
    if not isinstance(data["version"], str):
        raise StampError(f"{rel}: version must be a string")
    if data["update_source"] != UPDATE_SOURCE:
        raise StampError(
            f"{rel}: update_source must be exactly {UPDATE_SOURCE!r}; "
            f"found {data['update_source']!r}"
        )
    validate_knowledge(data["knowledge"], path.parent, rel)
    if "roster" in data:
        validate_knowledge(data["roster"], path.parent, rel, key="roster")
    return module


def validate_knowledge(value: object, skill_dir: Path, rel: str, key: str = "knowledge") -> None:
    """Each entry is a path to a plain file inside the skill, so help never points at something an install lacks."""
    if not isinstance(value, list) or not value:
        raise StampError(f"{rel}: {key} must be a non-empty list of paths inside the skill")
    seen: set[PurePosixPath] = set()
    for entry in value:
        if not isinstance(entry, str) or not entry or "\\" in entry:
            raise StampError(f"{rel}: {key} entry {entry!r} must be a relative POSIX path")
        relative = PurePosixPath(entry)
        if relative.is_absolute() or any(part in ("", ".", "..") for part in relative.parts):
            raise StampError(f"{rel}: {key} entry {entry!r} must stay inside the skill")
        if relative in seen:
            raise StampError(f"{rel}: {key} lists {entry!r} twice")
        seen.add(relative)
        current = skill_dir
        for part in relative.parts:
            current = current / part
            if current.is_symlink():
                raise StampError(f"{rel}: {key} document {entry!r} must not be a symlink")
        if not current.is_file():
            raise StampError(f"{rel}: {key} document {entry!r} is not shipped by the skill")


def validate_requires(value: object, rel: str, skills: set[str], table: str = "requires") -> None:
    """Each entry is `skill = { version, source? }`; a skill from another repo must say where it comes from."""
    if value is None:
        return
    if not isinstance(value, dict):
        raise StampError(f"{rel}: {table} must be a table of skill names")
    for skill, entry in value.items():
        if not isinstance(entry, dict) or not {"version"} <= set(entry) <= {"version", "source"}:
            raise StampError(f"{rel}: {table}.{skill} must be a table with version and optionally source")
        minimum = entry["version"]
        if not isinstance(minimum, str) or SEMVER.fullmatch(minimum) is None or "+" in minimum:
            raise StampError(f"{rel}: {table}.{skill}.version must be a plain SemVer version; found {minimum!r}")
        source = entry.get("source")
        if source is not None and not isinstance(source, str):
            raise StampError(f"{rel}: {table}.{skill}.source must be a string")
        if source is None and skill not in skills:
            raise StampError(f"{rel}: {table}.{skill} names no skill in this repository and gives no source")


def collect_skills(project_root: Path) -> tuple[list[Path], dict[str, str]]:
    """Return every skill's manifest path plus a skill-name -> module map."""
    skill_dirs = sorted(
        path for path in (project_root / "skills").glob("*") if path.is_dir()
    )
    if not skill_dirs:
        raise StampError(
            f"no skills/*/{MANIFEST_NAME} found under {project_root} — "
            "run from a cis-skills checkout"
        )
    manifests: list[Path] = []
    modules: dict[str, str] = {}
    for skill_dir in skill_dirs:
        manifest = skill_dir / MANIFEST_NAME
        rel = manifest.relative_to(project_root).as_posix()
        if not manifest.is_file():
            raise StampError(
                f"{skill_dir.relative_to(project_root).as_posix()}: missing {MANIFEST_NAME}"
            )
        modules[skill_dir.name] = read_manifest_module(manifest, rel)
        manifests.append(manifest)
    for manifest in manifests:
        rel = manifest.relative_to(project_root).as_posix()
        data = tomllib.loads(manifest.read_text(encoding="utf-8"))
        for table in DEPENDENCY_TABLES:
            validate_requires(data.get(table), rel, set(modules), table)
    return manifests, modules


def stamped_manifest_content(path: Path, rel: str, version: str) -> str:
    try:
        original = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise StampError(f"{rel}: cannot read manifest: {error}") from error
    lines = original.splitlines(keepends=True)
    # Only the top level: a table further down may have a `version` of its own.
    first_table = next((index for index, line in enumerate(lines) if line.lstrip().startswith("[")), len(lines))
    matches = [index for index in range(first_table) if VERSION_LINE.match(lines[index].rstrip("\n"))]
    if len(matches) != 1:
        raise StampError(
            f"{rel}: expected exactly one top-level 'version = \"...\"' line, found {len(matches)}"
        )
    lines[matches[0]] = f'version = "{version}"\n'
    return "".join(lines)


def verify_stamp(
    root: Path,
    manifests: list[Path],
    modules: dict[str, str],
    version: str,
    before: dict[str, dict[str, object]],
) -> None:
    # Each manifest is what it was with only the version changed.
    for manifest in manifests:
        rel = manifest.relative_to(root).as_posix()
        try:
            raw = manifest.read_bytes()
            data = tomllib.loads(raw.decode("utf-8"))
        except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
            raise StampError(f"{rel}: cannot read manifest after stamping: {error}") from error
        if data != {**before[rel], "version": version}:
            raise StampError(f"{rel}: stamping changed something other than the version")


def run(project_root: Path, version: str) -> int:
    try:
        validate_version(version)
        manifests, modules = collect_skills(project_root)

        # Phase 1: compute every new file content; nothing is written if any file fails.
        planned: list[tuple[Path, str]] = []
        before: dict[str, dict[str, object]] = {}
        for manifest in manifests:
            rel = manifest.relative_to(project_root).as_posix()
            data = tomllib.loads(manifest.read_text(encoding="utf-8"))
            before[rel] = data
            planned.append((manifest, stamped_manifest_content(manifest, rel, version)))

        # Phase 2: write, then verify from disk.
        for path, content in planned:
            try:
                path.write_text(content, encoding="utf-8")
            except OSError as error:
                raise StampError(
                    f"{path.relative_to(project_root).as_posix()}: cannot write: {error}"
                ) from error
        verify_stamp(project_root, manifests, modules, version, before)
    except StampError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Stamped version {version} into {len(planned)} files:")
    for path, _ in planned:
        print(f"  {path.relative_to(project_root).as_posix()}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Stamp a release version into every skill manifest."
    )
    parser.add_argument("version", help='SemVer release version, e.g. "0.3.1"')
    args = parser.parse_args(argv)
    return run(PROJECT_ROOT, args.version)


if __name__ == "__main__":
    sys.exit(main())
