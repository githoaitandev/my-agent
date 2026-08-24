# Docker And Compose Debugging

Use for Dockerfile, docker compose, container startup, image build, networking, volume, and port problems.

## Inspect

- `Dockerfile`, compose files, `.dockerignore`, entrypoint scripts, and env files.
- Build context and copied files.
- Service names, networks, health checks, ports, volumes, and profiles.
- Runtime user, permissions, and working directory.

## Common Causes

- wrong build context
- missing file due to `.dockerignore`
- host port already in use
- service name mismatch inside compose network
- env file not loaded
- bind mount hiding built files
- health check too strict or too early
- architecture mismatch on local machine

## Validation

Prefer targeted checks such as config rendering, image build, service logs, health endpoint, or one service startup before restarting the whole stack.
