# vid >> 104
# class Member:
#     def __init__(self, fname, mname, lname, gender):
#         self.fname = fname
#         self.lname = lname
#         self.name = mname
#         self.gender = gender

#     def full_Name(self):
#         return f"{self.fname} {self.name} {self.lname}"

#     def welcome(self):
#         if self.gender == "female":
#             return f"Welcome Ms. {self.fname} to our club!"
#         elif self.gender == "male":
#             return f"Welcome Mr. {self.fname} to our club!"
#         else:
#             return f"Welcome {self.fname} to our club!"


#     def get_all(self):
#         return f"{self.welcome()} Your full name is {self.full_Name()}"
# # member_one = Member("Andrew", "M.", "Smith")
# # print(member_one.fname, member_one.name, member_one.lname)


# member_one = Member("Andrew", "M.", "Smith", "male")
# member_two = Member("Monica", "L.", "Johnson", "female")
# # print(member_one.full_Name())

# # print(member_one.welcome())
# # print(member_two.welcome())

# print(member_one.get_all())


# vid >> 107

class Member:
    not_alowed_names = ["admin", "administrator", "root"]
    userCount = 0

    @classmethod
    def get_user_count(cls):
        return f"we have {cls.userCount} members in our club."

    def __init__(self, fname, mname, lname, gender):
        self.fname = fname
        self.lname = lname
        self.name = mname
        self.gender = gender
        Member.userCount += 1

    def full_Name(self):
        if self.fname.lower() in Member.not_alowed_names:
            raise ValueError(f"'{self.fname}' is not allowed as a first name.")
        else:
            return f"{self.fname} {self.name} {self.lname}"

    def welcome(self):
        if self.gender == "female":
            return f"Welcome Ms. {self.fname} to our club!"
        elif self.gender == "male":
            return f"Welcome Mr. {self.fname} to our club!"
        else:
            return f"Welcome {self.fname} to our club!"

    def get_all(self):
        return f"{self.welcome()} Your full name is {self.full_Name()}"
# member_one = Member("Andrew", "M.", "Smith")
# print(member_one.fname, member_one.name, member_one.lname)

    def delete_member(self):
        Member.userCount -= 1
        return (f"{self.fname} has been removed from the club.")


print(Member.userCount)
member_one = Member("Andrew", "M.", "Smith", "male")
member_two = Member("Monica", "L.", "Johnson", "female")
print(Member.userCount)

print(member_two.delete_member())

print(Member.userCount)
# print(member_one.full_Name())

# print(member_one.welcome())
# print(member_two.welcome())

# print(member_one.get_all())

print(Member.get_user_count())


# vid > 109


class skill:

    def __init__(self):
        self.skills = ["Python", "JavaScript", "HTML", "CSS", "SQL"]

    def __str__(self):
        return f"My skills are: {', '.join(self.skills)}"

    def __len__(self):
        return len(self.skills)


profile1 = skill()
print(profile1)
print(len(profile1))
# print(dir(profile1))


# myString = "Andrew"
# print(type(myString))
# print(str.upper(myString))
# print(myString.upper())


# vid >> 110


class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        # print(f"Food class initialized and {self.name} is ready to eat!")

    def eat(self):
        print("Eating food")


class Apple(Food):
    def __init__(self, name, price, amount):
        #
        super().__init__(name, price)  # Call the parent class constructor
        self.amount = amount
        print(
            f"Apple class initialized and {self.name} is ready to eat!,"
            f"the price is {self.price},"
            f"and the amount is {self.amount}.")

    def eat(self):
        print(
            f"Eating {self.name} which costs {self.price} and amount is {self.amount}")


fruirt = Apple("Pizza", 100, 500)
fruirt.eat()
