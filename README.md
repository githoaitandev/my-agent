# My Agent

Simple reusable Codex agent profile.

Install into the current project:

```bash
/path/to/my-agent/install.sh
```

Install into an explicit project:

```bash
/path/to/my-agent/install.sh /path/to/project
```

Overwrite existing target files:

```bash
/path/to/my-agent/install.sh --force
/path/to/my-agent/install.sh /path/to/project --force
```

## Structure

```text
my-agent/
  AGENTS.md
  install.sh
  README.md
  scripts/
    install.py
  .agents/
    skills/
      my-agent/
        SKILL.md
  .codex/
    config.toml
    agents/
      explorer.toml
      reviewer.toml
      worker.toml
    hooks.json
    hooks/
      pre_tool_use_policy.py
```

Default install skips existing files. Use `--force` when you want this profile to override the target project's Codex files.

