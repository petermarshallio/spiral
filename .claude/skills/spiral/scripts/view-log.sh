#!/usr/bin/env bash
# Print the most recent momentum-log entries.
# Usage: view-log.sh [n]
set -euo pipefail

N="${1:-10}"
LOG_DIR="${SPIRAL_LOG_DIR:-$HOME/.spiral}"
LOG_FILE="$LOG_DIR/log.md"

if [ ! -f "$LOG_FILE" ]; then
  echo "No spiral log yet at $LOG_FILE"
  exit 0
fi

tail -n "$N" "$LOG_FILE"
