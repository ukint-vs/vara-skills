---
name: sails-new-app
description: Use when a builder is starting a new standard Gear/Vara Sails app and needs the correct greenfield sequence before implementation. Do not use for edits to an established repo, Vara.eth or ethexe targets, or non-Sails templates.
---

# Sails New App

## Goal

Move a greenfield request from scope to an approved Sails workspace path without skipping the planning artifacts that later implementation depends on.

## Sequence

1. If the machine does not already have `rustup`, the required Wasm targets, `cargo-sails`, and a local `gear` binary, start with `../sails-dev-env/SKILL.md`.
2. Create the Sails workspace first.
3. Write the feature or app goal to `docs/plans/YYYY-MM-DD-<topic>-spec.md` using `../../assets/spec-template.md`.
4. Route architecture decisions through `../sails-architecture/SKILL.md`.
5. Scaffold with the standard Sails workspace shape: program crate, `build.rs`, Wasm output, and generated-client path kept intact from the start.
6. Keep the standard `build.rs` pipeline intact. In standard Sails workspaces, `cargo build` triggers `build.rs`, which produces `.opt.wasm` and may also emit `.idl` plus client wiring depending on whether generation lives in the program or client crate; then send IDL and client work to `../sails-idl-client/SKILL.md`.
7. Validate before moving to later phases by finishing with `../sails-gtest/SKILL.md`, then `../sails-local-smoke/SKILL.md`.

## Shared Inputs

- `../../references/vara-domain-overview.md`
- `../../references/sails-cheatsheet.md`
- `../../references/sails-program-and-service-architecture.md`
- `../../references/sails-idl-client-pipeline.md`

## Guardrails

- Keep the builder on standard Sails scaffolding and generated clients.
- Keep the standard Sails workspace shape and build-generated `.idl` and `.opt.wasm` artifact path intact, and check the crate's `build.rs` before adding ad hoc generation steps.
- Do not jump into raw Gear primitives when a Sails path already exists.
- Do not skip the planning docs just because the repo is greenfield.
