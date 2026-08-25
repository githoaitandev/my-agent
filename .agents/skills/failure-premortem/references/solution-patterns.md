# Solution Patterns

Use these to propose actionable mitigation options.

## Prevention

- startup config validation
- schema or request validation
- bounded queues, cache limits, pagination, streaming
- timeouts, retries with backoff, circuit breakers
- idempotency keys for retryable mutations
- safe defaults and explicit feature flags
- least-privilege permissions

## Detection

- focused regression tests
- smoke tests for app boot and health endpoints
- structured logs around critical paths
- metrics for latency, error rate, queue depth, memory, CPU, restarts
- alerts tied to user-visible symptoms
- CI checks for config and packaging

## Mitigation

- fallback path, graceful degradation, retry-safe operations
- clearer error messages and runbook steps
- backpressure and rate limiting
- worker dead-letter handling
- rollback scripts or reversible migrations

## Validation

- reproduce scenario locally when safe
- unit test for pure edge case
- integration test for config, database, worker, or HTTP behavior
- load/smoke check for resource risk
- container startup check for env/port/health risk

## Knowledge Alignment

For each high-ranked risk, explain the concept the developer should understand: timeout, idempotency, readiness, memory bound, transaction, migration, or observability gap.
