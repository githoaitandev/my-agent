#!/usr/bin/env python3
"""Conservative shell guard for project-local Codex hooks."""

from __future__ import annotations

import json
import re
import sys


BLOCK_PATTERNS = [
    r"\brm\s+-rf\s+/",
    r"\bgit\s+reset\s+--hard\b",
    r"\bgit\s+checkout\s+--\s+",
    r"\bsudo\s+",
    r"\bchmod\s+-R\s+777\b",
]


def deny(reason: str) -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }
        )
    )


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    tool_input = payload.get("tool_input") or {}
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    if not isinstance(command, str):
        return 0

    for pattern in BLOCK_PATTERNS:
        if re.search(pattern, command):
            deny(f"My Agent blocked a risky shell command matching `{pattern}`.")
            return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

