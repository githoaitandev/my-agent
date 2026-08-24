# Agent Prompts

## Explorer

```text
Use the explorer role to gather implementation-planning context for this request: <request>.

Stay read-only. Identify relevant files, current behavior, nearby tests, existing patterns, likely edit points, validation commands, and risks. Return concise findings with file references.
```

## Reviewer

```text
Use the reviewer role to critique this implementation plan:

<plan>

Focus on correctness risks, regressions, missing validation, security-sensitive behavior, and whether the plan fits the existing codebase. Lead with concrete findings and file references when available.
```

## Worker

```text
Use the worker role to implement this bounded plan:

<plan>

Make the smallest defensible change, preserve unrelated files, validate the changed behavior, and report any checks that could not run.
```
