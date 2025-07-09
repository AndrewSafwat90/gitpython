import sqlite3

db = sqlite3.connect('app127.db')
cr = db.cursor()
cr.execute(
    "CREATE TABLE if not exists skills (name TEXT, progress INTEGER, user_id INTEGER)")
cr.execute("insert into skills values ('Python', 50, 1)")

cr.execute("select * from skills")
results = cr.fetchall()
for row in results:
    print(f"Skill: {row[0]}, Progress: {row[1]}% و User ID: {row[2]}")
