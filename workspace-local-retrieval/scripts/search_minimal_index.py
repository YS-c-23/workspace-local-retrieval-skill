#!/usr/bin/env python3
"""Search the minimal SQLite FTS5 index with simple corpus allowlist enforcement."""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

AGENT_ALLOWLISTS = {
    'main': {'workspace-core', 'workspace-specialist'},
    'specialist-agent': {'workspace-specialist'},
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--db-path', required=True)
    ap.add_argument('--query', required=True)
    ap.add_argument('--agent', default='main')
    ap.add_argument('--corpus')
    ap.add_argument('--limit', type=int, default=5)
    args = ap.parse_args()

    allowed = AGENT_ALLOWLISTS.get(args.agent)
    if allowed is None:
        print(json.dumps({'ok': False, 'error': f'unknown agent: {args.agent}'} , indent=2, ensure_ascii=False))
        raise SystemExit(2)

    if args.corpus and args.corpus not in allowed:
        print(json.dumps({
            'ok': False,
            'error': f'agent {args.agent} is not allowed to access corpus {args.corpus}',
            'agent': args.agent,
            'allowedCorpora': sorted(allowed)
        }, indent=2, ensure_ascii=False))
        raise SystemExit(3)

    db_path = Path(args.db_path).resolve()
    con = sqlite3.connect(db_path)
    sql = 'SELECT path, corpus, snippet(docs_fts, 2, "[", "]", "…", 12) FROM docs_fts WHERE docs_fts MATCH ?'
    params = [args.query]
    if args.corpus:
        sql += ' AND corpus = ?'
        params.append(args.corpus)
    sql += ' LIMIT ?'
    params.append(args.limit)
    rows = list(con.execute(sql, params))
    con.close()

    print(json.dumps({
        'ok': True,
        'query': args.query,
        'agent': args.agent,
        'corpus': args.corpus,
        'hits': [
            {'path': path, 'corpus': corpus, 'snippet': snippet} for path, corpus, snippet in rows
        ],
        'hitCount': len(rows)
    }, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
