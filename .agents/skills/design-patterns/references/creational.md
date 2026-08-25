# Creational Patterns

## Factory

Use when callers should not know concrete construction details. Avoid when direct constructors are clear and stable.

## Builder

Use for complex object construction with many optional values or staged validation. Avoid for simple data containers.

## Singleton

Prefer dependency injection or module-level composition in most application code. Use singleton-like lifetime only when the framework owns lifecycle clearly.

## Prototype

Use when cloning configured objects is safer or cheaper than reconstructing them.
