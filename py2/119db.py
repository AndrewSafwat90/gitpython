import sqlite3

db = sqlite3.connect('app119.db')
cr = db.cursor()
cr.execute("CREATE TABLE if not exists users (user_id INTEGER , name TEXT)")
cr.execute(
    "CREATE TABLE if not exists skills (name TEXT, progress INTEGER , user_id INTEGER)")

myList = ["Andrew", "Monica", "John", "Alice",
          "Bob", "Charlie", "David", "Eve", "Frank"]

for key, user in enumerate(myList):
    cr.execute(f"INSERT INTO users (user_id, name) VALUES {(key + 1, user)}")

# cr.execute("INSERT INTO users (user_id, name) VALUES (1, 'Alice')")
# cr.execute("INSERT INTO users (user_id, name) VALUES (2, 'Bob')")
# cr.execute("INSERT INTO skills (name, progress, user_id) VALUES ('Python', 80, 1)")
db.commit()
db.close()


# db.execute(
#     "CREATE TABLE if not exists skills (name TEXT, progress INTEGER , user_id INTEGER)")
