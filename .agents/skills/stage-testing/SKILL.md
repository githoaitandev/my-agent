---
name: stage-testing
description: Use to plan, add, repair, or choose tests and validation commands for code changes: unit, integration, contract, UI, regression, and manual checks.
---

# Stage Testing

Use this skill when the user asks for tests, validation, coverage strategy, or when implementation changes need proof of behavior.

## Workflow

Find existing test patterns before adding new ones. Prefer tests that prove behavior and prevent realistic regressions. Keep test scope proportional to risk.

Use `repo-explorer` or `explorer` to locate test frameworks and commands. Use `policy-coding` for language/framework testing conventions. Use `worker` for bounded test additions and `reviewer` for high-risk behavior or missing validation review.

Read [references/test-strategy.md](references/test-strategy.md) for choosing test types, [references/test-types.md](references/test-types.md) for common shapes, [references/validation-flow.md](references/validation-flow.md) for commands, and [references/agent-prompts.md](references/agent-prompts.md) when delegating.

## Output

Return:

- recommended test level
- files or behaviors to test
- validation command
- test gaps that remain
- any checks that require services, credentials, or network
