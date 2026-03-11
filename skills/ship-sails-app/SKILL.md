---
name: ship-sails-app
description: Use when a builder needs the top-level router for a standard Gear/Vara Sails app workflow from spec through gtest and local smoke. Do not use for Vara.eth or ethexe work, raw gstd-only programs, or non-Sails tasks.
---

# Ship Sails App

## Role

Use this as the first stop for the provisional Sails-builder pack. Route the builder by repo state and next required artifact, then hand off to the narrower skill.

## Route By Situation

- No repo or greenfield workspace request: `../sails-new-app/SKILL.md`
- Existing Sails repo with feature or behavior change: `../sails-feature-workflow/SKILL.md`
- Confusion about `#[program]`, `#[service]`, state, or message flow: `../sails-architecture/SKILL.md`
- Broken `build.rs`, missing IDL, or generated client drift: `../sails-idl-client/SKILL.md`
- Need to author or debug `gtest`: `../sails-gtest/SKILL.md`
- `gtest` is green and the next step is a typed live-node smoke run: `../sails-local-smoke/SKILL.md`

## Required Artifact Chain

Keep the builder on this document chain inside `docs/plans/`:

`YYYY-MM-DD-<topic>-spec.md -> ...-architecture.md -> ...-tasks.md -> ...-gtest.md`

Use shared templates from:

- `../../assets/spec-template.md`
- `../../assets/architecture-template.md`
- `../../assets/task-plan-template.md`
- `../../assets/gtest-report-template.md`

## Shared References

- `../../references/vara-domain-overview.md`
- `../../references/sails-cheatsheet.md`
- `../../references/gtest-cheatsheet.md`

## Routing Reminder

- Route to the new-app path when the builder is starting from scratch.
- Mention later architecture, `gtest`, and local-node validation so the builder sees the full Sails path instead of just the first step.

## Guardrails

- Treat this as a candidate first-wave catalog, not a frozen public taxonomy.
- Keep the flow standard Gear/Vara Sails only.
- If the task jumps straight to deployment or a live network without green `gtest`, redirect to testing first.
