# My Agent Instructions

This repository is a reusable Codex agent profile. Its root files are intended to be installed into other projects.

## Operating Model

- `AGENTS.md` contains durable project instructions.
- `.agents/skills/` contains repo-local Codex skills.
- `.codex/` contains Codex runtime config, subagents, hooks, and hook scripts.
- `install.sh` (macOS/Linux/Git Bash) and `install.ps1` (Windows PowerShell) apply this profile to the current working directory or to an explicit target path.

## Workflow

- Preserve unrelated user changes.
- Before editing, identify the project files and behavior being changed.
- Use the narrowest useful validation command after changes.
- Use subagents only when the user asks for parallel review, repo exploration, or multi-part implementation.

## Subagents

- Use `explorer` for read-only codebase mapping.
- Use `reviewer` for read-only correctness, regression, security-sensitive, and test-gap review.
- Use `worker` for bounded implementation work.

