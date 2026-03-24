#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DB_PATH="${1:-$ROOT_DIR/.demo/demo.sqlite}"
CORPUS_DIR="$ROOT_DIR/assets/demo-corpus"

mkdir -p "$(dirname "$DB_PATH")"

echo "[1/4] Checking prerequisites"
python3 "$ROOT_DIR/scripts/check_retrieval_prereqs.py"

echo "[2/4] Building minimal demo index"
python3 "$ROOT_DIR/scripts/build_minimal_index.py" \
  --corpus-dir "$CORPUS_DIR" \
  --db-path "$DB_PATH" \
  --mode full

echo "[3/4] Running sample search"
python3 "$ROOT_DIR/scripts/search_minimal_index.py" \
  --db-path "$DB_PATH" \
  --query retrieval

echo "[4/4] Running smoke tests"
python3 "$ROOT_DIR/scripts/run_minimal_smoke_tests.py"

cat <<EOF

Demo setup complete.
Demo DB: $DB_PATH

Try additional queries:
  python3 "$ROOT_DIR/scripts/search_minimal_index.py" --db-path "$DB_PATH" --query budget --agent main --corpus workspace-specialist
  python3 "$ROOT_DIR/scripts/search_minimal_index.py" --db-path "$DB_PATH" --query retrieval --agent specialist-agent --corpus workspace-specialist
EOF
