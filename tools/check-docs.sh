#!/usr/bin/env bash
set -euo pipefail
need=( "docs/learn.md" "docs/prompts.md" "docs/retro.md" "docs/20-ADRs/ADR-0001-initial-approach.md" )
missing=0
for f in "${need[@]}"; do
  if [ ! -e "$f" ]; then
    echo "❌ Missing $f"
    missing=1
  fi
done
exit $missing
