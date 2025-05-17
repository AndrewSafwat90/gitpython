
# التكليف 01
# name = input("Please enter your name: \n")
# print(f"Hello, {name.capitalize().strip()}!. Happy To See You Here.")

print("*" * 50)
# التكليف 02
# age = int(input("Please enter your age: \n")).strip()


# if age < 16:
#     print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
# else:
#     print(f"Hello Your Age Is {age}, Enjoy Reading The Articles")
print("*" * 50)
# التكليف 03
# first_name = input("Please enter your first name: \n").strip().capitalize()
# second_name = input("Please enter your second name: \n").strip().capitalize()

# print(f"Hello {first_name} {second_name:.1s}. Welcome to the Python Course.")


print("*" * 50)
# التكليف 04

email = input("Please enter your email: \n").strip().lower()

print(f"Your Name Is : {email[0:email.index('@')]} ")
print(
    f"Email Service Provider Is : {email[email.index('@')+1: email.index('.', email.index('@'))]} ")

print(f"Top level domain Is : {email[email.index('.', email.index('@'))+1:]} ")
# email.index('.', email.index('@'))+1    >>> to get the index of the dot after the @
