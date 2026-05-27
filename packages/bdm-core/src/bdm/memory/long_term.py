from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence

from .event import MemoryEvent, MemoryEventType

_DEFAULT_PATH = Path.home() / ".bdm" / "memory.db"

_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS memory_events (
    id          TEXT PRIMARY KEY,
    content     TEXT NOT NULL,
    event_type  TEXT NOT NULL,
    tags        TEXT NOT NULL DEFAULT '[]',
    metadata    TEXT NOT NULL DEFAULT '{}',
    salience    REAL NOT NULL DEFAULT 1.0,
    created_at  TEXT NOT NULL
)
"""


def _row_to_event(row: sqlite3.Row) -> MemoryEvent:
    return MemoryEvent(
        id=row["id"],
        content=row["content"],
        event_type=MemoryEventType(row["event_type"]),
        tags=json.loads(row["tags"]),
        metadata=json.loads(row["metadata"]),
        salience=row["salience"],
        created_at=datetime.fromisoformat(row["created_at"]),
    )


class LongTermStore:
    """SQLite-backed persistent store for memory events.

    Events survive process restarts. DB file is created automatically
    on first use. Default location: ~/.bdm/memory.db
    """

    def __init__(self, path: str | Path = _DEFAULT_PATH) -> None:
        self._path = Path(path)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self._path), check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute(_CREATE_TABLE)
        self._conn.commit()

    def add(self, event: MemoryEvent) -> None:
        self._conn.execute(
            """
            INSERT OR REPLACE INTO memory_events
                (id, content, event_type, tags, metadata, salience, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event.id,
                event.content,
                event.event_type.value,
                json.dumps(event.tags),
                json.dumps(event.metadata),
                event.salience,
                event.created_at.isoformat(),
            ),
        )
        self._conn.commit()

    def get(self, event_id: str) -> MemoryEvent | None:
        row = self._conn.execute(
            "SELECT * FROM memory_events WHERE id = ?", (event_id,)
        ).fetchone()
        return _row_to_event(row) if row else None

    def query(
        self,
        *,
        limit: int = 10,
        event_type: MemoryEventType | None = None,
        tags: list[str] | None = None,
    ) -> Sequence[MemoryEvent]:
        sql = "SELECT * FROM memory_events"
        params: list = []

        if event_type is not None:
            sql += " WHERE event_type = ?"
            params.append(event_type.value)

        sql += " ORDER BY created_at DESC LIMIT ?"
        params.append(limit * 10 if tags else limit)

        rows = self._conn.execute(sql, params).fetchall()
        results = [_row_to_event(r) for r in rows]

        if tags:
            tag_set = set(tags)
            results = [e for e in results if tag_set.intersection(e.tags)]
            results = results[:limit]

        return results

    def delete(self, event_id: str) -> bool:
        cursor = self._conn.execute(
            "DELETE FROM memory_events WHERE id = ?", (event_id,)
        )
        self._conn.commit()
        return cursor.rowcount > 0

    def clear(self) -> None:
        self._conn.execute("DELETE FROM memory_events")
        self._conn.commit()

    def __len__(self) -> int:
        row = self._conn.execute("SELECT COUNT(*) FROM memory_events").fetchone()
        return row[0]

    def close(self) -> None:
        self._conn.close()

    def __enter__(self) -> LongTermStore:
        return self

    def __exit__(self, *_) -> None:
        self.close()
