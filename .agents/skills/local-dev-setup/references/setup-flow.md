# Local Setup Flow

## Discovery

- Read repo instructions and setup docs.
- Identify runtime versions through files such as `.nvmrc`, `.node-version`, `.python-version`, `global.json`, `go.mod`, `rust-toolchain`, Dockerfiles, or lockfiles.
- Identify package manager from lockfiles and scripts.
- Identify local services: databases, caches, queues, object storage, emulators, and compose profiles.
- Identify env files and templates without printing secret values.

## Execution

- Prefer documented setup commands.
- If dependency installation or service startup needs network or elevated permissions, request approval through the normal tool flow.
- If a command fails, preserve the first meaningful error and inspect config before retrying.
- Avoid repeated retries without a changed hypothesis.

## Repair

Good bounded repairs include:

- missing script in docs
- stale command names
- absent `.env.example` key documentation without real secrets
- incorrect local port references
- setup script that assumes the wrong working directory

Avoid broad rewrites of project tooling unless the user asks.

## Validation

- Verify the narrowest useful command: version check, install check, unit test, build, health endpoint, or dev server startup.
- Report any services that were not started and why.
