---
name: sails-local-smoke
description: Use when a builder has a standard Gear/Vara Sails app with green gtest coverage and needs typed validation against a local node. Do not use before gtest passes, for remote networks, or for non-Sails programs.
---

# Sails Local Smoke

## Goal

Validate the generated client path against a local node after `gtest` is already green.

## Specialist Skills To Delegate

- `gear-run-local-node`
- `gear-deploy-program`
- `sails-live-node-smoke`
- `gear-query-program-state`

## Sequence

1. Confirm the `docs/plans/...-gtest.md` note shows a green test loop.
2. Start or reuse a local Gear/Vara node with `gear-run-local-node`.
3. Deploy the tested Wasm with `gear-deploy-program`.
4. Exercise the generated client path with `sails-live-node-smoke`.
5. Query resulting state only when that helps close the smoke checklist.

## References

- `../../references/sails-cheatsheet.md`
- `../../references/gtest-cheatsheet.md`

## Guardrails

- Keep this step typed and local.
- Do not replace local smoke with explorer queries or ad hoc CLI poking.
- If `gtest` is red or missing, stop and go back to `../sails-gtest/SKILL.md`.
