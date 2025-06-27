class BaseOne:
    def __init__(self):
        print("BaseOne initialized")

    def base_one_method(self):
        print("BaseOne method called")


class BaseTwo:
    def __init__(self):
        print("BaseTwo initialized")

    def base_two_method(self):
        print("BaseTwo method called")


class Derived(BaseOne, BaseTwo):
    pass


# Create an instance of the Derived class
S1 = Derived()

print(S1.base_one_method)
print(S1.base_two_method)
S1.base_one_method()  # Call method from BaseOne
S1.base_two_method()  # Call method from BaseTwo
# This will automatically call the __init__ methods of BaseOne and BaseTwo
