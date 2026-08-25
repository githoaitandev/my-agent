# Design Flow

## Clarify

- Define the user-visible behavior or engineering outcome.
- Name non-goals to prevent scope creep.
- Identify constraints: existing patterns, runtime, data shape, permissions, performance, compatibility, and deadline.
- Separate confirmed facts from assumptions.

## Explore

- Identify the current architecture and likely edit points.
- Consider at least two approaches when the design is not obvious.
- Prefer reversible choices when uncertainty is high.
- Fit existing framework and repo conventions before adding new abstractions.

## Specify

- Define boundaries: modules, APIs, data contracts, config, migrations, UI states, background jobs, and external services.
- Identify failure modes and observability needs when relevant.
- Identify testing and validation before coding starts.

## Decide

- Choose the approach with the best tradeoff for the current goal.
- Name why rejected alternatives were not chosen.
- Keep unresolved questions only when they can change the design materially.
