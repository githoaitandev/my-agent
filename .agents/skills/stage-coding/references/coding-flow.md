# Coding Flow

## Before Editing

- Read the nearest `AGENTS.md`.
- Check git status and avoid overwriting unrelated work.
- Inspect relevant files and existing patterns.
- Identify the narrowest validation command.
- Load only relevant coding policies.

## Editing

- Keep changes scoped to the requested behavior.
- Prefer local helpers and established abstractions.
- Add a new abstraction only when it removes real complexity or matches an established pattern.
- Avoid metadata churn, broad rewrites, and unrelated formatting.
- Update tests or validation when behavior changes.

## After Editing

- Run the narrowest useful validation.
- Inspect the diff for accidental changes.
- Report blocked checks honestly.
