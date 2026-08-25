# Test Strategy

## Choose The Smallest Useful Test

- Unit test: pure logic, validation, transformations, edge cases.
- Integration test: multiple modules, database, filesystem, network boundaries, framework wiring.
- Contract test: API behavior, serialization, status codes, error shape, compatibility.
- UI/component test: user-visible state, interaction, accessibility-critical behavior.
- End-to-end test: critical flows where confidence cannot be gained cheaper.

## Risk-Based Depth

- Low risk: focused test or existing validation command may be enough.
- Medium risk: add or update tests near the changed behavior.
- High risk: test success path, failure path, and rollback or compatibility concerns.

## Good Tests

- assert observable behavior
- use realistic inputs and failure cases
- avoid over-mocking the behavior under test
- fit existing test style and helpers
- fail for the bug or regression they target
