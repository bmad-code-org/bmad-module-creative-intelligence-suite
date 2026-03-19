---
title: "CIS Workflows"
description: Reference for all Creative Intelligence Suite workflows
---

Technical reference for all CIS workflows including inputs, outputs, and invocation methods.

## Workflows Overview

| Workflow | Agent | Purpose | Output File |
| -------- | ----- | ------- | ----------- |
| **brainstorming** | Carson | Generate diverse ideas | `brainstorming-{date}.md` |
| **design-thinking** | Maya | Human-centered design | `design-thinking-{date}.md` |
| **innovation-strategy** | Victor | Strategic innovation | `innovation-strategy-{date}.md` |
| **problem-solving** | Dr. Quinn | Root cause analysis | `problem-solution-{date}.md` |
| **storytelling** | Sophia | Narrative crafting | `story-{date}.md` |

## Brainstorming Workflow

**Purpose:** Generate diverse, creative ideas using structured ideation techniques.

### How to Invoke

```bash
# Direct command
/cis-brainstorm

# With context data
workflow brainstorming --data /path/to/context.md

# Via agent
/bmad-cis-agent-brainstorming-coach
> brainstorm
```

### Inputs

| Input | Description | Required |
| ----- | ----------- | -------- |
| **topic** | What to brainstorm about | Yes |
| **technique** | Which ideation method to use | No (Carson recommends) |
| **mode** | user-selected, AI-recommended, random, progressive | No |

### Outputs

| Section | Contents |
| ------- | -------- |
| **Topic** | Your brainstorming challenge |
| **Technique** | Method applied and rationale |
| **Ideas** | Complete list of all generated ideas |
| **Top Picks** | Recommended ideas for pursuit |
| **Next Steps** | How to move forward |

### Techniques Library

Carson has access to 36 techniques across 7 categories stored in `brainstorming-techniques.csv`:

| Category | Technique Count |
| -------- | --------------- |
| Collaborative | 4 |
| Structured | 4 |
| Creative | 4 |
| Deep | 4 |
| Theatrical | 4 |
| Wild | 4 |
| Introspective | 4 |

---

## Design Thinking Workflow

**Purpose:** Create human-centered solutions through five-phase design thinking.

### How to Invoke

```bash
# Direct command
/cis-design-thinking

# With user research context
workflow design-thinking --data /path/to/user-research.md

# Via agent
/bmad-cis-agent-design-thinking-coach
> design-thinking
```

### Inputs

| Input | Description | Required |
| ----- | ----------- | -------- |
| **design_challenge** | Problem or opportunity being explored | Yes |
| **users_stakeholders** | Primary users and affected parties | No |
| **constraints** | Time, budget, technology limitations | No |

### Outputs

| Section | Contents |
| ------- | -------- |
| **Design Challenge** | Framed opportunity |
| **Point of View** | User-centered problem statement |
| **User Insights** | Empathy findings and personas |
| **How Might We Questions** | Reframed as opportunities |
| **Solution Concepts** | Generated ideas |
| **Prototypes** | Testable artifacts |
| **Test Plan** | Validation approach |

### Design Methods Library

Maya has access to phase-specific design methods in `design-methods.csv`.

---

## Innovation Strategy Workflow

**Purpose:** Identify disruption opportunities and business model innovation.

### How to Invoke

```bash
# Direct command
/cis-innovation-strategy

# With market context
workflow innovation-strategy --data /path/to/market-analysis.md

# Via agent
/bmad-cis-agent-innovation-strategist
> innovation-strategy
```

### Inputs

| Input | Description | Required |
| ----- | ----------- | -------- |
| **market_context** | Industry landscape and competitive intelligence | No |
| **innovation_challenge** | Strategic opportunity or threat | Yes |
| **constraints** | Resource limitations and strategic boundaries | No |

### Outputs

| Section | Contents |
| ------- | -------- |
| **Strategic Question** | Innovation challenge being addressed |
| **Market Analysis** | Forces, trends, competitive landscape |
| **Jobs-to-be-Done** | Unmet customer needs |
| **Blue Ocean Opportunities** | Uncontested market spaces |
| **Business Model** | Value creation and capture |
| **Competitive Advantages** | Sustainable moats |
| **Strategic Roadmap** | Execution priorities |

### Innovation Frameworks Library

Victor has access to strategic frameworks in `innovation-frameworks.csv`:
- Jobs-to-be-Done
- Blue Ocean Strategy
- Disruptive Innovation
- Business Model Canvas
- Value Chain Analysis

---

## Problem Solving Workflow

**Purpose:** Systematic problem diagnosis and root cause analysis.

### How to Invoke

```bash
# Direct command
/cis-problem-solving

# With problem brief
workflow problem-solving --data /path/to/problem-brief.md

# Via agent
/bmad-cis-agent-creative-problem-solver
> problem-solving
```

### Inputs

| Input | Description | Required |
| ----- | ----------- | -------- |
| **problem_description** | Challenge with symptoms and context | Yes |
| **previous_attempts** | Prior solutions and outcomes | No |
| **constraints** | Solution boundaries | No |
| **success_criteria** | How to measure effectiveness | No |

### Outputs

| Section | Contents |
| ------- | -------- |
| **Problem Statement** | Clearly defined challenge |
| **Diagnosis** | Root cause analysis |
| **Solution Options** | Multiple approaches with evaluation |
| **Recommended Solution** | Best option with rationale |
| **Implementation Plan** | Actionable steps |
| **Risk Mitigation** | Potential issues and prevention |
| **Success Metrics** | How to measure results |

### Solving Methods Library

Dr. Quinn has access to analytical frameworks in `solving-methods.csv`:
- Five Whys
- TRIZ
- Theory of Constraints
- Systems Thinking
- Root Cause Analysis

---

## Storytelling Workflow

**Purpose:** Craft compelling narratives using proven story frameworks.

### How to Invoke

```bash
# Direct command
/cis-storytelling

# With brand context
workflow storytelling --data /path/to/brand-info.md

# Via agent
/bmad-cis-agent-storyteller
> story
```

### Inputs

| Input | Description | Required |
| ----- | ----------- | -------- |
| **story_purpose** | Why the story is being told | Yes |
| **target_audience** | Who will experience it | Yes |
| **story_subject** | What or whom it's about | Yes |
| **platform_medium** | Where it will be told | No |
| **desired_impact** | What audience should feel/think/do | No |

### Outputs

| Section | Contents |
| ------- | -------- |
| **Story Framework** | Structure used and rationale |
| **Audience Profile** | Who the story is for |
| **Emotional Arc** | The feeling journey |
| **Complete Narrative** | Full story with vivid details |
| **Character Development** | Voice and transformation |
| **Platform Adaptation** | Formatted for medium |
| **Impact Plan** | Effectiveness measurement |

### Story Frameworks Library

Sophia has access to 25 narrative frameworks in `story-types.csv`:
- Hero's Journey
- Story Brand
- Three-Act Structure
- Before-After-Bridge
- Pixar Pitch
- And 20 more

---

## Output Location

All workflows save output to the configured output folder (default: `./creative-outputs/` or `_bmad-output/` depending on configuration).

Output files include timestamp in format: `{workflow-name}-{YYYY-MM-DD}.md`

## Common Workflow Features

All CIS workflows share:

- **Interactive facilitation** — AI guides through questions, not just generation
- **Technique libraries** — CSV databases of proven methods
- **Context integration** — Optional document input for relevance
- **Structured output** — Comprehensive reports with insights and actions
- **Energy monitoring** — Adaptive pacing based on engagement

## Next Steps

- **[Getting Started](/tutorials/getting-started.md)** — Try your first workflow
- **[Agents Reference](/reference/agents.md)** — Learn about workflow facilitators
- **[Configuration](/reference/configuration.md)** — Customize workflow behavior
