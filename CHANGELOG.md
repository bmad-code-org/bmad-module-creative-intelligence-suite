# CHANGELOG

## v0.2.0 - Apr 21, 2026 — customize.toml pattern across agents and workflows

### Agent customization surface

* All six agents (`bmad-cis-agent-brainstorming-coach`, `bmad-cis-agent-creative-problem-solver`, `bmad-cis-agent-design-thinking-coach`, `bmad-cis-agent-innovation-strategist`, `bmad-cis-agent-presentation-master`, `bmad-cis-agent-storyteller`) adopt the BMAD-METHOD `customize.toml` pattern. Each agent's `SKILL.md` now runs a six-step On Activation block that resolves customization via `resolve_customization.py`, executes prepend/append hook steps, loads `persistent_facts`, reads config from `{project-root}/_bmad/cis/config.yaml`, and greets the user before the menu appears.
* Added `[agent]` namespace in each agent's `customize.toml` exposing `role`, `identity`, `communication_style`, `principles`, `persistent_facts`, `activation_steps_prepend/append`, and the `[[agent.menu]]` entries. Overrides merge per BMad structural rules (scalars override, keyed arrays-of-tables replace-or-append, other arrays append).
* Added an agent roster with essence descriptors in `src/module.yaml` so external skills (party-mode, retrospective, advanced-elicitation, help catalog) can route to, display, and embody CIS agents without reading each agent file.

### Workflow customization surface

* All four workflow skills (`bmad-cis-design-thinking`, `bmad-cis-innovation-strategy`, `bmad-cis-problem-solving`, `bmad-cis-storytelling`) converted from redirect-only `SKILL.md` + `workflow.md` split to a single integrated `SKILL.md`. The standalone `workflow.md` file is removed from every workflow skill.
* Each workflow gains the same six-step On Activation block as agents (resolve customization → prepend → `persistent_facts` → config load → greet → append), plus a `Conventions` block declaring `{skill-root}`, `{project-root}`, and `{skill-name}`.
* Each workflow's terminal step now invokes `resolve_customization.py --key workflow.on_complete` as an `<action>` inside the final `<step>`. `bmad-cis-problem-solving` wires the hook at both the last mandatory step 8 and the optional step 9 so the hook fires whether or not the user runs the reflection step.
* Added `customize.toml` at every workflow skill root with a `[workflow]` namespace exposing `activation_steps_prepend`, `activation_steps_append`, `persistent_facts`, and `on_complete`. Team and per-user overrides merge from `{project-root}/_bmad/custom/{skill-name}.toml` and `{skill-name}.user.toml`.

### Fixes bundled with the rollout

* Disambiguated "before Step N" references in workflow Inputs sections to "before workflow Step N" now that the activation block also numbers its steps 1-6.
* Clarified `persistent_facts` behavior — if a `file:` glob matches no files or a path does not exist, silently skip that entry rather than fabricate content.
* `bmad-cis-storytelling`: fixed literal `communication_language` to templated `{communication_language}` so runtime language switching applies as intended.

## v0.1.9 - Mar 18, 2026

* Patch conversion rename of folder and conversion to skill format

## v0.1.8 - Feb 23, 2026

* Fix: use consistent YAML quoting in workflow descriptions

## v0.1.7 - Feb 22, 2026

* Add AGENTS.md with comprehensive development documentation, architecture overview, and schema validation guidance
* Convert test files from CommonJS to ES modules for better consistency
* Fix assert() calls to use assert.ok() for proper boolean validation
* Optimize workflow descriptions for skill selection with "Use when..." trigger patterns
* Remove redundant web_bundle sections from workflow configurations

## v0.1.6 - Feb 22, 2026

* Improve module-help.csv descriptions with "Use when..." clauses following '[Action]. Use [trigger].' pattern for better LLM comprehension

## v0.1.5 - Feb 8, 2026

* Add Astro + Starlight documentation site with comprehensive CIS documentation
* Add AI banner component to match BMAD-METHOD layout
* Remove _module-installer pattern for declarative directory creation
* Fix landing page layout to match BMAD-METHOD
* Fix docs workflow to use npm install instead of npm ci

## v0.1.4 - Feb 1, 2026

* Initial release
