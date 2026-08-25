# Agent Prompts

## Explorer

```text
Use the explorer role to gather design context for this request: <request>.

Stay read-only. Map relevant files, existing architecture, constraints, tests, validation commands, and risks. Return concise findings with file references.
```

## Reviewer

```text
Use the reviewer role to critique this technical design:

<design>

Focus on correctness, regressions, security-sensitive behavior, missing validation, reversibility, and fit with the existing codebase. Lead with concrete findings.
```
