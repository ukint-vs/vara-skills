---
name: sails-architecture
description: Use when a builder needs to shape or correct standard Gear/Vara Sails program and service boundaries, state ownership, or message flow. Do not use for pure deployment work, Vara.eth or ethexe targets, or non-Sails programs.
---

# Sails Architecture

## Goal

Turn an approved spec into a Sails-specific architecture artifact before implementation starts.

## Inputs

- `../../assets/architecture-template.md`
- `../../references/vara-domain-overview.md`
- `../../references/sails-cheatsheet.md`

Write the result to `docs/plans/YYYY-MM-DD-<topic>-architecture.md`.

## Specialist Skills To Delegate

- `sails-program-architecture-patterns`
- `gear-messaging-model`

## Review Checklist

- Are `#[program]` and `#[service]` boundaries explicit?
- Is state ownership clear and minimal?
- Are routes, replies, and events stable enough for generated clients?
- Does the design account for async Gear message flow and failure paths?

## Guardrails

- If the spec is missing, stop and create it first.
- Prefer Sails service composition over ad hoc raw Gear layering.
- Keep implementation detail out of the architecture note unless it changes the public contract.
