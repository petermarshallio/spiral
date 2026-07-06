#!/usr/bin/env bash
# Append a momentum-log entry: date | stage | note
# Usage: log-stage.sh "<Learn|Think|Articulate|Build>" "<one-line note>"
set -euo pipefail

STAGE="${1:?Usage: log-stage.sh <Learn|Think|Articulate|Build> <note>}"
NOTE="${2:-}"

LOG_DIR="${SPIRAL_LOG_DIR:-$HOME/.spiral}"
LOG_FILE="$LOG_DIR/log.md"
mkdir -p "$LOG_DIR"

TIMESTAMP="$(date +%Y-%m-%d)"
printf -- "- %s | %s | %s\n" "$TIMESTAMP" "$STAGE" "$NOTE" >> "$LOG_FILE"
echo "Logged: $TIMESTAMP | $STAGE | $NOTE"
