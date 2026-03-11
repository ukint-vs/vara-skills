---
name: sails-feature-workflow
description: Use when a builder is changing behavior inside an existing standard Gear/Vara Sails app and needs the correct stage-by-stage workflow. Do not use for greenfield scaffolding, Vara.eth or ethexe paths, or non-Sails repositories.
---

# Sails Feature Workflow

## Goal

Keep feature work inside an existing Sails repo on an explicit sequence instead of skipping straight to code edits.

## Required Sequence

1. Clarify the feature in `docs/plans/YYYY-MM-DD-<topic>-spec.md` with `idea-to-spec` and `../../assets/spec-template.md`.
2. Plan architecture or public interface in `...-architecture.md` with `../sails-architecture/SKILL.md` and `../../assets/architecture-template.md`.
3. Break the work into tasks in `...-tasks.md` with `task-decomposer` and `../../assets/task-plan-template.md`.
4. Implement the Rust changes through `sails-rust-implementer`.
5. Run `gtest` through `../sails-gtest/SKILL.md`.
6. Run smoke validation only after green `gtest`, using `../sails-local-smoke/SKILL.md`.

## References

- `../../references/vara-domain-overview.md`
- `../../references/sails-cheatsheet.md`
- `../../references/gtest-cheatsheet.md`

## Guardrails

- Do not skip the document chain for “small” features.
- Do not claim completion before `gtest` is green and documented.
- Do not treat local-node smoke as a substitute for `gtest`.
