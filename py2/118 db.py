import sqlite3

db = sqlite3.connect('app.db')
db.execute(
    "CREATE TABLE if not exists skills (name TEXT, progress INTEGER , user_id INTEGER)")
