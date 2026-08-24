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
      active-recall-coach/
        SKILL.md
        references/
          coaching-modes.md
          question-patterns.md
          session-formats.md
      repo-explorer/
        SKILL.md
        references/
          exploration-checklist.md
          agent-prompts.md
      tech-brainstorm/
        SKILL.md
        references/
          modes.md
          output-formats.md
      local-dev-setup/
        SKILL.md
        references/
          setup-flow.md
          agent-prompts.md
      devops-debug/
        SKILL.md
        references/
          debug-flow.md
          ci-cd.md
          docker.md
          agent-prompts.md
      implementation-planner/
        SKILL.md
        references/
          planning-template.md
          risk-rubric.md
          agent-prompts.md
  .codex/
    config.toml
    agents/
      explorer.toml
      recall-coach-tester.toml
      recall-learner-tester.toml
      reviewer.toml
      worker.toml
    hooks.json
    hooks/
      pre_tool_use_policy.py
```

Default install skips existing files. Use `--force` when you want this profile to override the target project's Codex files.
