# AGENTS.md

## Repository Overview

The Creative Intelligence Suite (CIS) is a BMad Code Method module that provides agents and workflows for creative thinking, brainstorming, design thinking, and innovation strategy. It extends the BMad Core framework with domain-specific tools for the "fuzzy front-end" of development.

**Key principle:** Everything in CIS is natural language (YAML, Markdown, CSV). No code in the core framework—AI agents consume these structured text files directly.

## Development Commands

```bash
# Full test suite (schemas, linting, markdown, formatting)
npm test

# Individual checks
npm run test:schemas          # Test Zod schema validation
npm run validate:schemas      # Validate all *.agent.yaml files
npm run lint                  # ESLint on JS/YAML files
npm run lint:fix              # Auto-fix lint issues
npm run lint:md               # Markdown linting
npm run format:check          # Prettier check
npm run format:fix            # Prettier format

# Documentation
npm run docs:dev              # Start dev server (Astro + Starlight)
npm run docs:build            # Build static site
npm run docs:preview          # Preview built site
```

**Before committing:** Always run `npm test` to validate schemas, linting, and formatting.

## Architecture

### Directory Structure

```
src/
├── agents/              # Agent definitions (*.agent.yaml)
│   └── storyteller/     # Sidecar agents with persistent memory
├── workflows/           # Structured methodologies
│   ├── bmad-cis-design-thinking/
│   ├── innovation-strategy/
│   ├── problem-solving/
│   └── storytelling/
├── teams/               # Multi-agent collaboration configs
└── module.yaml          # Module metadata and installation config
```

### Agent Definition Pattern

Agents are defined in `*.agent.yaml` files with three core components:

1. **metadata**: id (must follow `_bmad/cis/agents/` naming), name, title, icon, module, hasSidecar
2. **persona**: role, identity, communication_style, principles
3. **menu**: trigger → workflow mappings (supports fuzzy matching)
4. **critical_actions**: Initialization tasks for sidecar agents

**Example agent trigger flow:**
- User: `/cis-brainstorm` or just mentions "brainstorm"
- Agent matches trigger → executes associated workflow
- Workflow provides structured methodology via `workflow.md` or legacy `instructions.md`
- Output generated using template.md

### Workflow Structure

Workflows currently ship in two source formats:
- Legacy workflows keep `workflow.yaml` plus `instructions.md`, along with `template.md` and any `*.csv` support files.
- Native skill workflows keep `SKILL.md`, `workflow.md`, `bmad-skill-manifest.yaml`, and only the companion files the skill needs at runtime.

**Key workflow concepts:**
- `standalone: true` - Workflows are self-contained
- `config_source` - Loads variables from `{project-root}/_bmad/cis/config.yaml`
- `web_bundle` - Defines files included in documentation site
- Path references use `{project-root}` and `{installed_path}` placeholders

### Sidecar Agents

Sidecar agents (like Storyteller) maintain persistent memory across sessions:
- Memory location: `{project-root}/_bmad/_memory/{agent-sidecar}/`
- `critical_actions` load memory files on initialization
- Sidecar agents read and update memory between sessions

### Module Installation

CIS installs via BMad Method CLI (`npx bmad-method@alpha install`):
- `src/module.yaml` defines installation config
- `default_selected: false` - User must opt-in
- `visual_tools` - Prompt user for image generation preferences

## Schema Validation

CIS uses Zod schemas to validate `*.agent.yaml` files:
- Schema: `tools/schema/agent.js`
- Test fixtures: `test/fixtures/schemas/`
- Validation checks: required fields, enum values, path formats, error path specification

**When adding/modifying agents:** Run `npm run validate:schemas` before committing.

## Documentation System

The website uses Astro + Starlight following the Diátaxis framework:
- `docs/` - Source content (tutorials, how-to, explanations, reference)
- `website/` - Astro application with custom components
- `llms.txt` / `llms-full.txt` - AI-optimized documentation for LLM consumption

**Documentation build:** `npm run docs:build` runs `node tools/build-docs.mjs`

## Commit Convention

Use conventional commits:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation only
- `refactor:` - Code change (no fix/feature)
- `test:` - Adding tests
- `chore:` - Build/auxiliary tools

Keep messages under 72 characters. See CONTRIBUTING.md for PR guidelines.

## Path Conventions

- All paths use forward slashes, even on Windows
- `{project-root}` placeholder resolves to BMad project root
- Agent IDs must follow `_bmad/cis/agents/{name}.md` format
- Workflow and skill entry paths resolve from `{project-root}/_bmad/` after installation
