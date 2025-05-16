# def chechNum(num):
#     return num > 10


# muNumbers = [1,  16, 17, 18, 19, 20]
# filteredNums = filter(chechNum, muNumbers)

# print(type(filteredNums))

# for num in filteredNums:
#     print(num)


def chechNames(name):
    return name.startswith("A")


myNames = ["Ahmed", "Osama", "Oliver", "monica", "Andrew"]
filteredNames = filter(chechNames, myNames)

print(type(filteredNames))

for names in filteredNames:
    print(names)
