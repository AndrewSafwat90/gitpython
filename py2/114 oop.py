class Member:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        # Accessing private variable through a method
        return f"Hello {self.__name}"

    def set_name(self, newName):
        self.__name = newName


one = Member("Andrew")
print(one.get_name())  # Accessing private variable
one.set_name("Monica")  # Accessing private variable
print(one.get_name())  # Accessing private variable again
