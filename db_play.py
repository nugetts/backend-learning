import sqlite3

conn = sqlite3.connect("play.db")
cur = conn.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS tasks ("
    "id INTEGER PRIMARY KEY, "
    "title TEXT NOT NULL, "
    "done INTEGER NOT NULL DEFAULT 0)"
)

cur.execute("INSERT INTO tasks (title) VALUES (?)", ("Выучить SQL из Python",))
conn.commit()

cur.execute("SELECT id, title, done FROM tasks")
for row in cur.fetchall():
    print(row)

conn.close()
