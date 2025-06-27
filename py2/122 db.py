import sqlite3


db = sqlite3.connect('app122.db')

print("Connected to the database successfully.")
cr = db.cursor()
cr.execute(
    "CREATE TABLE if not exists users (user_id INTEGER , name TEXT)")
cr.execute("INSERT INTO users (user_id, name) VALUES (1, 'Alice')")
cr.execute("INSERT INTO users (user_id, name) VALUES (2, 'Bob')")
cr.execute("select * from users")

print(cr.fetchone())
print(cr.fetchone())


db.close()
