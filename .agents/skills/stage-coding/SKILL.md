---
name: stage-coding
description: Use during implementation to make scoped code changes safely: inspect relevant context, follow repo patterns and coding policies, preserve unrelated changes, validate narrowly, and report results.
---

# Stage Coding

Use this skill when the user wants implementation, refactoring, bug fixing, or small project edits.

## Workflow

Identify the behavior being changed and the files likely involved before editing. Preserve unrelated user changes. Use existing helpers, framework patterns, and repo conventions before inventing new abstractions.

Load `policy-coding` when language, framework, or domain-specific rules would materially affect the change. Use `implementation-planner` first when the request is vague, broad, risky, or cross-cutting. Use `worker` for a bounded implementation slice only when delegation is useful and write scopes are clear. Use `reviewer` after risky or shared behavior changes.

Read [references/coding-flow.md](references/coding-flow.md) for the default coding loop, [references/change-safety.md](references/change-safety.md) for safety constraints, and [references/agent-prompts.md](references/agent-prompts.md) when delegating.

## Output

Report:

- files changed
- behavior changed
- validation run and result
- checks not run and why
- remaining risk or follow-up
