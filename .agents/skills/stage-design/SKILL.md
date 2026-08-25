---
name: stage-design
description: Use before implementation to shape technical design: clarify goals, constraints, architecture options, API/data boundaries, risks, validation, and review needs. Do not use for tiny obvious edits.
---

# Stage Design

Use this skill when work should be designed before coding: new features, architecture choices, cross-cutting changes, public APIs, data model changes, or hard-to-reverse implementation decisions.

## Workflow

Start from the user's goal and local repo context. Keep design proportional to risk: small tasks need a compact design; broad tasks need explicit tradeoffs and validation.

Use `repo-explorer` or the `explorer` subagent when relevant code paths, commands, or constraints are unclear. Use `tech-brainstorm` when multiple viable approaches need comparison. Use `policy-coding` when language, framework, or domain policies should shape the design. Use `reviewer` for broad, risky, security-sensitive, or hard-to-reverse designs.

Read [references/design-flow.md](references/design-flow.md) for the design checklist, [references/design-review.md](references/design-review.md) for critique criteria, and [references/agent-prompts.md](references/agent-prompts.md) when delegating.

## Output

Return the smallest useful design artifact:

- goal and non-goals
- constraints and assumptions
- selected approach and alternatives considered
- affected files or boundaries
- validation plan
- risks, rollback, and open questions

Do not proceed to implementation unless the user asked to continue or the task already implies coding.
