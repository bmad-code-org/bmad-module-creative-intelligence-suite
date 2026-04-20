---
title: "CIS Configuration"
description: Configure CIS workflows, output locations, and agent behavior
---

Configure Creative Intelligence Suite workflows, output behavior, and agent preferences.

## Configuration File

CIS configuration is stored in:

```
_bmad/cis/config.yaml
```

If the file doesn't exist, CIS uses default values.

## Configuration Options

| Setting | Description | Default |
| ------- | ----------- | ------- |
| **output_folder** | Where workflow outputs are saved | `./_bmad-output/` |
| **user_name** | Name used in workflow facilitation | `User` |
| **communication_language** | Language for agent responses | `english` |

### output_folder

**Where workflow results are saved.**

Absolute or relative path. Workflow outputs are named `{workflow-name}-{date}.md`.

**Example:**

```yaml
output_folder: "./creative-outputs"
# or
output_folder: "/Users/name/Documents/creative-work"
```

**Relative paths** are resolved from project root.

### user_name

**How agents address you during facilitation.**

Used for personalized interaction. Agents weave your name into their responses.

**Example:**

```yaml
user_name: "Alex"
# Carson might say: "Alex, let's try a different angle..."
```

### communication_language

**Language for workflow facilitation.**

Agents communicate in the specified language while maintaining their distinctive personalities.

**Supported values:**

- `english` (default)
- `spanish`
- `french`
- `german`
- `italian`
- `portuguese`

**Example:**

```yaml
communication_language: "spanish"
# Maya facilitará en español manteniendo su estilo jazzístico
```

## Default Configuration

If no config file exists, CIS uses:

```yaml
output_folder: "./_bmad-output/"
user_name: "User"
communication_language: "english"
```

## Creating Configuration

Create or edit `_bmad/cis/config.yaml`:

```yaml
# CIS Configuration

output_folder: "./_bmad-output/"
user_name: "Your Name"
communication_language: "english"
```

## Workflow-Specific Context

Some workflows accept additional context via command-line flags:

### Providing Context Data

Pass context documents to workflows:

```bash
workflow design-thinking --data /path/to/user-research.md
workflow innovation-strategy --data /path/to/market-analysis.md
workflow problem-solving --data /path/to/problem-brief.md
workflow storytelling --data /path/to/brand-guidelines.md
```

Context files should be markdown. Agents incorporate this information into facilitation.

## Environment Variables

CIS respects these environment variables:

| Variable | Purpose | Example |
| ---------- | ------- | ------- |
| `BMAD_OUTPUT_DIR` | Override output folder | `BMAD_OUTPUT_DIR=./outputs` |
| `BMAD_USER_NAME` | Override user name | `BMAD_USER_NAME=Jordan` |
| `BMAD_LANGUAGE` | Override language | `BMAD_LANGUAGE=spanish` |

Environment variables take precedence over config file settings.

## Troubleshooting Configuration

### Outputs Not Appearing

Check output folder path is valid:

```bash
# Test path resolution
ls ./_bmad-output/
```

Ensure the folder exists or CIS can create it.

### Agent Not Using Your Name

Verify `user_name` in `_bmad/cis/config.yaml` is set correctly.

### Language Not Changing

Confirm `communication_language` uses supported values. Custom languages require agent prompt updates.

## Next Steps

- **[Getting Started](/tutorials/getting-started.md)** — Use workflows with default configuration
- **[Workflows Reference](/reference/workflows.md)** — Detailed workflow mechanics
