# Agent Prompts

## Worker

```text
Use the worker role for this bounded implementation task:

<task>

Write only in these areas if possible: <paths>. Preserve unrelated files and user edits. Follow existing repo patterns and relevant coding policies. Run the narrowest validation command and list changed files.
```

## Reviewer

```text
Use the reviewer role to review this implementation for correctness, regressions, security-sensitive behavior, and missing tests:

<summary or diff context>

Lead with findings grounded in file references. Avoid style-only feedback.
```
