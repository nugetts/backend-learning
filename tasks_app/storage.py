import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from tasks_app.models import Task

DATA_FILE = Path("tasks.json")


def save_tasks(tasks: list[Task]) -> None:
    data = []
    for task in tasks:
        item = asdict(task)
        item["created"] = task.created.isoformat()
        data.append(item)

    text = json.dumps(data, ensure_ascii=False, indent=2)
    DATA_FILE.write_text(text, encoding="utf-8")


def load_tasks() -> list[Task]:
    if not DATA_FILE.exists():
        return []

    text = DATA_FILE.read_text(encoding="utf-8")
    data = json.loads(text)

    tasks = []
    for item in data:
        task = Task(
            id=item["id"],
            title=item["title"],
            done=item["done"],
            created=date.fromisoformat(item["created"]),
        )
        tasks.append(task)
    return tasks