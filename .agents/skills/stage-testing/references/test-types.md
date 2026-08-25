# Test Types

## Unit

Use for deterministic functions, validators, parsers, state transitions, and edge cases.

## Integration

Use when behavior depends on framework wiring, dependency injection, persistence, external processes, filesystem, or service boundaries.

## Contract

Use for public APIs, event schemas, CLI output, generated files, and cross-package interfaces.

## Regression

Use when fixing a bug. The test should fail before the fix or at least directly cover the broken behavior.

## Smoke

Use for local setup, CLI startup, app boot, health endpoints, and dev server checks.
