# def printHello():
#     print("Hello from inside function")


# printHello()


# def addit(n1, n2):
#     if type(n1) != int or type(n2) != int:
#         print("Please insert numbers only")
#     else:
#         print(n1 + n2)


# addit(3, "3")


# def full_name(first, second, third):
#     print(f"Hello {first.strip().capitalize()} {second:.1s} {third} ")


# full_name("Andrew", "Safwat", "Makin")


# def details(name, *skills):
#     print(f"hello {name} your skills are: ")
#     for skill in skills:
#         print(skill)


# details("Andrew", "Py", "HTML")

# dictt = {
#     "py": "90",
#     "html": "60"
# }


# def details(**skills):
#     print(f"hello your skills are: ")
#     for skill, value in skills.items():
#         print(f"{skill} >> {value}")


# details(**dictt)

dictt = {
    "py": "90",
    "html": "60",
    "CSS": "70"
}
tuplee = ("Py", "HTML")


def show_skills(name, *skills, **skillsWithProgress):
    print(f"hello {name} the skills without progress : ")
    for skill in skills:
        print(f" - {skill}")

    print("skills with progress are : ")
    for skill_key, skill_value in dictt.items():
        print(f" - {skill_key} >> {skill_value}")


show_skills("Andrew", *tuplee, **dictt)
