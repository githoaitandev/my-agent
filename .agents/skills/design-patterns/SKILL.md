---
name: design-patterns
description: Use when choosing, evaluating, or explaining software design patterns, architecture patterns, anti-patterns, and code structure tradeoffs. Do not force patterns onto simple code.
---

# Design Patterns

Use this skill when the user asks for design patterns, code organization, refactoring structure, or pattern critique.

## Workflow

Start from the problem shape, not the pattern name. Identify the force that needs a pattern: object creation, extension, coordination, state, dependency direction, boundary isolation, or cross-cutting behavior.

Read [references/pattern-router.md](references/pattern-router.md) to select pattern families. Read only the relevant family reference: [references/creational.md](references/creational.md), [references/structural.md](references/structural.md), [references/behavioral.md](references/behavioral.md), [references/architecture-patterns.md](references/architecture-patterns.md), or [references/anti-patterns.md](references/anti-patterns.md).

Use `policy-coding` when language/framework conventions affect whether a pattern is idiomatic.

## Output

Return:

- problem force
- candidate pattern or simpler alternative
- why it fits or does not fit
- implementation sketch at the right abstraction level
- risks and anti-pattern warning

Prefer no pattern when direct code is clearer.
