---
name: sails-idl-client
description: Use when a builder needs to wire or repair the standard Gear/Vara Sails IDL and generated client pipeline in app, client, or test crates. Do not use for raw payload-only testing, Vara.eth or ethexe codegen, or non-Sails repositories.
---

# Sails IDL Client

## Goal

Keep Sails builders on the typed pipeline for IDL generation, Rust client generation, and integration wiring.

## Inputs

- `../../references/sails-cheatsheet.md`
- `../../assets/task-plan-template.md`

## Specialist Skill To Delegate

- `sails-idl-and-client-pipeline`

## Route Here When

- Check `build.rs` or generation wiring when it no longer generates the expected artifacts
- the client crate drifted from program changes
- Check output paths and artifact freshness before deeper debugging
- tests are building raw payloads instead of using generated clients
- local smoke needs a typed client path

## Guardrails

- Keep generated artifacts aligned with the program contract before deeper debugging.
- Prefer generated client flows in tests and smoke runs when the workspace supports them.
- Do not treat missing codegen as a reason to bypass the Sails pipeline.
