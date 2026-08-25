# Architecture Patterns

## Layered Architecture

Use when dependency direction and separation of concerns matter. Avoid layers that only pass data through.

## Hexagonal / Ports And Adapters

Use when domain logic must be isolated from frameworks, databases, or external services.

## CQRS

Use when read and write models have genuinely different needs. Avoid for simple CRUD.

## Event-Driven

Use when asynchronous decoupling, audit trail, or integration events are central. Design idempotency and observability early.

## Modular Monolith

Use when boundaries matter but service-level operational overhead is not justified.

## Microservices

Use when independent deployment and ownership outweigh distributed-systems cost.
