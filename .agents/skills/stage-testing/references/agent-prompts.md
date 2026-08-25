# Agent Prompts

## Explorer

```text
Use the explorer role to find test and validation context for this change: <change>.

Stay read-only. Identify test frameworks, nearby tests, helpers, fixtures, commands, and gaps. Return file references and the narrowest validation command.
```

## Worker

```text
Use the worker role to add or repair tests for this bounded behavior:

<behavior>

Follow existing test patterns. Keep changes scoped. Run the narrowest validation command and report changed files.
```
