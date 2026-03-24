#!/usr/bin/env bash
set -euo pipefail

if command -v apt-get >/dev/null 2>&1; then
  sudo apt-get update
  sudo apt-get install -y python3 python3-venv python3-pip nodejs npm sqlite3
elif command -v dnf >/dev/null 2>&1; then
  sudo dnf install -y python3 python3-pip nodejs npm sqlite sqlite-devel
elif command -v pacman >/dev/null 2>&1; then
  sudo pacman -Sy --needed python nodejs npm sqlite
else
  echo "Unsupported Linux package manager. Install Python 3.10+, Node 20+, and sqlite3 manually." >&2
  exit 1
fi

cat <<'EOF'

Prerequisite helper finished.

Next steps:
  1. Re-run: python3 scripts/check_retrieval_prereqs.py
  2. Bootstrap config:
       python3 scripts/bootstrap_workspace_retrieval.py --dest ./retrieval --workspace-root "$(pwd)"
  3. Run the minimal demo:
       bash scripts/setup_demo.sh

Optional:
  - Install Ollama if you want a local embedding backend for semantic retrieval.
EOF
