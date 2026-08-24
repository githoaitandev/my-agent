---
name: local-dev-setup
description: Use to get a project running on a personal development machine: discover runtimes, install steps, env files, local services, dev servers, ports, and validation commands. Do not use for production release readiness.
---

# Local Dev Setup

Use this skill when the user wants to install, run, repair, or document a local development environment.

## Workflow

First discover the stack and declared setup path. Read manifests, README/setup docs, env examples, container config, task runners, and scripts. Do not install dependencies, start services, or mutate config until the needed action is clear and allowed by the current permission model.

Use the `explorer` subagent for unfamiliar repos or multi-service projects. Use the `worker` subagent only for bounded edits such as fixing a setup script, adding a missing env example, or improving local docs after the problem is understood.

Read [references/setup-flow.md](references/setup-flow.md) for the setup checklist. Read [references/agent-prompts.md](references/agent-prompts.md) when delegating to subagents.

## Output

Return:

- detected stack and required tools
- install and run commands
- required env files and local services
- ports and URLs
- validation command
- blockers or actions that need user approval

Prefer commands already declared by the repo over invented commands.
