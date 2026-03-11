# AGENTS.md

## Purpose
This repository is the provisional product repo for a portable Vara Sails-builder skill pack. It owns builder-facing skill content, shared references, validation scripts, and installation surfaces for Codex first, with Claude and OpenClaw packaging added in-repo.

## Working Rules
- Use `writing-skills` before creating or editing any skill in `skills/`.
- Apply TDD to repository behavior: add or update tests before changing scripts, validation logic, or published skill contracts.
- Keep each skill directory flat and include `SKILL.md`, `assets/`, `references/`, and `scripts/`.
- Prefer shared repository references in `references/` and shared templates in `assets/`; skill files may reference them via relative paths.
- Do not embed machine-specific absolute paths in published docs or skills unless the file is an explicit local validation target.
- Treat the current public skill catalog as provisional until the sibling eval repo proves which candidate skills create real uplift.
- Keep the first builder path focused on standard Gear/Vara Sails, not Vara.eth-first workflows.

## Verification
- Run `make verify` before claiming the repo is ready.
- Keep installation working through `scripts/install-codex-skills.sh`.
- Keep repository docs aligned with the product split: this repo owns skills and packaging; the sibling eval repo owns measurement.
