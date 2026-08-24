# CI/CD Debugging

Use for GitHub Actions, local CI scripts, build pipelines, and test automation.

## Inspect

- Workflow files and reusable actions.
- Script names and working directories.
- Runtime versions and caches.
- Secrets or variables referenced by name only.
- Matrix differences from local development.

## Common Causes

- local command differs from CI command
- missing lockfile or wrong package manager
- runtime version mismatch
- path or working-directory mismatch
- test order or timezone dependency
- missing service container or health check
- cache restoring stale generated files

## Output

Tie every recommendation to a workflow file, script, log line, or manifest.
