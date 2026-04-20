---
title: "Getting Started with CIS"
description: Learn to brainstorm, innovate, and solve problems with Creative Intelligence Suite
---

Unlock creative breakthroughs using AI-powered workflows with specialized agents that guide you through ideation, design thinking, innovation strategy, and systematic problem-solving.

## What You'll Learn

- Install and initialize Creative Intelligence Suite
- Run your first brainstorming session with Carson
- Use design thinking for human-centered solutions
- Apply innovation strategy to find market opportunities
- Solve complex problems with systematic analysis
- Craft compelling narratives with Sophia

:::note[Prerequisites]
- **BMad Method installed** — CIS is a module that extends BMad Method
- **AI-powered IDE** — Claude Code, Cursor, Windsurf, or similar
- **A challenge or idea** — Something to brainstorm, solve, or improve
:::

:::tip[Quick Path]
**Install CIS** — Select during BMad setup or `npx bmad-method install`
**Try brainstorming** — `/cis-brainstorm` with Carson
**Explore workflows** — Each agent specializes in creative approaches
**Fresh chats** for each workflow to avoid context issues.
:::

## Understanding CIS

The Creative Intelligence Suite (CIS) extends BMad Method with tools for the fuzzy front-end of development—where ideas are born, problems are reframed, and solutions emerge through structured creativity.

### CIS Agents and Workflows

| Agent | Workflow | Purpose |
| ----- | -------- | ------- |
| **Carson** | `brainstorming` | Generate ideas using 36 techniques across 7 categories |
| **Maya** | `design-thinking` | Human-centered design through 5 phases |
| **Victor** | `innovation-strategy` | Identify disruption opportunities and business model innovation |
| **Dr. Quinn** | `problem-solving` | Systematic problem diagnosis and root cause analysis |
| **Sophia** | `storytelling` | Craft compelling narratives using 25 story frameworks |
| **Caravaggio** | *(coming soon)* | Structure persuasive presentations |

### When to Use CIS

| Situation | Use This |
| ----------- | ---------- |
| Stuck on a problem | `/cis-problem-solving` |
| Need fresh ideas | `/cis-brainstorm` |
| Designing for users | `/cis-design-thinking` |
| Finding market gaps | `/cis-innovation-strategy` |
| Telling your story | `/cis-storytelling` |

## Installation

CIS installs as a module during BMad Method setup. If you haven't installed BMad Method yet:

```bash
npx bmad-method install
```

When prompted to select modules, choose **Creative Intelligence Suite**.

The installer adds CIS agents and workflows to your `_bmad/` folder.

:::note[Already have BMad Method installed?]
Run the installer again and select Creative Intelligence Suite to add it to your existing setup.
:::

## Step 1: Your First Brainstorming Session

Let's start with the most popular workflow—brainstorming with Carson.

### Load the Brainstorming Coach

In a fresh chat, load Carson:

```
/cis-brainstorm
```

### Run the Session

Carson will ask what you want to brainstorm about. Provide a topic—anything from "improving user onboarding" to "new product ideas for pet owners."

Carson guides you through:

1. **Topic exploration** — Understanding what you're brainstorming
2. **Technique selection** — Choose from 36 techniques or let Carson recommend one
3. **Ideation** — Carson facilitates using "Yes, and..." methodology
4. **Idea capture** — Results saved to `_bmad-output/brainstorming-{date}.md`

### Example Session

```
You: /cis-brainstorm
Carson: What would you like to brainstorm about?
You: Ways to reduce user churn
Carson: Let's explore this! I recommend the SCAMPER technique...
    [Guides you through 7 creative angles]
    [Generates diverse, actionable ideas]
```

## Step 2: Human-Centered Design with Maya

When you need to design solutions for real people, Maya's design thinking workflow helps you empathize, define, ideate, prototype, and test.

### Load the Design Thinking Coach

```
/cis-design-thinking
```

### The Five Phases

| Phase | What Happens |
| ----- | ------------ |
| **Empathize** | Understand user needs and pain points |
| **Define** | Frame the problem from user perspective |
| **Ideate** | Generate diverse solutions |
| **Prototype** | Create rapid testable artifacts |
| **Test** | Validate with real users |

### What You Get

Output saved to `_bmad-output/design-thinking-{date}.md`:

- Design challenge statement and point-of-view
- User insights and empathy mapping
- "How Might We" questions
- Solution concepts with prototypes
- Test plans and iteration roadmap

## Step 3: Strategic Innovation with Victor

Victor helps you find disruption opportunities and business model innovation.

### Load the Innovation Strategist

```
/cis-innovation-strategy
```

### Strategic Analysis

Victor guides you through:

1. **Market landscape** — Competitive dynamics and trends
2. **Jobs-to-be-Done** — What users are actually trying to accomplish
3. **Blue Ocean Strategy** — Find uncontested market space
4. **Business model innovation** — New ways to create and capture value

### What You Get

Output saved to `_bmad-output/innovation-strategy-{date}.md`:

- Market disruption analysis
- Innovation opportunity mapping
- Business model canvas alternatives
- Strategic priorities and implementation roadmap

## Step 4: Systematic Problem-Solving with Dr. Quinn

For complex, stubborn problems, Dr. Quinn applies systematic methodologies to find root causes and effective solutions.

### Load the Problem Solver

```
/cis-problem-solving
```

### The Analytical Process

Dr. Quinn treats problems like puzzles:

1. **Problem diagnosis** — Separate symptoms from root causes
2. **Framework selection** — TRIZ, Theory of Constraints, Five Whys, Systems Thinking
3. **Solution generation** — Multiple approaches evaluated
4. **Implementation planning** — Actionable steps with risk mitigation

### What You Get

Output saved to `_bmad-output/problem-solution-{date}.md`:

- Root cause analysis
- Solution evaluation matrix
- Implementation plan with metrics
- Risk mitigation strategies

## Step 5: Storytelling with Sophia

When you need to persuade, inspire, or connect, Sophia crafts compelling narratives.

### Load the Storyteller

```
/cis-storytelling
```

### Narrative Development

Sophia guides you through:

1. **Purpose definition** — What should the audience feel/think/do?
2. **Framework selection** — Hero's Journey, Story Brand, Three-Act, and more
3. **Character development** — Relatable protagonists and authentic voice
4. **Narrative arc** — Tension, climax, and resolution
5. **Platform adaptation** — Tailored for your medium

### What You Get

Output saved to `_bmad-output/story-{date}.md`:

- Complete narrative with emotional beats
- Character development and dialogue
- Sensory details and vivid moments
- Platform-specific formatting

## What You've Accomplished

You've learned the foundation of creative intelligence with CIS:

- Installed CIS and explored all six agents
- Run a brainstorming session with Carson
- Applied design thinking with Maya
- Analyzed innovation opportunities with Victor
- Solved problems systematically with Dr. Quinn
- Crafted narratives with Sophia

Your `_bmad-output/` folder now contains:

```
your-project/
├── _bmad/
│   └── cis/                          # CIS agents and workflows
├── _bmad-output/
│   ├── brainstorming-{date}.md       # Your ideation session results
│   ├── design-thinking-{date}.md     # Human-centered design artifacts
│   ├── innovation-strategy-{date}.md # Strategic innovation roadmap
│   ├── problem-solution-{date}.md    # Root cause and solutions
│   └── story-{date}.md               # Your crafted narrative
└── ...
```

## Quick Reference

| Workflow | Command | Agent | Purpose |
| -------- | ------- | ----- | ------- |
| `brainstorming` | `/cis-brainstorm` | Carson | Generate diverse ideas |
| `design-thinking` | `/cis-design-thinking` | Maya | Human-centered design |
| `innovation-strategy` | `/cis-innovation-strategy` | Victor | Strategic innovation |
| `problem-solving` | `/cis-problem-solving` | Dr. Quinn | Root cause analysis |
| `storytelling` | `/cis-storytelling` | Sophia | Craft compelling narratives |

## Common Questions

**How do I provide context to a workflow?**

Use the `--data` flag with a file path:

```bash
workflow cis-design-thinking --data /path/to/user-research.md
```

**Can I use multiple CIS workflows together?**

Yes. Start with brainstorming to generate options, then use design thinking to refine user-centered solutions, or innovation strategy to evaluate business potential.

**What's the difference between problem-solving and design thinking?**

Design thinking focuses on user needs and rapid prototyping. Problem-solving applies analytical frameworks to find root causes and evaluate solutions systematically.

**Do I need to use all workflows?**

No. Each workflow stands alone. Use the ones that match your current challenge.

## Getting Help

- **During workflows** — Agents guide you with questions and technique explanations
- **Community** — [Discord](https://discord.gg/gk8jAdXWmj) (#creative-intelligence-suite)
- **Issues** — [GitHub Issues](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite/issues)

## Key Takeaways

:::tip[Remember These]
- **Always use fresh chats** — Start a new chat for each workflow
- **Trust the facilitation** — Agents guide you through proven techniques
- **Capture everything** — Outputs are saved automatically
- **Iterate freely** — Run workflows multiple times as ideas evolve
:::

Ready to think differently? Start your first brainstorming session and discover where structured creativity can take you.
