# Failure Catalog

Use these categories to generate realistic scenarios. Tie each scenario to evidence from the repo when possible.

## User Behavior

- invalid input, duplicate submit, stale UI state, wrong workflow order
- user lacks permissions, switches account/tenant, uploads bad file
- user cancels midway or retries after timeout

## Environment

- missing env var, wrong env var name, bad config default
- wrong runtime version, OS path difference, timezone/locale mismatch
- port conflict, missing local service, wrong bind address
- filesystem permissions, missing directory, full disk

## Dependency

- package version mismatch, lockfile drift, transitive breaking change
- native module build failure, incompatible architecture
- external API contract change, unavailable service, rate limit

## Data

- migration missing, migration partially applied, rollback impossible
- seed data absent, null/empty edge case, duplicate data
- N+1 query, slow query, lock contention, timezone mismatch
- cache contains stale or incompatible shape

## Operations

- local command differs from CI command
- Docker build context or `.dockerignore` omits required files
- health check missing or too strict
- logs are not actionable, errors are swallowed
- build artifact lacks runtime file or config

## Distributed Systems

- timeout, retry duplication, partial failure, race condition
- background job runs twice or not at all
- queue ordering assumption, idempotency gap, backpressure missing
- network partition, DNS failure, cold start, slow dependency

## Security And Permissions

- secret exposure, unsafe logs, broad token scope
- authorization bypass, tenant boundary mix-up
- unsafe file upload/path traversal
- CORS/cookie/auth config mismatch

## Reliability And Resource Exhaustion

- memory leak, unbounded in-memory queue, unbounded file read
- CPU spike from expensive loop or regex
- process crash on unhandled exception or rejected promise
- container OOMKilled from low memory limit or high startup peak
- connection pool exhaustion, thread pool starvation
