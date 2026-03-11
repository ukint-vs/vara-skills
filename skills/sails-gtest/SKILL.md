---
name: sails-gtest
description: Use when a builder needs the standard Gear/Vara Sails gtest loop for feature verification, debugging, or regression coverage. Do not use for live-network-only validation, deployment-first workflows, or non-Sails programs.
---

# Sails Gtest

## Goal

Run the Sails-first test loop with generated clients and explicit `gtest` evidence before any live-node smoke step.

## Inputs

- `../../assets/gtest-report-template.md`
- `../../references/gtest-cheatsheet.md`
- `../../references/sails-cheatsheet.md`

Write the result to `docs/plans/YYYY-MM-DD-<topic>-gtest.md`.

## Specialist Skills To Delegate

- `gtest-core-workflows`
- `gear-test-sails-program`
- `gear-gas-and-value-accounting`

## Expected Loop

1. Confirm the implementation target is ready for verification.
2. Use generated clients or `GtestEnv` instead of hand-built payloads where the workspace supports them.
3. Advance blocks explicitly when replies or deferred effects depend on progression.
4. Assert behavior, replies, or events in the test result, not just compilation.
5. Record failure mode, fix, and passing command output in the gtest note.
6. Route to `../sails-local-smoke/SKILL.md` only after the suite is green.

## Guardrails

- Do not use green `cargo test` output without Sails-appropriate assertions as proof.
- Do not start local-node smoke while `gtest` is still red.
- Do not skip gas or value reasoning when tests depend on it.
