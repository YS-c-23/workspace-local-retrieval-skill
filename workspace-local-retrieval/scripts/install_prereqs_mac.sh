#!/usr/bin/env bash
set -euo pipefail

if ! command -v brew >/dev/null 2>&1; then
  echo "Homebrew is required on macOS for this helper. Install Homebrew first:" >&2
  echo "  https://brew.sh/" >&2
  exit 1
fi

need_formula() {
  local formula="$1"
  if brew list --formula "$formula" >/dev/null 2>&1; then
    echo "already installed: $formula"
  else
    echo "installing: $formula"
    brew install "$formula"
  fi
}

need_formula python
need_formula node
need_formula sqlite

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
