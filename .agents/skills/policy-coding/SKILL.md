---
name: policy-coding
description: Use to load concise local coding policies by language, framework, and domain through an index before coding, design, review, or testing. Uses official docs only as fallback for missing or version-sensitive details.
---

# Policy Coding

Use this skill when stack-specific coding rules should shape design, implementation, testing, or review.

## Routing

Read [index.yaml](index.yaml) first. Detect matching policies from user request, file names, manifests, dependencies, and task keywords. Load only the smallest relevant set of policy YAML files.

Policy files are concise local decision rules. They encode default preferences for this agent profile. Repository conventions override generic policy when they are clear and intentional.

Use [sources/official-docs.yaml](sources/official-docs.yaml) only when a policy is missing, stale, version-sensitive, or the user asks for current official guidance.

## Output

When policy affects the answer, mention which policy IDs were loaded and the key rule that changed the decision.

Do not browse or read external documentation for ordinary stable rules. Do not invent a policy pack when no matching policy exists; fall back to repo conventions and general engineering judgment.
