# class Member:
#     def __init__(self, name):
#         self.name = name    # public variable


# one = Member("Andrew")
# print(one.name)  # Accessing public variable
# one.name = "Monica"  # Accessing public variable
# print(one.name)  # Accessing public variable again


# class Member:
#     def __init__(self, name):
#         self._name = name    # public variable


# one = Member("Andrew")
# print(one._name)  # Accessing public variable
# one._name = "Monica"  # Accessing public variable
# print(one._name)  # Accessing public variable again


class Member:
    def __init__(self, name):
        self.__name = name    # private variable

    def get_name(self):
        # Accessing private variable through a method
        return f"Hello {self.__name}"


one = Member("Andrew")
print(one.get_name())  # Accessing private variable
