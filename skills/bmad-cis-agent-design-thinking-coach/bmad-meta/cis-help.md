# BMad Creative Intelligence Suite knowledge

This document is carried by every skill in the `cis` module. It covers what the module's skills do and how to choose between them. The agent persona skills carry a further document describing themselves; nothing here describes a module other than `cis`.

## The cis module

Facilitated sessions for creative and strategic thinking: design, innovation, problem solving, and narrative. The skills are not software-specific and work on any subject.

There is no path through this module. No skill has a prerequisite, none hands off to another, and any of them can run at any time — before, during, or entirely outside another module's flow. Suggest the one that fits the user's question and never present one as a required step.

Each skill is a guided conversation. It asks questions, brings a library of named techniques, and builds one document as it goes. The user does the thinking; the skill structures it.

## Choosing a skill

- `bmad-cis-design-thinking` (DT) — the user needs to understand people before deciding what to make. Works through empathy, problem definition, ideation, prototyping, and testing.
- `bmad-cis-innovation-strategy` (IS) — the question is about a market or a business model: where disruption could come from, and what strategic move to make.
- `bmad-cis-problem-solving` (PS) — there is a specific hard problem with no obvious answer. Diagnoses the root cause, generates solutions, evaluates them, and plans the fix.
- `bmad-cis-storytelling` (ST) — the content exists and needs to land with an audience. Picks a story framework and builds the narrative, emotional arc, and variations.

When two fit, ask what the user wants to walk away with. A defined problem points to problem solving; an undefined one about people points to design thinking; a market question points to innovation strategy; a message points to storytelling.

For open-ended idea generation with no structure yet, suggest `bmad-brainstorming`. It belongs to the `core-tools` module, not this one, so it may not be installed.

A project environment may hold only a subset of these skills. When the fitting skill is not installed, say so rather than substituting another.

## During a session

After each section the skill saves the document and offers to continue, run advanced elicitation on the section, bring in party mode, or finish the rest without pausing. Advanced elicitation and party mode are `core-tools` skills; offer them only when they are installed.

## Skills that work well alongside

Every `cis` skill names these `core-tools` skills under `recommends` in its manifest. None is needed to run a session. When one would help and is not installed, say so and offer to install it; `bmad doctor` lists the missing ones.

- `bmad-advanced-elicitation` — pushes a finished section through a chosen critique method.
- `bmad-party-mode` — brings several personas into the session for a group discussion.
- `bmad-forge-idea` — stress-tests a half-formed idea before or after a session.
- `bmad-customize` — authors overrides for a skill's techniques, persona, or menu.

## Party rooms

Every `cis` skill names `bmad-meta/cis-roster.toml` under `roster` in its manifest. It gives `bmad-party-mode` the module's personas and two rooms: `creative-studio` (the six personas) and `midnight-salon` (three personas plus guests). Offer them when the user wants several creative perspectives at once; they need `bmad-party-mode` installed.

## Where things land

Each session writes one dated document under `{output_folder}`:

- design thinking — `design-thinking-{date}.md`
- innovation strategy — `innovation-strategy-{date}.md`
- problem solving — `problem-solution-{date}.md`
- storytelling — `story-{date}.md`

## Setup

Every skill in this module needs the `bmad` hub skill from the `core-tools` module, which installs the shared scripts under `{project-root}/_bmad`. `bmad doctor` reports a missing or outdated dependency.

## When this document is not enough

For a `cis` question this document and the installed skills cannot answer, fetch `https://cis-docs.bmad-method.org/llms.txt` and follow the links relevant to the question. It indexes the full documentation site and names the source repository, which is the final authority on how anything actually behaves.
