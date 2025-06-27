import sqlite3

db = sqlite3.connect('app123.db')
cr = db.cursor()

cr.execute("CREATE TABLE if not exists users (user_id INTEGER , name TEXT)")
cr.execute(
    "CREATE TABLE if not exists skills (name TEXT, progress INTEGER , user_id INTEGER)")

user_id = 1  # Assuming a single user for simplicity


def commit_and_close():
    db.commit()
    db.close()
    print("Database connection closed.")


message = """
what do you want?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option:
"""

input_value = input(message).strip().lower()

commands_list = ["s", "a", "d", "u", "q"]


def show_all_skills():
    cr.execute(f"SELECT * FROM skills WHERE user_id = '{user_id}'")
    result = cr.fetchall()
    print(f"Total skills: {len(result)}")
    if len(result) > 0:
        print("showing all skills with progress: ")
    for row in result:
        print(f"Skill: {row[0]}, Progress: {row[1]}%")
    commit_and_close()


def add_new_skill():
    sk = input("Enter Skill name: ").strip().capitalize()
    progress = input("Enter Skill progress: ").strip()
    cr.execute(
        f"INSERT INTO skills (name, progress, user_id) VALUES ('{sk}', '{progress}', '{user_id}')")
    commit_and_close()


def delete_skill():
    sk = input("Enter Skill name: ").strip().capitalize()
    cr.execute(
        f"delete from skills where name = '{sk}' and user_id = {user_id}")
    commit_and_close()


def update_skill_progress():
    sk = input("Enter Skill name: ").strip().capitalize()
    progress = input("Enter the new Skill progress: ").strip()
    cr.execute(
        f"update skills set progress = '{progress}' where name = '{sk}' and user_id = {user_id}")
    commit_and_close()


def quit_app():
    print("Quitting the app...")
    commit_and_close()


if input_value in commands_list:
    print(f"You have selected: {input_value}")
    if input_value == "s":
        show_all_skills()
    elif input_value == "a":
        add_new_skill()
    elif input_value == "d":
        delete_skill()
    elif input_value == "u":
        update_skill_progress()
    elif input_value == "q":
        quit_app()

    else:
        print("Invalid option selected.")
else:
    print(
        f"Invalid option: {input_value}. Please choose from {commands_list}.")
