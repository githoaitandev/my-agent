# Debug Flow

## Evidence First

- Capture the exact failing command and the first meaningful error.
- Check recent changes if git history or diff is relevant.
- Identify whether the failure is local environment, dependency, config, code, network, permissions, or service state.
- Prefer reading declared config over guessing defaults.

## Hypothesis Loop

For each hypothesis:

1. Name the hypothesis.
2. Identify the file, command, or log that can confirm it.
3. Run or inspect the narrowest check.
4. Update the hypothesis before retrying.

Stop retrying when the command fails the same way without new evidence.

## Fix Boundary

Good fixes are narrow:

- correct a command, path, port, env var name, or compose service
- align docs/scripts with actual tooling
- fix build or startup config
- add missing validation around config loading

Ask before broad toolchain changes, destructive cleanup, credential changes, or production-affecting actions.

## Validation

- Re-run the failing command when feasible.
- If full validation is expensive or blocked, run the nearest cheaper check and report the gap.
- Include rollback notes for config changes that can affect deployment or shared services.
