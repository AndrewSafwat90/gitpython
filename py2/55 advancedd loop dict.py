
# mySkills = {
#     "Python": "90%",
#     "SQL": "80%",
#     "PHP": "70%"
# }

# # print(mySkills.items())

# for skill_key, skill_value in mySkills.items():
#     print(f" - {skill_key} =>  {skill_value} :  ")


myUltimateSkills = {
    "Py": {
        "lib": "80",
        "Basics": "80",
    },
    "Flutter": {
        "lib": "80",
        "Basics": "80",
    },
}

# print(myUltimateSkills.items())
# dict_items([('Py', {'lib': '80', 'Basics': '80'}), ('Flutter', {'lib': '80', 'Basics': '80'})])


for skill_key, skill_value in myUltimateSkills.items():
    print(f" - language {skill_key} progress are : ")
    for child1, child2 in skill_value.items():
        print(f" - {child1} ==>>  {child2}")

#  - language Py progress are :
#  - lib ==>>  80
#  - Basics ==>>  80
#  - language Flutter progress are :
#  - lib ==>>  80
#  - Basics ==>>  80
