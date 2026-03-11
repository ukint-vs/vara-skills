#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
import re
import sys


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
NEGATIVE_TRIGGER_PATTERNS = ("Do not use", "Don't use")
ALLOWED_FRONTMATTER_FIELDS = {"name", "description"}


def fail(message: str) -> int:
    print(message, file=sys.stderr)
    return 1


def parse_frontmatter(skill_md: Path) -> tuple[str, str]:
    lines = skill_md.read_text(encoding="utf-8").splitlines()
    if len(lines) > 500:
        raise ValueError(f"SKILL.md exceeds 500 lines: {len(lines)}")
    if len(lines) < 4 or lines[0] != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")
    try:
        closing = lines[1:].index("---") + 1
    except ValueError as err:
        raise ValueError("SKILL.md frontmatter is not closed") from err
    fields: dict[str, str] = {}
    for line in lines[1:closing]:
        if ":" not in line:
            raise ValueError(f"malformed frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    extra_fields = sorted(set(fields) - ALLOWED_FRONTMATTER_FIELDS)
    if extra_fields:
        raise ValueError(
            "frontmatter must contain only name and description; "
            f"found extra fields: {', '.join(extra_fields)}"
        )
    name = fields.get("name")
    description = fields.get("description")
    if not name or not description:
        raise ValueError("frontmatter must contain name and description")
    if not NAME_RE.match(name):
        raise ValueError("name must use lowercase letters, numbers, and single hyphens only")
    if len(name) > 64:
        raise ValueError("name must be at most 64 characters")
    if len(name) + len(description) > 1024:
        raise ValueError("frontmatter exceeds 1024 combined characters")
    if not description.startswith("Use when"):
        raise ValueError("description must start with 'Use when'")
    if not any(pattern in description for pattern in NEGATIVE_TRIGGER_PATTERNS):
        raise ValueError("description must contain a negative trigger such as 'Do not use'")
    return name, description


def validate_support_directory(path: Path, dirname: str) -> None:
    support_dir = path / dirname
    if not support_dir.is_dir():
        raise ValueError(f"missing required directory: {dirname}")
    for child in support_dir.iterdir():
        if child.name.startswith("."):
            continue
        if child.is_dir():
            raise ValueError(
                f"{dirname} must stay one level deep; found nested directory: {child.relative_to(path)}"
            )


def validate(path: Path) -> None:
    if not path.is_dir():
        raise ValueError(f"skill path is not a directory: {path}")
    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        raise ValueError(f"missing SKILL.md in {path}")
    name, _ = parse_frontmatter(skill_md)
    if path.name != name:
        raise ValueError(f"directory name '{path.name}' must match skill name '{name}'")
    for dirname in ("scripts", "references", "assets"):
        validate_support_directory(path, dirname)


def main() -> int:
    if len(sys.argv) != 2:
        return fail("usage: validate-skill.py <skill-dir>")
    try:
        validate(Path(sys.argv[1]).resolve())
    except ValueError as err:
        return fail(str(err))
    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
