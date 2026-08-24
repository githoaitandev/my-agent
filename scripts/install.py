#!/usr/bin/env python3
"""Install this reusable Codex agent profile into a target project."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SOURCE_ROOT = Path(__file__).resolve().parents[1]
INSTALL_PATHS = [
    "AGENTS.md",
    ".agents",
    ".codex",
]


def copy_path(src: Path, dst: Path, force: bool, created: list[str], skipped: list[str]) -> None:
    if not src.exists():
        return

    if src.is_dir():
        for child in src.rglob("*"):
            if child.is_dir():
                continue
            rel = child.relative_to(SOURCE_ROOT)
            copy_path(child, dst.parent / rel, force, created, skipped)
        return

    if dst.exists() and not force:
        skipped.append(str(dst))
        return

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    created.append(str(dst))


def resolve_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install My Agent into a project.")
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target project directory. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing target files.",
    )
    return parser.parse_args()


def main() -> int:
    args = resolve_args()
    target = Path(args.target).expanduser().resolve()

    if not target.exists() or not target.is_dir():
        raise SystemExit(f"Target project directory does not exist: {target}")

    created: list[str] = []
    skipped: list[str] = []

    for rel in INSTALL_PATHS:
        copy_path(SOURCE_ROOT / rel, target / rel, args.force, created, skipped)

    print(f"My Agent installed into: {target}")
    if created:
        print("Created or updated:")
        for path in created:
            print(f"- {path}")
    if skipped:
        print("Skipped existing files:")
        for path in skipped:
            print(f"- {path}")
    if not created and not skipped:
        print("No installable files found.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

