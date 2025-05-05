# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in list:
#     # print(number)
#     if number % 2 == 0:
#         print(f"the number {number} is even")
#     else:
#         print(f"the number {number} is Odd")


# mySlills = {
#     "A": "90%",
#     "B": "80%",
#     "C": "70%",
#     "D": "60%",
#     "E": "50%",
# }

# for skill in mySlills:
#     print(f"my progress in {skill} is : {mySlills[skill]}")


# persons = ["Andrew", "Safwat", "Makin"]
# skills = {"Python", "SQL", "PHP"}

# for name in persons:
#     print(f"{name} skills are :")
#     for skill in skills:
#         print(f" - {skill}")

people = {
    "Andrew": {
        "Python": "90%",
        "SQL": "80%",
        "PHP": "70%"
    },
    "Safwat": {
        "Python": "60%",
        "SQL": "50%",
        "PHP": "40%"
    },
    "Makin": {
        "Python": "30%",
        "SQL": "20%",
        "PHP": "10%"
    },
}
# {people[name]}
print(people["Safwat"])
print(people["Andrew"]["Python"])


# for name in people:
#     print(f"skills and progress for {name} are:  ")

#     for skill in people[name]:
#         print(f" - {skill.upper()} >> {people[name][skill]}")

for name in people:
    print(f"skills and progress for {name} are:  ")

    for skill in people[name]:
        print(f" {people[name][skill]}")
