# gear-agent-skills

Provisional product repository for a `vara-skills` Sails-builder pack.

The current repo is the source-of-truth workspace for a portable, markdown-first skill pack targeting Codex, Claude, and OpenClaw. The public website comes later, after the first measured skill set is finalized.

The pack is being narrowed toward standard Gear/Vara Sails app builders:

- starting a new Sails app
- building features in an existing Sails app
- getting architecture, IDL/client wiring, `gtest`, and local-node validation right

The current public catalog is provisional and is expected to change as the eval suite identifies which candidate skills actually create uplift.

## Shared Layers

- `references/` contains agent-facing summaries of core Vara, Sails, gtest, and Vara.eth extension concepts.
- `assets/` contains canonical output shapes for spec, architecture, task-plan, and gtest artifacts.
- `scripts/` contains deterministic helper commands for install, validation, gtest execution, and parser output.
- `docs/plans/` captures approved design and implementation artifacts for the pack.

## Verification

```bash
make verify
```

This runs repository layout, skill-validator, skill-catalog, parser, and install tests for the current product repo surface.

## Installation

```bash
bash scripts/install-codex-skills.sh
```

## Current Direction

- the current repo evolves into `vara-skills`
- a sibling repo `vara-skills-evals` will own benchmark definitions and uplift results
- the top-level router and candidate Sails-builder skills are still being defined
- only measured winning skills should remain in the first public pack
