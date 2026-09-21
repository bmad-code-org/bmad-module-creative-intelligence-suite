# Creative Intelligence Suite

[![Version](https://img.shields.io/npm/v/bmad-creative-intelligence-suite?color=blue&label=version)](https://www.npmjs.com/package/bmad-creative-intelligence-suite)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-%3E%3D3.11-blue?logo=python&logoColor=white)](https://www.python.org)
[![uv](https://img.shields.io/badge/uv-package%20manager-blueviolet?logo=uv)](https://docs.astral.sh/uv/)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

**Think differently.** A collection of agents and workflows for innovation, brainstorming, design thinking, and creative problem-solving.

## About CIS

The Creative Intelligence Suite (CIS) extends BMad Method with tools for the fuzzy front-end of development—where ideas are born, problems are reframed, and solutions emerge through structured creativity.

## The Agents

| Agent | Skill | What they bring |
|-------|-------|-----------------|
| **Carson**, Brainstorming Coach | `bmad-cis-agent-brainstorming-coach` | Guided ideation that pushes past the obvious ideas |
| **Maya**, Design Thinking Coach | `bmad-cis-agent-design-thinking-coach` | Human-centered design through empathy, ideation, and prototyping |
| **Dr. Quinn**, Creative Problem Solver | `bmad-cis-agent-creative-problem-solver` | Root cause diagnosis, then solutions that hold |
| **Victor**, Innovation Strategist | `bmad-cis-agent-innovation-strategist` | Disruption opportunities and business model innovation |
| **Sophia**, Storyteller | `bmad-cis-agent-storyteller` | Narratives built on proven story frameworks |
| **Caravaggio**, Presentation Expert | `bmad-cis-agent-presentation-master` | Plans and critiques decks, pitches, talks, and visuals |

## Installation

CIS installs as plain skills. Install the `bmad` hub skill first, then CIS:

```bash
npx skills add bmad-code-org/BMAD-METHOD --skill bmad
npx skills add bmad-code-org/bmad-module-creative-intelligence-suite
```

Then ask your agent to run `bmad setup` in the project. `bmad status` reports anything a skill still needs. To install one skill, add `--skill <name>` and include `bmod-cis`, the module's record: it carries the help and the party roster for every CIS skill.

## Quick Start

Ask for a skill by name, or describe what you want and let the agent pick:

```
bmad-cis-design-thinking      # Human-centered design process
bmad-cis-problem-solving      # Systematic problem analysis
bmad-cis-innovation-strategy  # Business model and disruption analysis
bmad-cis-storytelling         # Narrative built on a story framework
```

Each skill also has an agent persona, such as `bmad-cis-agent-storyteller`, for a conversation with that one perspective.

## When to Use CIS

| Situation | Use This |
|-----------|----------|
| Stuck on a problem | `bmad-cis-problem-solving` |
| Need fresh ideas | `bmad-brainstorming` (from BMad core tools) |
| Designing for users | `bmad-cis-design-thinking` |
| Finding market gaps | `bmad-cis-innovation-strategy` |
| Telling your product story | `bmad-cis-storytelling` |
| Planning or critiquing a pitch deck | `bmad-cis-agent-presentation-master` |

## Example: Brainstorming Session

```
You: Run bmad-brainstorming
CIS: What would you like to brainstorm about?
You: Ways to improve user onboarding
CIS: Let's use the SCAMPER technique...
    [Guides you through 7 creative angles]
    [Generates diverse, actionable ideas]
```

## Workflow Capabilities

- **Idea Generation** — Multiple ideation frameworks (SCAMPER, Reverse Brainstorming, etc.)
- **Problem Reframing** — Turn obstacles into opportunities
- **User Empathy** — Build deep understanding of user needs
- **Solution Divergence** — Generate many options before converging
- **Narrative Craft** — Shape your product's story

## Team Collaboration

CIS includes team configurations for collaborative creativity:

- **Creative Squad** — Cross-functional creative sessions
- **Design Pair** — Two-person design thinking

## Documentation

**[Creative Intelligence Suite Documentation](http://cis-docs.bmad-method.org)** — Tutorials, how-to guides, and reference

- [Getting Started](http://cis-docs.bmad-method.org/tutorials/)
- [BMad Method Docs](http://docs.bmad-method.org) — Core framework documentation

## Community

- [Discord](https://discord.gg/gk8jAdXWmj) — Share your creative breakthroughs
- [YouTube](https://youtube.com/@BMadCode) — Tutorials, master class, and more
- [X / Twitter](https://x.com/BMadCode)
- [Website](https://bmadcode.com)
- [GitHub Issues](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite/issues) — Report issues

## Support BMad

BMad is free for everyone and always will be. Star this repo, [buy me a coffee](https://buymeacoffee.com/bmad), or email <contact@bmadcode.com> for corporate sponsorship.

## License

MIT License — see [LICENSE](LICENSE) for details.

---

**Creative Intelligence Suite** — Part of the [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD) ecosystem.

[![Contributors](https://contrib.rocks/image?repo=bmad-code-org/bmad-module-creative-intelligence-suite)](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite/graphs/contributors)

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for contributor information.
