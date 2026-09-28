#!/usr/bin/env bash
set -euo pipefail
REPO_URL="${1:-https://github.com/Kinrokin/data-center-water-audit.git}"
git init -b main
git add .
git commit -m "Publish data-center water audit"
git remote add origin "$REPO_URL"
git push -u origin main --force-with-lease
