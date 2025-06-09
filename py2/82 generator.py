def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4


mygen = myGenerator()
# print(type(myGenerator))
print(next(mygen))
print("Test 1")
print(next(mygen))
print("Test 2")
print(next(mygen))
print("Test 3")
print(next(mygen))
print("Test 4")


print("*" * 50)


for item in mygen:
    print(item)
