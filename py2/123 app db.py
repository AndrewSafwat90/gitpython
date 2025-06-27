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
    print("Showing all skills...")


def add_new_skill():
    print("Adding a new skill...")


def delete_skill():
    print("Deleting a skill...")


def update_skill_progress():
    print("Updating skill progress...")


def quit_app():
    print("Quitting the app...")


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
