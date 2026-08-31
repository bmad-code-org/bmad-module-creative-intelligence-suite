# CHANGELOG

## v0.3.2 - Aug 30, 2026 — team overrides reach home-installed skills

### Fixes

- **All fifteen resolver call sites pass `--project-root`** (#44). `resolve_customization.py` worked out the project root by itself when the flag was absent, walking up from the skill's installed directory. For a skill installed under your home directory that walk reaches `~`, and a user-level BMad install leaves a `~/_bmad` sitting there — so the resolver decided home was the project, found no override, and returned shipped defaults. A `_bmad/custom/bmad-cis-*.toml` in the actual project was never opened, and nothing reported it.

  Whether an override took effect therefore depended on where its skill happened to be installed, which the override's author cannot see from the override. Two people with identical checkouts could get different behavior depending on whether either had ever run a user-level install.

  The resolver itself is fixed upstream in [BMAD-METHOD#2802](https://github.com/bmad-code-org/BMAD-METHOD/pull/2802), and that is what repairs an existing install — CIS ships no copy of the script and calls core's, so the fix arrives with your next core upgrade. Passing the root explicitly is the other half: nothing is left to infer, and it matches `resolve_config.py`, which has always required the flag. Six agents, four workflows, and the `workflow.on_complete` terminal hooks are covered.

### Maintenance

- **Marketplace plugin version synced to 0.3.2** — nothing in the release workflow touches `.claude-plugin/marketplace.json`, so its version drifts from `package.json` unless bumped by hand.

## v0.3.1 - Aug 16, 2026 — `persistent_facts` ships empty

### Fixes

- **Skills no longer load `project-context.md` by default** (#40). All ten `customize.toml` files shipped with `persistent_facts = ["file:{project-root}/**/project-context.md"]` pre-seeded, which made loading that file an opt-out default baked into every skill rather than a customization you choose. `persistent_facts` is a user-customization surface, so it now ships as an empty array in all ten.

  This also corrects an assumption that no longer held: `bmad-project-context` does not produce a `project-context.md` at all. It writes a verified block into the repository's `AGENTS.md` and treats a `project-context.md` as a legacy artifact from the retired skills. The seeded default named a file that the current tooling never creates.

  Repository-wide context belongs in `AGENTS.md`, which every skill already sees. `persistent_facts` is for context that only one skill needs, loaded when that skill runs instead of carried as constant memory. If you keep a `project-context.md` and want a skill to read it, add the entry to your team or user override TOML:

  ```toml
  persistent_facts = ["file:{project-root}/**/project-context.md"]
  ```

## v0.3.0 - Aug 9, 2026 — skills run their Python through `uv run`

### Fixes

- **The customization resolver is invoked with `uv run`** (#37). All fifteen call sites — six agents plus the four workflows and their `on_complete` hooks — shelled out to a bare `python3` to run `_bmad/scripts/resolve_customization.py`. That script declares `requires-python = ">=3.11"` and hard-exits below it, because `tomllib` is a 3.11 stdlib addition. On macOS without Homebrew or Ubuntu 22.04, where `python3` is 3.10, activation fell through to the skill's "if the script fails" path and hand-merged the TOML layers in-context — no error surfaced, so a run could resolve customization subtly wrong and look fine. `uv run` reads the script's own `requires-python` and provisions a matching interpreter, so whatever `python3` resolves to on your PATH no longer matters.
- **README Python badge corrected to `>=3.11`** (#37). It advertised `>=3.10`, a floor that cannot run the shared resolver.

### Requirements

- **`uv` is what you need; a system Python is not.** CIS skills no longer invoke a bare interpreter anywhere. Install [`uv`](https://docs.astral.sh/uv/) and it provisions the right Python per script.

## v0.2.1 - May 17, 2026 — module-help.csv column alignment

- Normalized `src/module-help.csv` to the documented 13-column schema (#32).
- Renamed `after`/`before` columns in `src/module-help.csv` to `preceded-by`/`followed-by` to match the canonical 13-column schema introduced in BMAD-METHOD v6.6.0. Warning-only fix; data was already loaded positionally (#35).

## v0.2.0 - Apr 21, 2026 — customize.toml pattern across agents and workflows

### Agent customization surface

- All six agents (`bmad-cis-agent-brainstorming-coach`, `bmad-cis-agent-creative-problem-solver`, `bmad-cis-agent-design-thinking-coach`, `bmad-cis-agent-innovation-strategist`, `bmad-cis-agent-presentation-master`, `bmad-cis-agent-storyteller`) adopt the BMAD-METHOD `customize.toml` pattern. Each agent's `SKILL.md` now runs a six-step On Activation block that resolves customization via `resolve_customization.py`, executes prepend/append hook steps, loads `persistent_facts`, reads config from `{project-root}/_bmad/cis/config.yaml`, and greets the user before the menu appears.
- Added `[agent]` namespace in each agent's `customize.toml` exposing `role`, `identity`, `communication_style`, `principles`, `persistent_facts`, `activation_steps_prepend/append`, and the `[[agent.menu]]` entries. Overrides merge per BMad structural rules (scalars override, keyed arrays-of-tables replace-or-append, other arrays append).
- Added an agent roster with essence descriptors in `src/module.yaml` so external skills (party-mode, retrospective, advanced-elicitation, help catalog) can route to, display, and embody CIS agents without reading each agent file.

### Workflow customization surface

- All four workflow skills (`bmad-cis-design-thinking`, `bmad-cis-innovation-strategy`, `bmad-cis-problem-solving`, `bmad-cis-storytelling`) converted from redirect-only `SKILL.md` + `workflow.md` split to a single integrated `SKILL.md`. The standalone `workflow.md` file is removed from every workflow skill.
- Each workflow gains the same six-step On Activation block as agents (resolve customization → prepend → `persistent_facts` → config load → greet → append), plus a `Conventions` block declaring `{skill-root}`, `{project-root}`, and `{skill-name}`.
- Each workflow's terminal step now invokes `resolve_customization.py --key workflow.on_complete` as an `<action>` inside the final `<step>`. `bmad-cis-problem-solving` wires the hook at both the last mandatory step 8 and the optional step 9 so the hook fires whether or not the user runs the reflection step.
- Added `customize.toml` at every workflow skill root with a `[workflow]` namespace exposing `activation_steps_prepend`, `activation_steps_append`, `persistent_facts`, and `on_complete`. Team and per-user overrides merge from `{project-root}/_bmad/custom/{skill-name}.toml` and `{skill-name}.user.toml`.

### Fixes bundled with the rollout

- Disambiguated "before Step N" references in workflow Inputs sections to "before workflow Step N" now that the activation block also numbers its steps 1-6.
- Clarified `persistent_facts` behavior — if a `file:` glob matches no files or a path does not exist, silently skip that entry rather than fabricate content.
- `bmad-cis-storytelling`: fixed literal `communication_language` to templated `{communication_language}` so runtime language switching applies as intended.

## v0.1.9 - Mar 18, 2026

- Patch conversion rename of folder and conversion to skill format

## v0.1.8 - Feb 23, 2026

- Fix: use consistent YAML quoting in workflow descriptions

## v0.1.7 - Feb 22, 2026

- Add AGENTS.md with comprehensive development documentation, architecture overview, and schema validation guidance
- Convert test files from CommonJS to ES modules for better consistency
- Fix assert() calls to use assert.ok() for proper boolean validation
- Optimize workflow descriptions for skill selection with "Use when..." trigger patterns
- Remove redundant web_bundle sections from workflow configurations

## v0.1.6 - Feb 22, 2026

- Improve module-help.csv descriptions with "Use when..." clauses following '[Action]. Use [trigger].' pattern for better LLM comprehension

## v0.1.5 - Feb 8, 2026

- Add Astro + Starlight documentation site with comprehensive CIS documentation
- Add AI banner component to match BMAD-METHOD layout
- Remove \_module-installer pattern for declarative directory creation
- Fix landing page layout to match BMAD-METHOD
- Fix docs workflow to use npm install instead of npm ci

## v0.1.4 - Feb 1, 2026

- Initial release
