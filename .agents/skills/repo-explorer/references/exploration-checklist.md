# Exploration Checklist

Use only the sections relevant to the current repo and user goal.

## Project Shape

- Read nearest `AGENTS.md` and any repo-local Codex config if present.
- Identify language and framework from manifests such as `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `.csproj`, `pom.xml`, `build.gradle`, `Dockerfile`, and compose files.
- Identify top-level directories and their likely ownership: app, packages, services, tests, infra, docs, scripts.
- Locate entrypoints, routing, dependency injection, background workers, scheduled jobs, CLIs, and config loading.

## Commands

- Prefer commands declared in package scripts, Makefiles, task runners, or docs.
- Separate local dev commands from validation commands.
- Note commands that require network, credentials, containers, databases, or privileged services.

## Testing And Quality

- Locate test framework, test directories, fixtures, and narrow test commands.
- Identify lint, format, typecheck, build, and integration-test commands.
- Prefer the narrowest useful validation command for follow-up work.

## Environment

- Look for `.env.example`, config templates, docker compose services, local database setup, ports, and generated files.
- Do not print secrets. Mention secret-dependent files only by path and purpose.

## Risk Areas

- Flag migrations, auth, permissions, billing, data deletion, concurrency, cache invalidation, background jobs, deployment config, and generated artifacts.
- Distinguish risk from blocker.
