
# التكليف 01
# num1 = int(input("Please enter the first number: ").strip())
# num2 = int(input("Please enter the second number: ").strip())
# operation = input(
#     "Please enter the operation ((+)= 1 , (-) = 2, (*) = 3, (/) = 4): ").strip()
# # Validate the operation

# # Perform the operation
# if operation == "1":
#     print(num1 + num2)
# elif operation == "2":
#     print(num1 - num2)
# elif operation == "3":
#     print(num1 * num2)
# elif operation == "4":
#     print(num1 / num2)
# else:
#     print("Invalid operation")


print("*" * 50)
# التكليف 02
# num = int(input("Please enter your age: ").strip())

# print("App Is Not Suitable For You" if num < 16 else "App Is Suitable For You")


print("*" * 50)
# التكليف 03
# age = int(input("Please enter your age: ").strip())

# ageInMonths = age * 12
# ageInWeeks = age * 52
# ageInDays = age * 365
# ageInHours = age * 365 * 24
# ageInMinutes = age * 365 * 24 * 60
# ageInSeconds = age * 365 * 24 * 60 * 60

# if age > 10 and age < 100:

#     print(f"Your age in months is: {age * 12} months")
#     print(f"Your age in weeks is: {age * 52} weeks")
#     print(f"Your age in days is: {age * 365} days")
#     print(f"Your age in hours is: {age * 365 * 24} hours")
#     print(f"Your age in minutes is: {age * 365 * 24 * 60} minutes")
#     print(f"Your age in seconds is: {age * 365 * 24 * 60 * 60} seconds")

# else:
#     print("Please enter a valid age between 10 and 100")


print("*" * 50)
# التكليف 04

countries = ["Egypt", "Palestine", "Syria",
             "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
print("Welcome to our store")
print(f"Available countries are: {countries}")
country = input("Input Your Country : ").strip().lower()

if country == "egypt" or country == "Palestine" or country == "Syria":
    print(f"Your price is: ${price - discount}")

else:
    print(f"Your price is: ${price}")
