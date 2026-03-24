#!/usr/bin/env python3
"""Build a minimal SQLite FTS5 index for the sanitized demo corpus."""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from pathlib import Path

ALLOWED_EXTS = {'.md', '.txt'}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def iter_docs(corpus_dir: Path):
    for path in sorted(corpus_dir.rglob('*')):
        if path.is_file() and path.suffix.lower() in ALLOWED_EXTS:
            rel = path.relative_to(corpus_dir).as_posix()
            corpus = rel.split('/', 1)[0] if '/' in rel else 'default'
            text = path.read_text(encoding='utf-8')
            yield corpus, rel, text


def ensure_schema(con: sqlite3.Connection) -> None:
    con.executescript(
        '''
        CREATE TABLE IF NOT EXISTS docs (
          path TEXT PRIMARY KEY,
          corpus TEXT NOT NULL,
          sha256 TEXT NOT NULL,
          content TEXT NOT NULL
        );
        CREATE VIRTUAL TABLE IF NOT EXISTS docs_fts USING fts5(
          path UNINDEXED,
          corpus UNINDEXED,
          content
        );
        '''
    )


def full_build(con: sqlite3.Connection, corpus_dir: Path) -> dict:
    con.execute('DELETE FROM docs')
    con.execute('DELETE FROM docs_fts')
    count = 0
    for corpus, rel, text in iter_docs(corpus_dir):
        digest = sha256_text(text)
        con.execute('INSERT INTO docs(path, corpus, sha256, content) VALUES (?, ?, ?, ?)', (rel, corpus, digest, text))
        con.execute('INSERT INTO docs_fts(path, corpus, content) VALUES (?, ?, ?)', (rel, corpus, text))
        count += 1
    con.commit()
    return {'mode': 'full', 'indexedDocs': count}


def incremental_refresh(con: sqlite3.Connection, corpus_dir: Path) -> dict:
    existing = {row[0]: (row[1], row[2]) for row in con.execute('SELECT path, corpus, sha256 FROM docs')}
    current = {}
    updated = 0
    inserted = 0
    for corpus, rel, text in iter_docs(corpus_dir):
        digest = sha256_text(text)
        current[rel] = (corpus, digest, text)
        if rel not in existing:
            con.execute('INSERT INTO docs(path, corpus, sha256, content) VALUES (?, ?, ?, ?)', (rel, corpus, digest, text))
            con.execute('INSERT INTO docs_fts(path, corpus, content) VALUES (?, ?, ?)', (rel, corpus, text))
            inserted += 1
        elif existing[rel][1] != digest:
            con.execute('UPDATE docs SET corpus=?, sha256=?, content=? WHERE path=?', (corpus, digest, text, rel))
            con.execute('DELETE FROM docs_fts WHERE path=?', (rel,))
            con.execute('INSERT INTO docs_fts(path, corpus, content) VALUES (?, ?, ?)', (rel, corpus, text))
            updated += 1
    removed = 0
    for rel in set(existing) - set(current):
        con.execute('DELETE FROM docs WHERE path=?', (rel,))
        con.execute('DELETE FROM docs_fts WHERE path=?', (rel,))
        removed += 1
    con.commit()
    return {'mode': 'incremental', 'inserted': inserted, 'updated': updated, 'removed': removed}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--corpus-dir', required=True)
    ap.add_argument('--db-path', required=True)
    ap.add_argument('--mode', choices=['full', 'incremental'], default='full')
    args = ap.parse_args()

    corpus_dir = Path(args.corpus_dir).resolve()
    db_path = Path(args.db_path).resolve()
    db_path.parent.mkdir(parents=True, exist_ok=True)

    con = sqlite3.connect(db_path)
    ensure_schema(con)
    if args.mode == 'full':
        result = full_build(con, corpus_dir)
    else:
        result = incremental_refresh(con, corpus_dir)
    result['dbPath'] = str(db_path)
    result['corpusDir'] = str(corpus_dir)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    con.close()


if __name__ == '__main__':
    main()
