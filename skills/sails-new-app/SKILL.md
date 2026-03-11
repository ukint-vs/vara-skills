---
name: sails-new-app
description: Use when a builder is starting a new standard Gear/Vara Sails app and needs the correct greenfield sequence before implementation. Do not use for edits to an established repo, Vara.eth or ethexe targets, or non-Sails templates.
---

# Sails New App

## Goal

Move a greenfield request from scope to an approved Sails workspace path without skipping the planning artifacts that later implementation depends on.

## Sequence

1. Write the feature or app goal to `docs/plans/YYYY-MM-DD-<topic>-spec.md` using `../../assets/spec-template.md`.
2. Route architecture decisions through `../sails-architecture/SKILL.md`.
3. When the builder is ready to scaffold, delegate to `sails-new-program`.
4. After scaffold or first implementation, send IDL and client work to `../sails-idl-client/SKILL.md`.
5. Finish with `../sails-gtest/SKILL.md`, then `../sails-local-smoke/SKILL.md`.

## Shared Inputs

- `../../references/vara-domain-overview.md`
- `../../references/sails-cheatsheet.md`

## Specialist Skills To Delegate

- `idea-to-spec`
- `sails-program-architecture-patterns`
- `sails-new-program`
- `sails-idl-and-client-pipeline`

## Guardrails

- Keep the builder on standard Sails scaffolding and generated clients.
- Do not jump into raw Gear primitives when a Sails path already exists.
- Do not skip the planning docs just because the repo is greenfield.
