---
name: repo-explorer
description: Use for read-only repository mapping before changes: architecture, entrypoints, dependencies, commands, tests, risk areas, and likely edit points. Do not use for implementation itself.
---

# Repo Explorer

Use this skill when the user wants to understand a project, prepare for a change, or reduce uncertainty before implementation. Keep exploration read-only unless the user explicitly asks to proceed with changes after the findings.

## Workflow

Start with cheap local signals: nearest `AGENTS.md`, file tree, manifests, scripts, tests, CI config, env examples, and relevant docs. Prefer `rg` and targeted reads over broad file dumps.

For broad or unfamiliar repositories, use the `explorer` subagent for read-only mapping. For small or obvious tasks, explore directly.

Read [references/exploration-checklist.md](references/exploration-checklist.md) when the repo is unfamiliar, multi-language, or has unclear commands. Read [references/agent-prompts.md](references/agent-prompts.md) when delegating exploration to the `explorer` subagent.

## Output

Return a concise map with:

- architecture and important directories
- primary entrypoints and runtime commands
- build, test, lint, and dev commands
- dependency and environment notes
- likely edit points for the user's goal
- risks, unknowns, and next recommended step

Use file references for concrete claims. Do not over-document unrelated parts of the repo.
