# Vara Sails Builder Pack Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a measured, portable Sails-builder skill pack for Codex, Claude, and OpenClaw, plus a separate eval repo that determines which first-wave skills actually improve Gear/Vara Sails builder behavior.

**Architecture:** Treat the current repo as the `vara-skills` product repo and create a sibling `vara-skills-evals` repo for measurement. Start with a provisional router plus candidate Sails-builder skills, then use mixed factual and builder-task A/B evals to decide what remains in the first public pack.

**Tech Stack:** Markdown `SKILL.md`, Bash, Python 3, YAML eval definitions, Claude plugin metadata, Codex install scripts, OpenClaw wrapper skills, local Gear/Vara/Sails reference repos.

---

### Task 1: Reframe the current repo as the product repo

**Files:**
- Modify: `<repo-root>/README.md`
- Modify: `<repo-root>/AGENTS.md`
- Modify: `<repo-root>/tests/test_repo_layout.py`
- Modify: `<repo-root>/tests/test_skill_catalog.py`
- Create: `<repo-root>/docs/plans/2026-03-11-vara-sails-builder-pack-design.md`
- Create: `<repo-root>/docs/plans/2026-03-11-vara-sails-builder-pack.md`

**Step 1: Write the failing repo assertions**

Extend `tests/test_repo_layout.py` and `tests/test_skill_catalog.py` so they fail until the repo exposes the new public shape:

- top-level router `ship-sails-app`
- candidate Sails-builder skills
- Claude and OpenClaw packaging files
- no claim that the current public catalog is finalized

**Step 2: Run tests to verify they fail**

Run:

```bash
python3 <repo-root>/tests/test_repo_layout.py
python3 <repo-root>/tests/test_skill_catalog.py
```

Expected:

- `FAIL` because the router skill and packaging files do not exist yet.

**Step 3: Write the minimal repo framing changes**

Update `README.md` and `AGENTS.md` to describe the repo as a provisional `vara-skills` product repo for a Sails-builder pack, not as a finalized generic Gear starter catalog.

**Step 4: Run repo tests again**

Run:

```bash
make -C <repo-root> test-layout
```

Expected:

- the test may still fail until later tasks add the missing skill and packaging files.

**Step 5: Commit**

```bash
git -C <repo-root> add README.md AGENTS.md tests/test_repo_layout.py tests/test_skill_catalog.py docs/plans/2026-03-11-vara-sails-builder-pack-design.md docs/plans/2026-03-11-vara-sails-builder-pack.md
git -C <repo-root> commit -m "docs: reframe repo as vara-skills product repo"
```

### Task 2: Bootstrap the eval repo

**Files:**
- Create: `<vara-skills-evals-root>/README.md`
- Create: `<vara-skills-evals-root>/PLAN.md`
- Create: `<vara-skills-evals-root>/runner/run.sh`
- Create: `<vara-skills-evals-root>/runner/judge.md`
- Create: `<vara-skills-evals-root>/results/.gitkeep`
- Create: `<vara-skills-evals-root>/tests/test_repo_layout.py`
- Create: `<vara-skills-evals-root>/tests/test_runner_smoke.py`

**Step 1: Write the failing eval-repo tests**

Add a layout test for the repo skeleton and a smoke test for `runner/run.sh --help`.

**Step 2: Run tests to verify they fail**

Run:

```bash
python3 <vara-skills-evals-root>/tests/test_repo_layout.py
python3 <vara-skills-evals-root>/tests/test_runner_smoke.py
```

Expected:

- `FAIL` because the repo and runner do not exist yet.

**Step 3: Create the minimal eval repo**

Add the README, plan, runner scaffold, judge prompt, results directory, and test files.

**Step 4: Run tests to verify they pass**

Run:

```bash
python3 <vara-skills-evals-root>/tests/test_repo_layout.py
python3 <vara-skills-evals-root>/tests/test_runner_smoke.py
```

Expected:

- both tests `PASS`

**Step 5: Commit**

```bash
git -C <vara-skills-evals-root> add .
git -C <vara-skills-evals-root> commit -m "chore: bootstrap vara-skills-evals"
```

### Task 3: Define the first benchmark sets

**Files:**
- Create: `<vara-skills-evals-root>/evals/ship-sails-app.yaml`
- Create: `<vara-skills-evals-root>/evals/sails-new-app.yaml`
- Create: `<vara-skills-evals-root>/evals/sails-feature-workflow.yaml`
- Create: `<vara-skills-evals-root>/evals/sails-architecture.yaml`
- Create: `<vara-skills-evals-root>/evals/sails-idl-client.yaml`
- Create: `<vara-skills-evals-root>/evals/sails-gtest.yaml`
- Create: `<vara-skills-evals-root>/evals/sails-local-smoke.yaml`
- Create: `<vara-skills-evals-root>/tests/test_eval_catalog.py`

**Step 1: Write the failing eval-catalog test**

Require every candidate skill to have:

- at least one factual prompt
- at least two builder-task prompts
- `expected_facts`
- `fail_if`

**Step 2: Run the test to verify it fails**

Run:

```bash
python3 <vara-skills-evals-root>/tests/test_eval_catalog.py
```

Expected:

- `FAIL` because the YAML files do not exist yet.

**Step 3: Add the initial eval definitions**

Base prompts on real Sails-builder tasks, using the current local repos as ground truth:

- `<sails-root>`
- `<gear-root>`
- `<vara-wiki-root>`

Keep the suite mixed, but builder-task-heavy.

**Step 4: Run the test to verify it passes**

Run:

```bash
python3 <vara-skills-evals-root>/tests/test_eval_catalog.py
```

Expected:

- `PASS`

**Step 5: Commit**

```bash
git -C <vara-skills-evals-root> add evals tests/test_eval_catalog.py
git -C <vara-skills-evals-root> commit -m "test: add first Sails builder eval definitions"
```

### Task 4: Replace the public skill catalog with a provisional Sails-builder pack

**Files:**
- Create: `<repo-root>/SKILL.md`
- Create: `<repo-root>/skills/ship-sails-app/SKILL.md`
- Create: `<repo-root>/skills/sails-new-app/SKILL.md`
- Create: `<repo-root>/skills/sails-feature-workflow/SKILL.md`
- Create: `<repo-root>/skills/sails-architecture/SKILL.md`
- Create: `<repo-root>/skills/sails-idl-client/SKILL.md`
- Create: `<repo-root>/skills/sails-gtest/SKILL.md`
- Create: `<repo-root>/skills/sails-local-smoke/SKILL.md`
- Modify: `<repo-root>/scripts/install-codex-skills.sh`
- Modify: `<repo-root>/tests/test_skill_catalog.py`

**Step 1: Write the failing catalog assertions**

Make the catalog test fail until the new public router and candidate skills exist.

**Step 2: Run the catalog test to verify it fails**

Run:

```bash
python3 <repo-root>/tests/test_skill_catalog.py
```

Expected:

- `FAIL` because the new skill set does not exist yet.

**Step 3: Add the provisional public skills**

Write lean, portable `SKILL.md` files that:

- route by builder task and stage;
- point to shared references and templates;
- explicitly state they are candidate first-wave skills;
- remain standard Gear/Vara Sails only.

Do not yet optimize for completeness; optimize for clear routing and testability.

**Step 4: Run catalog and validator tests**

Run:

```bash
python3 <repo-root>/tests/test_skill_validation.py
python3 <repo-root>/tests/test_skill_catalog.py
```

Expected:

- both tests `PASS`

**Step 5: Commit**

```bash
git -C <repo-root> add SKILL.md skills scripts/install-codex-skills.sh tests/test_skill_catalog.py
git -C <repo-root> commit -m "feat: add provisional Sails builder skill pack"
```

### Task 5: Add Claude and OpenClaw packaging

**Files:**
- Create: `<repo-root>/.claude-plugin/plugin.json`
- Create: `<repo-root>/.claude-plugin/marketplace.json`
- Create: `<repo-root>/openclaw-skill/SKILL.md`
- Create: `<repo-root>/openclaw-skill/README.md`
- Create: `<repo-root>/tests/test_packaging_metadata.py`

**Step 1: Write the failing packaging test**

Require valid Claude plugin metadata and an OpenClaw wrapper that points users at the top-level router skill.

**Step 2: Run the test to verify it fails**

Run:

```bash
python3 <repo-root>/tests/test_packaging_metadata.py
```

Expected:

- `FAIL` because the packaging files do not exist yet.

**Step 3: Add the packaging files**

Use the `ethskills` structure as the reference shape, but point it at the Sails-builder pack and current repo metadata.

**Step 4: Run packaging and repo verification**

Run:

```bash
python3 <repo-root>/tests/test_packaging_metadata.py
make -C <repo-root> verify
```

Expected:

- packaging test `PASS`
- full repo verify `PASS`

**Step 5: Commit**

```bash
git -C <repo-root> add .claude-plugin openclaw-skill tests/test_packaging_metadata.py
git -C <repo-root> commit -m "feat: add Claude and OpenClaw packaging"
```

### Task 6: Run the first A/B benchmark and cut the pack to measured winners

**Files:**
- Modify: `<vara-skills-evals-root>/runner/run.sh`
- Create: `<vara-skills-evals-root>/results/YYYY-MM-DD-initial-sails-builder-report.md`
- Modify: `<repo-root>/README.md`
- Modify: `<repo-root>/tests/test_skill_catalog.py`

**Step 1: Add the smallest working A/B path**

Make `runner/run.sh` able to:

- load one eval file;
- run baseline and skill-loaded prompts;
- emit machine-readable results;
- write a markdown summary.

**Step 2: Run the runner smoke test**

Run:

```bash
bash <vara-skills-evals-root>/runner/run.sh --help
```

Expected:

- help output prints usage and exits `0`

**Step 3: Run the first benchmark slice**

Run the suite against at least two target model families, using the candidate pack.

**Step 4: Freeze the winning public set**

Update `README.md` and `tests/test_skill_catalog.py` so the public catalog matches the measured winners only. Remove, merge, or mark provisional any candidate skill that does not show clear uplift.

**Step 5: Verify and commit**

Run:

```bash
make -C <repo-root> verify
python3 <vara-skills-evals-root>/tests/test_repo_layout.py
python3 <vara-skills-evals-root>/tests/test_eval_catalog.py
```

Expected:

- all checks `PASS`

Commit:

```bash
git -C <vara-skills-evals-root> add runner results tests
git -C <vara-skills-evals-root> commit -m "results: first Sails builder uplift benchmark"
git -C <repo-root> add README.md tests/test_skill_catalog.py
git -C <repo-root> commit -m "docs: freeze first measured Sails skill catalog"
```

## Assumptions

- `<repo-root>` is the product repo even if it is later renamed to `vara-skills`.
- `<vara-skills-evals-root>` will be created as a sibling repo for measurement.
- The first public pack is allowed to start as a candidate catalog and shrink based on benchmark evidence.
- Standard Gear/Vara Sails is the only first-class builder path in v1.
- Website publication is explicitly deferred until after the benchmark-driven first pack is finalized.
