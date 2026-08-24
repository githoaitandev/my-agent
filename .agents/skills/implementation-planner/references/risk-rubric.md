# Risk Rubric

Use this rubric to decide how much planning, exploration, and review is appropriate.

## Low Risk

Examples:

- copy change
- isolated test update
- small style-compatible component tweak
- narrow script fix

Handle directly with a short plan or no explicit plan.

## Medium Risk

Examples:

- changing shared helper behavior
- touching config used by multiple commands
- adding a dependency
- modifying local setup or build scripts
- changing API behavior with tests nearby

Use focused exploration and a concise plan. Consider reviewer if behavior is shared.

## High Risk

Examples:

- auth, permissions, payments, secrets, data deletion
- database migrations or persistence semantics
- deployment behavior
- concurrency, retries, queues, background jobs
- cross-package or multi-service changes
- hard-to-rollback architecture changes

Use explorer first when context is incomplete. Use reviewer to critique the plan or final diff when feasible.

## Planning Depth

- More risk: more explicit assumptions, validation, rollback.
- More uncertainty: more exploration before deciding.
- More reversibility: less ceremony needed.
