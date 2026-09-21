# Release Runbook — Creative Intelligence Suite

`dev` receives development PRs; `main` is the default, release-only branch.
`npx skills` installs from `main`, and installed copies check `main` for
updates, so what `main` serves is the released version. Release by
fast-forwarding `main` to a stamped commit on `dev`, then tag it. No release
branches, release PRs, merge commits, or back-merges are needed. `main` stays
an ancestor of `dev`.

This is a hand-run process. Use Git, `uv`, and Node. Pause other pushes and
merges into `dev` until the next placeholder is pushed. Do the release in one
sitting. Stop on any failed command or unexpected diff.

## 1. Prepare

Start in a clean checkout with no unpublished commits:

```bash
git status --porcelain
git fetch origin
git switch dev
git pull --ff-only origin dev
test "$(git rev-parse HEAD)" = "$(git rev-parse origin/dev)"
git merge-base --is-ancestor origin/main dev

cis_release_version=0.4.0
cis_next_version=0.4.1-next
git show origin/main:skills/bmod-cis/bmod.toml
git tag --list "v$cis_release_version"
```

Choose the versions explicitly. The release must differ from what `main`
serves and must not reuse a tag. Use SemVer, optionally with a prerelease; no
`-dev` or build metadata (`+...`). The next placeholder is the next patch with
`-next`. The stamper enforces the version syntax, not release history.

## 2. Stamp and push dev

```bash
uv run --python 3.11 tools/stamp_release.py "$cis_release_version"
git diff
git add skills/bmod-cis/bmod.toml
git commit -m "chore(release): v$cis_release_version"
cis_release_commit=$(git rev-parse HEAD)
npm ci && npm test
git push origin dev
```

Review before committing: only the `version` line in `skills/bmod-cis/bmod.toml`
should change. Member skills carry no version. The stamper checks every
`bmod.toml` before writing: the record's code, version and update source, that
the record's `skills` list and the folders naming it agree, the record's
`SKILL.md`, `help/help.md`, topic files and `roster.toml`, and well-formed
`required_skills` and `recommended_skills`. If it exits nonzero after writing,
restore the record with `git restore skills/bmod-cis/bmod.toml`, fix the
reported problem, and rerun.

Run `npm test` on committed `HEAD` in this checkout before pushing; keep that
tested commit checked out through promotion and tagging. Wait for its GitHub
status checks to pass before promoting it.

## 3. Fast-forward main and tag

```bash
git fetch origin
test "$(git rev-parse HEAD)" = "$cis_release_commit"
test "$(git rev-parse origin/dev)" = "$cis_release_commit"
git merge-base --is-ancestor origin/main dev
git push origin dev:main
git fetch origin
test "$(git rev-parse origin/main)" = "$cis_release_commit"
git tag -a "v$cis_release_version" "$cis_release_commit" -m "Release v$cis_release_version"
git push origin "refs/tags/v$cis_release_version"
```

The tag identifies the same stamped commit on `dev` and `main`. Never force a
push or move a release tag. If `dev` moved, stop rather than including
unreviewed changes in the release.

## 4. Stamp the next placeholder

```bash
git fetch origin
test "$(git rev-parse origin/dev)" = "$cis_release_commit"
uv run --python 3.11 tools/stamp_release.py "$cis_next_version"
git diff
git add skills/bmod-cis/bmod.toml
git commit -m "chore: bump placeholder version to $cis_next_version"
npm ci && npm test
git push origin dev
```

Review the same version-only changes before committing. `main` and the tag
retain the release version; `dev` carries the next placeholder. Development can
resume. Nothing needs merging back.

## 5. Verify

```bash
npx skills add bmad-code-org/bmad-module-creative-intelligence-suite --list
```

Install `bmod-cis` and one skill into a scratch project and run `bmad status`
there; it should report the `cis` module at the released version.

Installed copies check `main` through `raw.githubusercontent.com`, which caches
files for around five minutes. Verify the release through Git first, or wait
before trusting an update check that still reports the previous version.
