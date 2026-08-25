---
name: system-design
description: Use for software architecture and system design decisions: requirements, components, data flow, APIs, consistency, scalability, reliability, security boundaries, tradeoffs, and ADR-style outputs.
---

# System Design

Use this skill for architecture-level thinking before implementation or when evaluating a system design.

## Workflow

Anchor on requirements and constraints before proposing architecture. Separate functional requirements from quality attributes such as reliability, latency, cost, operability, security, and maintainability.

Use `tech-brainstorm` for option exploration and tradeoff comparison. Use `stage-design` when the design will become an implementation plan. Use `policy-coding` only for stack-specific constraints. Use `reviewer` for critical design review when decisions are hard to reverse.

Read [references/architecture-lenses.md](references/architecture-lenses.md) for design lenses, [references/tradeoff-rubric.md](references/tradeoff-rubric.md) for comparison, and [references/system-design-template.md](references/system-design-template.md) for structured output.

## Output

Prefer a compact architecture note with diagrams described textually when useful. Name assumptions, tradeoffs, failure modes, and validation strategy.
