# def myDecorator(fun):
#     def nestedFunc(num1, num2):
#         if num1 < 0 or num2 < 0:
#             print("Negative numbers are not allowed")
#         fun(num1, num2)
#     return nestedFunc


# @myDecorator
# def myFunction(num1, num2):
#     print(num1 + num2)


# myFunction(5, 10)

from time import time


def speedTest(func):
    def wrapper():
        start = time()
        print(start)
        func()
        end = time()
        print(end)
        print(
            f"Function {func.__name__} took {end - start:.4f} seconds to execute.")
    return wrapper


@speedTest
def test():
    for i in range(1, 100):
        print(i)


test()
