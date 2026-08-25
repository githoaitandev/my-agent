# Agent Prompts

## Explorer

```text
Use the explorer role to scan this project for failure-premortem evidence.

Stay read-only. Map manifests, entrypoints, config/env loading, Docker/Compose, CI, tests, database/migrations, external services, background jobs, health checks, logging/metrics, and likely risk surfaces. Return concise findings with file references and do not propose broad fixes yet.
```

## Reviewer

```text
Use the reviewer role to challenge this failure-premortem report:

<report>

Focus on missing high-impact failure modes, weak evidence, over-ranked risks, under-ranked risks, missing validation, security-sensitive behavior, and operational blind spots. Lead with concrete findings.
```

## Worker

```text
Use the worker role to implement this bounded mitigation:

<mitigation>

Preserve unrelated files. Make the smallest defensible change. Validate with the narrowest relevant command and report changed files.
```
