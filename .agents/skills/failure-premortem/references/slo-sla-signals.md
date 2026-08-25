# SLA/SLO And Reliability Signals

This skill can detect **risk indicators** for SLA/SLO failure from source and config. It cannot prove actual SLA/SLO compliance without runtime data.

## What Can Be Detected From Source/Config

- Missing timeout on outbound calls.
- Missing retry, backoff, or idempotency around transient failures.
- Unbounded memory growth: arrays, caches, queues, file reads, request body buffering.
- Missing pagination or streaming for large data.
- Startup path can crash from missing config, migration mismatch, or unavailable dependency.
- Health check missing, shallow, or not aligned with real readiness.
- No graceful shutdown for servers, workers, or queue consumers.
- No structured error logging around critical paths.
- No metrics around latency, error rate, throughput, saturation, or queue depth.
- Container memory limits too low, absent, or inconsistent with workload.
- CI/build lacks smoke tests for app boot or config validation.

## What Usually Needs Runtime Data

- Actual availability percentage.
- p95/p99 latency.
- error budget burn rate.
- real memory high-water mark.
- CPU saturation.
- container restart frequency.
- OOMKilled events.
- crash loop frequency.
- traffic mix and peak load behavior.

## OOM Risk Indicators

- Reading whole files, request bodies, or query results into memory.
- In-memory cache without max size, TTL, or eviction.
- Queue/buffer with no bound or backpressure.
- Image/video/PDF processing without streaming or temp-file strategy.
- Large JSON serialization/deserialization on hot paths.
- Missing container memory limit or no monitoring for memory.

## Crash Risk Indicators

- Missing startup config validation.
- Unhandled async errors or rejected promises.
- Panics/exceptions escaping request or worker boundaries.
- Database migrations assumed but not checked.
- Required files assumed present at runtime.
- Background worker exits on one bad message.

## SLO-Oriented Output

When reliability matters, include:

- likely SLI affected: availability, latency, error rate, freshness, durability
- suspected SLO risk: what objective could be missed
- evidence: source/config indicator
- detection gap: metric/log/alert missing
- mitigation: code/config/test/observability change
