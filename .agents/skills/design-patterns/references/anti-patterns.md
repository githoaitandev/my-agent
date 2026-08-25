# Anti-Patterns

- Pattern for pattern's sake: abstraction without repeated pressure.
- God object/service: one type owns too many responsibilities.
- Anemic domain with scattered business rules: data types have no behavior and logic is duplicated.
- Boolean parameter explosion: call sites cannot reveal intent.
- Leaky abstraction: callers need to know hidden implementation details.
- Hidden global state: tests and runtime behavior become order-dependent.
- Over-mocking: tests lock implementation instead of behavior.
- Framework leakage: domain logic depends on framework details unnecessarily.

When refactoring, remove the smallest source of pain first.
