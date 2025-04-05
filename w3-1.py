# #
# # x = 5
# # x = int(5)

# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# x, y, z = ["apple", "banana", "cherry"]

# print(x)
# print(y)
# print(z)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# x = 5
# y = "John"
# print(x, y)


# print('Hello', 'World')

# x = "awesome"


# def myfunc():
#     x = "fantastic"
#     print("Python is " + x)    # >>  Python is fantastic


# myfunc()

# print("Python is " + x)   # >> Python is awesome


# def myfunc():
#     global x
#     x = "fantastic"


# myfunc()

# print("Python is " + x)


# x = str(100)

# quote = "He said: \"Hello!\""
# print(quote)

# print("It's alright")

# print('It\'s alright')

# print("It\'s alright")

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# for x in "banana":
#     print(x)

# a = "Hello, World!"
# print(len(a))

# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# b = "Hello, World!"
# print(b[2:5])

# b = "Hello, World!"
# print(b[:5])

# b = "Hello, World!"
# print(b[-5:-2])

# a = "Hello, World!"
# print(a.upper())

# a = "Hello, World!"
# print(a.lower())

# a = "       Hello, World!           "
# print(a.strip())


# a = "Hello, World!"
# print(a.replace("H", "J"))


a = "Hello"
b = "World!"

print(a + b)    # HelloWorld!

print("Hello" + "World!")    # HelloWorld
print("Hello", "World!")    # Hello World

age = 36
txt = "My name is John, I am " + str(age)
# TypeError: can only concatenate str (not "int") to str
#  txt = "My name is John, I am " + age
print(txt)

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


txt = f"The price is {20 * 59} dollars"
print(txt)

print('Hello\fWorld!')
