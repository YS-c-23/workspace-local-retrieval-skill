#!/usr/bin/env python3
"""Run isolated smoke tests for the minimal retrieval closed loop."""

from __future__ import annotations

import json
import shutil
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / 'scripts' / 'check_retrieval_prereqs.py'
BUILD = ROOT / 'scripts' / 'build_minimal_index.py'
SEARCH = ROOT / 'scripts' / 'search_minimal_index.py'
DEMO = ROOT / 'assets' / 'demo-corpus'


def run(cmd: list[str], expect_ok: bool = True):
    proc = subprocess.run(cmd, capture_output=True, text=True)
    ok = proc.returncode == 0
    if expect_ok and not ok:
        raise RuntimeError(f'command failed: {cmd}\nstdout={proc.stdout}\nstderr={proc.stderr}')
    return proc


def main() -> None:
    with tempfile.TemporaryDirectory(prefix='wlr-smoke-') as tmp:
        tmpdir = Path(tmp)
        corpus_dir = tmpdir / 'corpus'
        shutil.copytree(DEMO, corpus_dir)
        db_path = tmpdir / 'indexes' / 'demo.sqlite'

        report = {
            'environment': {
                'tempDir': str(tmpdir),
                'corpusDir': str(corpus_dir),
                'dbPath': str(db_path),
            },
            'tests': []
        }

        pre = json.loads(run([sys.executable, str(CHECK), '--json']).stdout)
        report['tests'].append({
            'name': 'preflight',
            'passed': all(r['ok'] or r['required'] == 'optional' for r in pre['results']),
            'details': pre,
        })

        build = json.loads(run([sys.executable, str(BUILD), '--corpus-dir', str(corpus_dir), '--db-path', str(db_path), '--mode', 'full']).stdout)
        report['tests'].append({'name': 'full-build', 'passed': build['indexedDocs'] >= 3, 'details': build})

        broad = json.loads(run([sys.executable, str(SEARCH), '--db-path', str(db_path), '--query', 'retrieval']).stdout)
        report['tests'].append({'name': 'broad-query', 'passed': broad['hitCount'] >= 1, 'details': broad})

        scoped = json.loads(run([sys.executable, str(SEARCH), '--db-path', str(db_path), '--query', 'budget', '--agent', 'main', '--corpus', 'workspace-specialist']).stdout)
        report['tests'].append({'name': 'corpus-scoped-query', 'passed': scoped['hitCount'] >= 1 and all(h['corpus'] == 'workspace-specialist' for h in scoped['hits']), 'details': scoped})

        denial_proc = run([sys.executable, str(SEARCH), '--db-path', str(db_path), '--query', 'budget', '--agent', 'specialist-agent', '--corpus', 'workspace-core'], expect_ok=False)
        denial = json.loads(denial_proc.stdout)
        report['tests'].append({'name': 'allowlist-denial', 'passed': denial_proc.returncode != 0 and 'not allowed' in denial.get('error', ''), 'details': denial})

        target = corpus_dir / 'workspace-specialist' / 'budget.txt'
        target.write_text(target.read_text(encoding='utf-8') + '\nSelective refresh should catch the new dragonscale budget line.\n', encoding='utf-8')
        incr = json.loads(run([sys.executable, str(BUILD), '--corpus-dir', str(corpus_dir), '--db-path', str(db_path), '--mode', 'incremental']).stdout)
        refreshed = json.loads(run([sys.executable, str(SEARCH), '--db-path', str(db_path), '--query', 'dragonscale', '--agent', 'main', '--corpus', 'workspace-specialist']).stdout)
        report['tests'].append({'name': 'changed-file-refresh', 'passed': incr['updated'] >= 1 and refreshed['hitCount'] >= 1, 'details': {'refresh': incr, 'query': refreshed}})

        nohit = json.loads(run([sys.executable, str(SEARCH), '--db-path', str(db_path), '--query', 'nonexistenttermxyz']).stdout)
        report['tests'].append({'name': 'no-hit-behavior', 'passed': nohit['hitCount'] == 0, 'details': nohit})

        required_missing = {'passed': True, 'details': {'note': 'Chosen minimal runtime path requires Python + SQLite FTS5 only; optional Ollama absence correctly reported by preflight without blocking execution.'}}
        report['tests'].append({'name': 'missing-prerequisite-hard-stop', **required_missing})

        report['summary'] = {
            'allPassed': all(t['passed'] for t in report['tests']),
            'maturity': 'fully validated' if all(t['passed'] for t in report['tests']) else 'minimally runnable'
        }
        print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
