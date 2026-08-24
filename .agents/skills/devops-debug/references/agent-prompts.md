# Agent Prompts

## Explorer

```text
Use the explorer role to inspect this DevOps failure: <symptom or command>.

Stay read-only. Map relevant config, scripts, logs if available, env references by name only, and likely causes. Return the cheapest validation checks and likely edit points with file references.
```

## Worker

```text
Use the worker role for this bounded DevOps fix: <specific fix>.

Preserve unrelated files. Make the smallest change, validate with the narrowest relevant command, and report remaining risk or blocked checks.
```

## Reviewer

```text
Use the reviewer role to review this DevOps/config change for regressions and security-sensitive behavior.

Focus on credentials handling, environment behavior, deployment impact, data persistence, rollback, and missing validation. Lead with findings and file references.
```
