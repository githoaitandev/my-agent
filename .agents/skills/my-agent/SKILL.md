---
name: my-agent
description: Use the My Agent reusable Codex workflow for project setup, repo exploration, review, bounded implementation, and hook-aware development. Trigger when the user mentions My Agent, asks to apply this agent profile, install reusable Codex config, use project subagents, or follow this repo's agent workflow.
---

# My Agent

Use this skill when working in a project that has installed the My Agent profile.

## Behavior

1. Read the nearest `AGENTS.md` before making changes.
2. Check `.codex/agents/` when the user asks for subagents or parallel work.
3. Respect `.codex/hooks.json` and hook outcomes.
4. Keep changes scoped to the user's request.
5. Validate with the narrowest relevant command available in the project.

## Install Or Update

When the user asks to install this profile into a project, run the source repo's installer:

```bash
/path/to/my-agent/install.sh /path/to/target-project
```

Use `--force` only when the user explicitly wants to override existing target files.

## Subagent Roles

- `explorer`: read-only repository mapping.
- `reviewer`: read-only risk and correctness review.
- `worker`: scoped implementation work.

