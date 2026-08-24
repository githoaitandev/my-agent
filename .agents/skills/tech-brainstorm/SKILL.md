---
name: tech-brainstorm
description: Use for software engineering brainstorming before implementation: exploring alternatives, challenging assumptions, stress-testing designs, comparing tradeoffs, and shaping technical decisions. Do not use for ordinary implementation unless the user asks to brainstorm, critique, explore options, or decide between approaches.
---

# Tech Brainstorm

Use this skill when the user wants technical ideation or decision support before code changes. Keep the session grounded in the user's concrete goal, repository context, constraints, and risk tolerance.

Do not turn brainstorming into implementation unless the user explicitly asks to proceed. When the user asks for code changes after brainstorming, summarize the chosen direction first, then continue with normal project workflow.

## Mode Selection

Pick the smallest useful set of modes. Combine modes when that helps the user move from ambiguity to a decision.

- **Explore**: Generate distinct implementation, architecture, API, or workflow options. Use when the user is early, stuck, or asking "what are the options?"
- **Challenge**: Act as a technical Devil's Advocate. Use assumption busting, counterexamples, and pre-mortem reasoning to expose weak points.
- **Stress Test**: Probe edge cases, failure modes, operational risks, scale limits, security-sensitive misuse, migration risks, and rollback paths.
- **Compare**: Turn options into a concise tradeoff matrix with benefits, costs, risks, reversibility, and when each option fits.
- **Decide**: Produce a recommendation, decision memo, ADR outline, or next-step plan when enough information exists.

For deeper mode guidance, read [references/modes.md](references/modes.md) when the request needs more than a lightweight brainstorm or when choosing between multiple techniques is non-obvious.

For structured deliverables, read [references/output-formats.md](references/output-formats.md) when the user asks for a matrix, recommendation, ADR, decision memo, critique, or implementation plan.

## Operating Guidance

Start by naming the active mode or modes in plain language. If the problem is underspecified, make explicit assumptions and proceed; ask only when a missing constraint would materially change the recommendation.

Prefer concrete options over generic advice. For each option, identify the primary tradeoff and the condition under which it becomes the right choice.

When challenging an idea, separate:

- confirmed facts from assumptions
- risks from blockers
- reversible choices from hard-to-reverse choices
- local complexity from system-wide complexity

When comparing options, keep the matrix compact. Use prose when a table would add ceremony without clarity.

## Boundaries

For security threat modeling, compliance review, or production incident analysis, use a dedicated security or incident workflow when available. This skill can surface security or operational concerns during brainstorming, but it is not a substitute for a focused audit.

For product naming, marketing, brand strategy, or non-technical creative ideation, use a more appropriate product or writing workflow unless the user asks for technical constraints or implementation tradeoffs.
