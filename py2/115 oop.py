class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"Hello: {self.name}"

    def calAge(self):
        return self.age * 365


one = Member("Andrew", 30)
print(one.say_hello())  # Accessing public method
print(one.calAge())  # Accessing public method
