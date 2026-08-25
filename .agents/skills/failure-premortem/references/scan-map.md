# Scan Map

Use this to gather evidence before simulating failures. Keep the scan proportional to the user's goal.

## Project Shape

- Read nearest `AGENTS.md` and repo docs.
- Identify language, framework, package manager, runtime versions, and app entrypoints.
- Locate tests, validation scripts, CI workflows, Dockerfiles, compose files, and deployment-like config.
- Identify generated files, build outputs, and package artifacts.

## Configuration

- Inspect config loading paths and environment variable names.
- Compare required config against `.env.example`, docs, compose files, CI variables, and appsettings templates.
- Do not print secrets. Mention secret-dependent files by path and purpose only.

## Runtime Behavior

- Identify HTTP servers, CLIs, background workers, schedulers, queues, database connections, caches, external APIs, and file storage.
- Look for startup validation, health checks, graceful shutdown, retries, timeouts, and idempotency.
- Note ports, bind addresses, volumes, service names, and health checks.

## Data And State

- Inspect migrations, schema files, seed data, fixtures, local database setup, and persistence code.
- Look for destructive operations, batch jobs, import/export, and cache invalidation.

## Validation Surface

- Identify unit, integration, smoke, contract, and end-to-end checks.
- Identify the narrowest command that would catch each simulated failure.
