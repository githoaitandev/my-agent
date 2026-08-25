---
name: failure-premortem
description: Use before implementation, merge, launch, or risky local operation to scan a project, simulate plausible failure scenarios from source/config behavior, rank risks, and propose prevention, detection, mitigation, validation, and rollback options.
---

# Failure Premortem

Use this skill when the user wants to find likely failures before they happen. It is useful for local projects, pre-merge review, demo readiness, internal tools, and production-like release planning.

This is a read-first workflow. Do not change code unless the user explicitly asks to implement mitigations after the risk report.

## Workflow

Scan the project for real evidence: repo instructions, manifests, entrypoints, config loading, env examples, Docker/Compose, CI scripts, tests, database/migrations, auth boundaries, external services, background jobs, and validation commands.

Use `repo-explorer` or the `explorer` subagent when the repo is unfamiliar or the risk surface spans multiple areas. Use `policy-coding` to load relevant stack/domain policy. Use `system-design` for architecture-level reliability risks. Use `devops-debug` references when risks involve CI, Docker, env, ports, startup, or services. Use `reviewer` to challenge broad or high-risk reports.

Read [references/scan-map.md](references/scan-map.md) for project scanning, [references/failure-catalog.md](references/failure-catalog.md) for scenario families, [references/slo-sla-signals.md](references/slo-sla-signals.md) for reliability and OOM/crash indicators, [references/risk-rubric.md](references/risk-rubric.md) for ranking, [references/solution-patterns.md](references/solution-patterns.md) for mitigations, [references/output-formats.md](references/output-formats.md) for report shape, and [references/agent-prompts.md](references/agent-prompts.md) when delegating.

## Output

Return a ranked risk report with:

- evidence from files, config, or missing validation
- simulated failure scenario
- likely trigger, actor, and affected behavior
- likelihood, impact, detectability, reversibility, and confidence
- proposed prevention, detection, mitigation, validation, and rollback
- open questions that materially affect risk

Be explicit about uncertainty. Source/config can reveal risk indicators, but actual SLA/SLO compliance requires runtime metrics, logs, traces, load profiles, and real operational objectives.
