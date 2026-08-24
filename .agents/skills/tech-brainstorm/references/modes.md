# Brainstorm Modes

Use these modes selectively. A good brainstorm usually combines two or three modes, not the entire list.

## Explore

Use when the user needs options before committing to implementation.

Useful techniques:

- **Divergent thinking**: produce several meaningfully different options before evaluating them.
- **Alternative architectures**: compare different shapes of the system, such as local-first vs server-first, sync vs async, monolith vs service boundary, framework-native vs custom abstraction.
- **Analogy transfer**: borrow patterns from adjacent domains such as compilers, queues, spreadsheets, version control, observability, games, or workflow engines.
- **Constraint inversion**: ask what changes if a common tool, dependency, budget, or assumption is unavailable.

Good output: distinct options with the main tradeoff for each.

## Challenge

Use when the user has a preferred direction and wants a technical Devil's Advocate.

Useful techniques:

- **Assumption busting**: list implicit assumptions and test which ones are fragile.
- **Counterexample search**: find realistic cases where the proposed solution performs badly.
- **Pre-mortem**: assume the solution failed after release and identify likely causes.
- **Complexity audit**: separate necessary complexity from incidental complexity.

Good output: risks, weak assumptions, and possible mitigations without overstating uncertainty.

## Stress Test

Use when the user needs confidence around behavior under pressure.

Useful techniques:

- **Edge-case storming**: enumerate boundary values, invalid states, concurrency hazards, ordering issues, partial data, and recovery paths.
- **Failure-mode analysis**: inspect network failures, dependency failures, retries, idempotency, persistence, observability, and rollback.
- **Scale lens**: test whether the design changes at 10x data, 10x users, 10x latency sensitivity, or 10x operational load.
- **Abuse-case lens**: consider misuse, confused users, prompt injection, data exposure, permission mistakes, and unsafe automation.

Good output: failure scenarios ranked by likelihood and blast radius.

## Compare

Use when there are multiple viable options.

Useful techniques:

- **Tradeoff matrix**: compare option, benefit, cost, risk, reversibility, and when to choose it.
- **Decision criteria weighting**: identify which criteria should dominate the decision.
- **Reversibility check**: prefer reversible choices when uncertainty is high.
- **Migration path comparison**: compare not only end states, but also the path from current state to target state.

Good output: a compact comparison and a clear recommendation or shortlist.

## Decide

Use when the user is ready to choose a direction.

Useful techniques:

- **Decision memo**: summarize context, decision, rationale, consequences, and follow-up work.
- **ADR outline**: produce status, context, decision, consequences, and alternatives considered.
- **Next-step plan**: turn the chosen direction into implementation steps and validation.
- **Open-question filter**: keep only questions that can materially change the decision.

Good output: a recommendation that names caveats, validation steps, and rollback considerations.
