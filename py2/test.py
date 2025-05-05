# # list = [1, 2, 3, 4, 5]
# # # print(list.index(list[-1]))

# # list.remove(1)
# # print(list)


# a = {1, 2, 3}
# b = {"A", "B",  3}
# a.difference(b)
# print(a.difference(b))

# print("*" * 50)

# a = {1, 2, 3}
# b = {"A", "B",  3}
# print(a)
# a.difference_update(b)
# print(a)


# print("*" * 50)

# a = {1, 2, 3}
# b = {"A", "B",  3}
# print(a)
# print(a.intersection(b))
# print(a)


# print("*" * 50)

# a = {1, 2, 3}
# b = {"A", "B",  3}
# print(a)
# a.intersection_update(b)
# print(a)


# print("*" * 50)

# a = {1, 2, 3}
# b = {"A", "B",  3}
# print(a)
# print(a.symmetric_difference(b))
# print(a ^ b)
# print(a)


# print("*" * 50)

# a = {1, 2, 3}
# b = {"A", "B",  3}
# print(a)
# a.symmetric_difference_update(b)

# print(a)


# print("*" * 50)

# a = {1, 2, 3}
# b = {"A", "B",  3}

# print(a.issuperset(b))

# print("*" * 50)

# a = {1, 2, 3, "A", "B"}
# b = {"A", "B",  3}

# print(a.issuperset(b))


# print("*" * 50)

# a = {1, 2, 3}
# b = {"A", "B",  3}

# print(a.issubset(b))

# print("*" * 50)

# a = {1, 2, 3, "A", "B"}
# b = {"A", "B", "C", 1, 2, 3}

# print(a.issubset(b))

print("*" * 50)

user = {
    "Andrew": 1,
    "Safwat": 2,
    "Makin": 3
}

print(user.keys())
print(user.values())

print("*" * 50)

languages = {
    "one": {
        "name": "HTML",
        "progress": 80
    },
    "two": {
        "name": "CSS",
        "progress": 90
    },
    "Three": {
        "name": "Python",
        "progress": 30
    },
}

print(languages)
print(languages["one"]['name'])
print(languages["two"]['progress'])


print("*" * 50)

one = {
    "name": "Python",
    "progress": 30
}

two = {
    "name": "CSS",
    "progress": 90
}

alLang = {
    "one": one,
    "two": two
}

print(alLang["one"]["name"])


print("*" * 50)

one = {
    "name": "Python"
}
print(one)
print(one.setdefault("name", "Andrew"))
print(one)


print("*" * 50)

one = {
    "name": "Python",
    "progress": 30
}
print(one)
one.update({"age": 36})
print(one)
print(one.popitem())


print("*" * 50)
print("*" * 50)

a = {"key1", "key2", "key3"}
b = "1"

# c = dict.fromkeys(a, b)
print(dict.fromkeys(a, b))

print("*" * 50)

print(bool(False))

print("*" * 50)
print("*" * 50)

age = 36

print(age > 16)
print(not age > 16)


x = 10
y = 20

x = x+y
print(x)

print("*" * 50)
x = 10
y = 20
x += y
print(x)
