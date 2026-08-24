# Planning Template

Use this structure when a task needs an explicit implementation plan.

```text
Goal:
...

Assumptions:
- ...

Context checked:
- ...

Likely files:
- ...

Plan:
1. ...
2. ...
3. ...

Validation:
- ...

Risks:
- ...

Rollback:
- ...

Open questions:
- ...
```

Keep open questions short. If a reasonable assumption is safe, state it and continue.

## Good Plans

- fit the existing codebase shape
- identify the smallest useful validation command
- distinguish required work from optional cleanup
- avoid unrelated refactors
- name hard-to-reverse decisions

## Bad Plans

- list generic development steps
- require broad rewrites without evidence
- ask questions that can be answered from local context
- treat every task as high risk
