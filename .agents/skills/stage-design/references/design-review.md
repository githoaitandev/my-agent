# Design Review

Use this when critiquing a proposed design.

## Review Lenses

- Correctness: Does the design satisfy the actual behavior?
- Fit: Does it match the repo's existing architecture and conventions?
- Complexity: Is complexity necessary or incidental?
- Reversibility: Can the decision be changed later?
- Boundaries: Are module, API, data, and ownership boundaries clear?
- Failure: What happens under partial failure, invalid input, concurrency, or dependency outage?
- Validation: Is there a narrow test or check that proves the design?
- Rollback: How can the change be backed out?

## Findings

Lead with concrete risks. Avoid style-only critique unless style hides a real maintenance or correctness problem.
