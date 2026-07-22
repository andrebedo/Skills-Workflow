#!/usr/bin/env python3
"""Create missing Puppeteer workflow documents in a project."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize Puppeteer project documents.")
    parser.add_argument("--project-root", required=True, type=Path)
    args = parser.parse_args()

    project_root = args.project_root.expanduser().resolve()
    if not project_root.is_dir():
        raise SystemExit(f"Project root is not a directory: {project_root}")

    templates = Path(__file__).resolve().parent.parent / "assets" / "docs"
    if not templates.is_dir():
        raise SystemExit(f"Template directory is missing: {templates}")

    destination = project_root / "docs"
    destination.mkdir(parents=True, exist_ok=True)
    created: list[str] = []
    preserved: list[str] = []

    for template in sorted(templates.glob("*.md")):
        target = destination / template.name
        relative = target.relative_to(project_root).as_posix()
        if target.exists():
            preserved.append(relative)
        else:
            shutil.copyfile(template, target)
            created.append(relative)

    print("Created:")
    print("\n".join(f"  {path}" for path in created) if created else "  none")
    print("Preserved:")
    print("\n".join(f"  {path}" for path in preserved) if preserved else "  none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())