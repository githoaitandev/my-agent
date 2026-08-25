# Change Safety

## Preserve User Work

- Do not revert changes you did not make.
- If user changes overlap with your task, work with them.
- If unrelated files are dirty, ignore them.

## High-Risk Areas

Use extra care for:

- auth, permissions, secrets, billing, data deletion
- migrations and persistence semantics
- deployment, CI, and environment config
- concurrency, retries, queues, background jobs
- shared libraries and public APIs

## Validation

- Prefer focused tests over full suites for narrow changes.
- Run full build or broader checks when shared contracts change.
- If validation needs network, credentials, or services, request approval through normal tool flow.
