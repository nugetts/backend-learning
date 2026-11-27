import sqlite3
from datetime import date
from pathlib import Path

from tasks_app.models import Task

DB_FILE = Path("tasks.db")


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def row_to_task(row: sqlite3.Row) -> Task:
    return Task(
        id=row["id"],
        title=row["title"],
        done=bool(row["done"]),
        created=date.fromisoformat(row["created"]),
    )


def init_db() -> None:
    conn = connect()
    conn.execute(
        "CREATE TABLE IF NOT EXISTS tasks ("
        "id INTEGER PRIMARY KEY, "
        "title TEXT NOT NULL, "
        "done INTEGER NOT NULL DEFAULT 0, "
        "created TEXT NOT NULL)"
    )
    conn.commit()
    conn.close()


def get_all_tasks() -> list[Task]:
    conn = connect()
    rows = conn.execute("SELECT * FROM tasks ORDER BY id").fetchall()
    conn.close()
    return [row_to_task(row) for row in rows]


def get_task(task_id: int) -> Task | None:
    conn = connect()
    row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    conn.close()
    if row is None:
        return None
    return row_to_task(row)


def create_task(title: str) -> Task:
    conn = connect()
    row = conn.execute(
        "INSERT INTO tasks (title, created) VALUES (?, ?) RETURNING *",
        (title, date.today().isoformat()),
    ).fetchone()
    conn.commit()
    conn.close()
    return row_to_task(row)


def update_task(task_id: int, title: str, done: bool) -> Task | None:
    conn = connect()
    conn.execute(
        "UPDATE tasks SET title = ?, done = ? WHERE id = ?",
        (title, int(done), task_id),
    )
    conn.commit()
    conn.close()
    return get_task(task_id)


def delete_task(task_id: int) -> bool:
    conn = connect()
    cur = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    conn.close()
    return deleted
