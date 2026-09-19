#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALLER="$SOURCE_DIR/scripts/install.py"

if command -v python3 >/dev/null 2>&1; then
  exec python3 "$INSTALLER" "$@"
fi

if command -v python >/dev/null 2>&1; then
  exec python "$INSTALLER" "$@"
fi

if command -v py >/dev/null 2>&1; then
  exec py -3 "$INSTALLER" "$@"
fi

echo "Python 3 is required to install My Agent." >&2
exit 1
