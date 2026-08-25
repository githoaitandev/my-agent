# Output Formats

## Compact Report

```text
Mode: Failure Premortem

Scope:
...

Top risks:
1. <risk title>
   Evidence: <file/config/absence>
   Scenario: <trigger -> failure -> impact>
   Ranking: Likelihood High/Medium/Low, Impact High/Medium/Low, Detectability High/Medium/Low, Reversibility High/Medium/Low, Confidence High/Medium/Low
   Solutions:
   - Prevent:
   - Detect:
   - Mitigate:
   - Validate:

Open questions:
- ...
```

## SLO-Oriented Report

```text
Reliability risk:
...

Likely SLI affected:
- Availability / latency / error rate / freshness / durability

Possible SLO miss:
...

Evidence:
- ...

Detection gap:
- Missing metric/log/alert:

Recommended changes:
- Code/config:
- Test:
- Observability:
- Runbook:
```

## Solution Matrix

```text
| Risk | Prevent | Detect | Mitigate | Validate | Owner question |
| --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... |
```

Keep reports ranked. Avoid listing every imaginable failure when there is no project evidence.
