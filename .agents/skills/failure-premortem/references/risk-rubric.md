# Risk Rubric

Rank each scenario by these dimensions.

## Likelihood

- High: evidence shows a common path, missing guard, or known local/prod mismatch.
- Medium: plausible under realistic user/environment conditions.
- Low: requires unusual conditions or several failures together.

## Impact

- High: data loss, security issue, app unavailable, failed critical workflow, expensive recovery.
- Medium: feature broken, degraded reliability, manual fix required.
- Low: local annoyance, clear workaround, limited scope.

## Detectability

- High: existing test, health check, log, metric, or alert would reveal it clearly.
- Medium: visible symptom exists but diagnosis is indirect.
- Low: silent corruption, swallowed error, missing telemetry, or late discovery.

## Reversibility

- High: config/docs/test/code change can be backed out easily.
- Medium: rollback possible but requires coordination or data repair.
- Low: migration, data deletion, public contract, or security exposure.

## Confidence

- High: scenario is grounded in direct file evidence.
- Medium: evidence is partial or pattern-based.
- Low: hypothesis needs more runtime or domain context.

Prioritize high impact + high likelihood + low detectability first.
