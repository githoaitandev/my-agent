# Agent Prompts

## Explorer

```text
Use the explorer role to map local development setup for this repository.

Stay read-only. Identify runtime versions, package manager, install commands, dev server commands, local services, env files/templates, ports, validation commands, and likely setup blockers. Return file references and avoid printing secrets.
```

## Worker

```text
Use the worker role for this bounded local-dev setup fix: <specific fix>.

Preserve unrelated files. Make the smallest change, then run the narrowest relevant validation command. Report any command that could not run and why.
```
