import datetime

myBirthday = datetime.datetime(1990, 9, 10)

# print(myBirthday)
print(myBirthday.strftime("%B"))
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%a"))
print(myBirthday.strftime("%A"))


print(myBirthday.strftime("%d %B %Y"))
