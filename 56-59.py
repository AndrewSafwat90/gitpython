# التكليف 01

# print("Enter two numbers and an operator (add (a), subtract (s), multiply (m)):")
# num1 = float(input("num1 ").strip())
# num2 = float(input("num2 ").strip())
# operator = input("operator ").strip().lower()
# if operator == "":
#     operator = "add"  # Default to addition if no operator is provided


# def Calculate(num1, num2, operator):
#     if operator == "add" or operator == "a":
#         return num1 + num2
#     elif operator == "subtract" or operator == "s":
#         return num1 - num2
#     elif operator == "multiply" or operator == "m":
#         return num1 * num2

#     else:
#         return "Invalid Operator"


# print(f"Result: {Calculate(num1, num2, operator)}")
# print("*" * 50)
# التكليف 02
# listOfNumbers = input(
#     "Please enter numbers separated by commas: ").strip().split(",")
# listOfNumbers = [int(num.strip()) for num in listOfNumbers]
# print("You entered:", listOfNumbers)


# def addition(*numbers):
#     total = 0
#     for number in numbers:
#         if number == 10:
#             continue
#         elif number == 5:
#             total -= 5
#         else:
#             total += number
#     return f"Total sum is {total}"


# print(addition(*listOfNumbers))
print("*" * 50)


# التكليف 03

Username = input("Please Enter your name: ").strip()
show_skills = input(
    "Please Enter your name then your skills separated by commas: ").strip()
show_skillsToList = show_skills.split(",")


def show_skills_function(name, *skills):
    if len(skills) == 0:
        return f"Hello {name}, you have no skills to show."
    else:
        for skill in skills:
            return f"Hello {name}, your skills are: {skill.strip()}"


print(show_skills_function(Username, *show_skillsToList))
print("*" * 50)
# التكليف 04
