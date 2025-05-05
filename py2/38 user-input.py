# fName = input("what's is your first name ?")
# mName = input("what's is your Middle name ?")
# lName = input("what's is your Last name ?")
# age = input("My age is :")

# fName = fName.strip().capitalize()
# mName = mName.strip().capitalize()
# lName = lName.strip().capitalize()
# age = age.strip()


# print(f"My name is {fName}.{mName:.1s} {lName}, and my age is {age}")


# email = "andrew.safwat@gmail.com"

# print(email[0:email.index("@")])

theName = input('what\'s your name? ')
email = input('what\'s your Email? ')

username = email[:email.index("@")].strip().capitalize()
domain = email[email.index("@")+1:]


print(f"Your Username is {username} \n your domain is {domain}")
