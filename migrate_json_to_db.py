from tasks_app import db
from tasks_app.storage import load_tasks

db.init_db()

if db.get_all_tasks():
    print("В базе уже есть задачи, перенос пропущен.")
else:
    old_tasks = load_tasks()
    conn = db.connect()
    for t in old_tasks:
        conn.execute(
            "INSERT INTO tasks (title, done, created) VALUES (?, ?, ?)",
            (t.title, int(t.done), t.created.isoformat()),
        )
    conn.commit()
    conn.close()
    print(f"Перенесено задач: {len(old_tasks)}")
