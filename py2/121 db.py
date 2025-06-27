import sqlite3


def get_all_data():

    try:
        db = sqlite3.connect('app121.db')

        print("Connected to the database successfully.")
        cr = db.cursor()
        cr.execute(
            "CREATE TABLE if not exists users (user_id INTEGER , name TEXT)")
        cr.execute("INSERT INTO users (user_id, name) VALUES (1, 'Alice')")
        cr.execute("INSERT INTO users (user_id, name) VALUES (2, 'Bob')")
        cr.execute("select * from users")

        result = cr.fetchall()

        print(f"Total records: {len(result)} rows")

        for row in result:
            print(f"User ID: {row[0]}, Name: {row[1]}")

    except sqlite3.Error as e:
        print(f"Error connecting to the database {e}")

    finally:
        if (db):
            db.close()
            print("Database connection closed.")


get_all_data()
