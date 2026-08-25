# Validation Flow

## Discover

- Read manifest scripts, Makefiles, CI config, and docs.
- Prefer repo-declared commands.
- Identify narrow commands for changed files or packages.

## Run

- Start with the narrowest command that proves the changed behavior.
- Broaden to build/typecheck/lint/full test when shared contracts or generated artifacts changed.
- If commands require services or credentials, report the blocker or request approval.

## Report

Include command, result, and what it proves. If a check fails, separate pre-existing failures from failures caused by the change when possible.
