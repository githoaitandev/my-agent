---
name: implementation-planner
description: Use before coding when a request is vague, broad, risky, or cross-cutting: define scope, assumptions, likely files, plan, validation, risks, and whether subagents should help. Do not use for tiny obvious edits.
---

# Implementation Planner

Use this skill to turn an implementation request into a bounded engineering plan before edits begin.

## Workflow

Clarify the goal, constraints, and expected behavior. Inspect enough local context to identify likely files and validation commands. Keep the plan proportional to the risk and avoid ceremony for small changes.

Use the `explorer` subagent when relevant files or architecture are unclear. Use the `reviewer` subagent to critique the plan for broad, risky, security-sensitive, or hard-to-reverse changes. Use the `worker` subagent only after the plan is accepted or when the user has already asked to implement.

Read [references/planning-template.md](references/planning-template.md) for structured plans. Read [references/risk-rubric.md](references/risk-rubric.md) when deciding how much planning or review is justified. Read [references/agent-prompts.md](references/agent-prompts.md) when delegating to subagents.

## Output

Return:

- goal and assumptions
- likely files or areas
- proposed change plan
- validation command
- risks and rollback notes
- open questions only if they materially change the plan

If proceeding directly to implementation, state the chosen plan briefly before editing.
