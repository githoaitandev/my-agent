---
name: frontend-3d
description: Route and coordinate frontend 3D implementation across Three.js, React Three Fiber, WebGL, shaders, GSAP, and immersive UI design. Use for web experiences where 3D rendering and interface motion must work together. Do not use for ordinary two-dimensional frontend work.
---

# Frontend 3D

Choose the smallest useful skill set for the requested experience, then follow the repository's normal planning, implementation, and testing workflow.

## Route the work

- Use `prism` when visual direction, page composition, motion, and 3D need one cohesive design treatment.
- Use `r3f-*` skills when the renderer lives in React or uses `@react-three/fiber` and Drei.
- Use `threejs-*` skills for vanilla Three.js, low-level scene control, asset pipelines, shaders, profiling, WebXR, or spatial audio.
- Use `gsap-*` skills for timelines, ScrollTrigger, framework lifecycle integration, and animation performance.
- Combine only the domain skills needed by the request. Do not load every imported skill by default.

When both `r3f-*` and `threejs-*` appear applicable, treat R3F as the React integration layer and load a `threejs-*` skill only for lower-level concepts that the selected R3F skill does not cover.

## Preserve the My Agent workflow

- Use `implementation-planner` or `stage-design` first when the request is broad, risky, or cross-cutting.
- Use `stage-coding` for scoped implementation and `stage-testing` for validation.
- Preserve the project's existing renderer, framework, package manager, design system, and user changes unless the request requires changing them.
- Verify installed package versions before relying on version-sensitive APIs.

## Shared constraints

- Define target devices and a frame-time or quality budget before adding expensive effects.
- Keep high-frequency animation out of React state; update scene objects or motion values in the render loop.
- Lazy-load substantial scenes and assets, cap device pixel ratio where appropriate, and dispose GPU resources on unmount or route changes.
- Provide a non-WebGL or static fallback when 3D is decorative or browser support is uncertain.
- Respect `prefers-reduced-motion`; pause continuous motion and preserve usable interaction and content.
- Keep semantic content and ordinary controls in the DOM unless the experience specifically requires spatial UI.

## Validation

Validate the narrowest relevant surface: build or typecheck first, then exercise resize, route cleanup, context loss where practical, reduced motion, mobile layout, console errors, and representative interaction. Profile before claiming a performance improvement.

## Imported skill provenance

- `r3f-*`: `EnzeD/r3f-skills`, revision `4a11805` (2026-08-31).
- `threejs-*`: `alton47/threejs-skills`, revision `7b8e256` (2026-03-25).
- `gsap-*`: `greensock/gsap-skills`, revision `aed9cfd` (2026-04-21).
- `prism`: `GOODMAN-PRO/prism`, revision `cfbd892` (2026-06-06).
