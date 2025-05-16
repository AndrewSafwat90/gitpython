from functools import reduce


def sumAll(num1, num2):
    return num1 + num2


numbers = [1, 2, 3, 4, 5]
Result = reduce(sumAll, numbers)
print(Result)
