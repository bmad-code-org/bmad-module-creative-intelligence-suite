# BMad Creative Intelligence Suite agent persona knowledge

This document is carried by the `cis` module's agent persona skills. It describes only those skills. The module's own document covers how to choose between the session skills.

## The agent personas

Each persona is a conversation with a single named perspective. Offer one when the user asks for it by name or role, or wants that perspective's take without running a full session.

- `bmad-cis-agent-brainstorming-coach` — Carson, brainstorming specialist. Menu: `bmad-brainstorming` (BS).
- `bmad-cis-agent-creative-problem-solver` — Dr. Quinn, problem solver. Menu: `bmad-cis-problem-solving` (PS).
- `bmad-cis-agent-design-thinking-coach` — Maya, design thinking coach. Menu: `bmad-cis-design-thinking` (DT).
- `bmad-cis-agent-innovation-strategist` — Victor, innovation strategist. Menu: `bmad-cis-innovation-strategy` (IS).
- `bmad-cis-agent-storyteller` — Sophia, storyteller. Menu: `bmad-cis-storytelling` (ST).
- `bmad-cis-agent-presentation-master` — Caravaggio, presentation and visual communication expert.

Five of the personas are a front door to one session skill. The session skill does the work and runs fine without its persona, so never present a persona as a required step. A persona names its menu skill under `recommends` in its manifest, and offers to install it when the user picks a menu item whose skill is absent.

Caravaggio is the exception: no session skill stands behind the menu. The persona does the work itself — slide decks, pitch decks, conference talks, video explainer layouts, information visualization, and concept visuals.

A project environment may hold only a subset of these personas.
