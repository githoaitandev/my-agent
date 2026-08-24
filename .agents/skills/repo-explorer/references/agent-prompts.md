# Agent Prompts

Use these as starting points when delegating to the `explorer` subagent. Keep prompts bounded to read-only mapping.

## General Repo Map

```text
Use the explorer role to map this repository for the following goal: <goal>.

Stay read-only. Identify architecture, important directories, entrypoints, build/test/dev commands, environment requirements, and likely edit points. Return concise findings with file references and call out unknowns that materially affect the goal.
```

## Focused Area Map

```text
Use the explorer role to inspect only the code paths related to <area or feature>.

Stay read-only. Map relevant files, data flow, dependencies, tests, and risks. Return likely edit points and the narrowest validation command.
```
