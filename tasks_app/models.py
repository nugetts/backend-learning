from dataclasses import dataclass, field
from datetime import date


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    created: date = field(default_factory=date.today)