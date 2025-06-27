import sqlite3

db = sqlite3.connect('app120.db')
cr = db.cursor()
cr.execute("CREATE TABLE if not exists users (user_id INTEGER , name TEXT)")
cr.execute(
    "CREATE TABLE if not exists skills (name TEXT, progress INTEGER , user_id INTEGER)")


cr.execute("INSERT INTO users (user_id, name) VALUES (1, 'Alice')")
cr.execute("INSERT INTO users (user_id, name) VALUES (2, 'Bob')")
db.commit()

# cr.execute("select name from users")
cr.execute("SELECT * FROM users")
# print(cr.fetchone())
print(cr.fetchall())
db.close()


# db.execute(
#     "CREATE TABLE if not exists skills (name TEXT, progress INTEGER , user_id INTEGER)")
