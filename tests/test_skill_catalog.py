#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate-skill.py"
STARTER_SKILLS = {
    "idea-to-spec": [
        "SKILL.md",
    ],
    "gear-architecture-planner": [
        "SKILL.md",
    ],
    "task-decomposer": [
        "SKILL.md",
    ],
    "sails-rust-implementer": [
        "SKILL.md",
    ],
    "gtest-tdd-loop": [
        "SKILL.md",
    ],
}


def require(path: Path) -> None:
    assert path.exists(), f"missing expected path: {path.relative_to(ROOT)}"


def validate(skill_dir: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(skill_dir)],
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr


def main() -> int:
    require(VALIDATOR)

    for skill_name, expected_paths in STARTER_SKILLS.items():
        skill_dir = ROOT / "skills" / skill_name
        require(skill_dir)
        for relative in expected_paths:
            require(skill_dir / relative)
        validate(skill_dir)

    print("starter skills ok")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as err:
        print(err, file=sys.stderr)
        raise SystemExit(1)
