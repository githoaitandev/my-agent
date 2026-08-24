---
name: devops-debug
description: Use for debugging development operations issues: CI failures, Docker or Compose problems, env vars, ports, local services, build scripts, deployment config, logs, and process startup failures. Avoid production-changing actions unless explicitly requested and approved.
---

# DevOps Debug

Use this skill when the user reports a failing command, service, container, CI job, deployment-like config, or local environment problem.

## Workflow

Start from evidence: exact command, error output, logs, changed files, environment assumptions, and expected behavior. Build a short hypothesis list, then test the cheapest hypothesis first.

Use the `explorer` subagent for config/log mapping when the failure spans multiple files or tools. Use `worker` for a bounded fix after the likely cause is known. Use `reviewer` when the fix touches security-sensitive config, credentials handling, deployment behavior, data persistence, or broad automation.

Read [references/debug-flow.md](references/debug-flow.md) for the general debugging path. Read the focused references only when relevant: [references/ci-cd.md](references/ci-cd.md), [references/docker.md](references/docker.md), or [references/agent-prompts.md](references/agent-prompts.md).

## Output

Return:

- symptom and evidence
- likely cause
- fix applied or proposed
- validation result
- remaining risk or required user action

Do not expose secrets. Do not mask uncertainty with confident guesses.
