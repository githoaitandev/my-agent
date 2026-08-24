# Output Formats

Choose a format that matches the user's request. Keep outputs compact unless the user asks for a full design note.

## Option List

Use for early exploration.

```text
Mode: Explore

Options:
- Option A: ...
  Best when: ...
  Main tradeoff: ...
- Option B: ...
  Best when: ...
  Main tradeoff: ...

Next useful question: ...
```

## Challenge Notes

Use for Devil's Advocate, assumption busting, or pre-mortem.

```text
Mode: Challenge

Confirmed facts:
- ...

Assumptions:
- ...

Risks:
- Risk: ...
  Why it matters: ...
  Mitigation: ...

Hardest objection: ...
```

## Stress-Test Notes

Use for edge cases, failure modes, scale, or operations.

```text
Mode: Stress Test

Failure scenarios:
- Scenario: ...
  Likelihood: Low/Medium/High
  Blast radius: Low/Medium/High
  Mitigation: ...

Validation needed:
- ...
```

## Tradeoff Matrix

Use when comparing concrete options.

```text
Mode: Compare

| Option | Benefits | Costs | Risks | Reversibility | Choose when |
| --- | --- | --- | --- | --- | --- |
| A | ... | ... | ... | High/Medium/Low | ... |
| B | ... | ... | ... | High/Medium/Low | ... |

Recommendation: ...
```

## Decision Memo

Use when the user wants a decision or an ADR-like result.

```text
Mode: Decide

Decision:
...

Context:
...

Rationale:
- ...

Alternatives considered:
- ...

Consequences:
- ...

Next steps:
- ...
```

## Implementation Plan

Use only when the user asks to proceed from brainstorm into execution.

```text
Chosen direction:
...

Implementation steps:
1. ...
2. ...
3. ...

Validation:
- ...

Rollback:
- ...
```
