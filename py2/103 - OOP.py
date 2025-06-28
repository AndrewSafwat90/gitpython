# class Member:
#     def __init__(self,):
#         self.name = "Andrew"


# # memnber_one = Member()
# # print(memnber_one.__class__)

# # Member()
# memnber_one = Member()
# memnber_two = Member()
# memnber_three = Member()
# # print(type(memnber_one))
# print(memnber_one.name)
# print(memnber_two.name)
# print(memnber_three.name)


# class Member:
#     def __init__(self, first_name):
#         self.name = first_name


# # memnber_one = Member()
# # print(memnber_one.__class__)

# # Member()
# memnber_one = Member(first_name="John")
# memnber_two = Member(first_name="Doe")
# memnber_three = Member(first_name="Jane")
# # print(type(memnber_one))
# print(memnber_one.name)
# print(memnber_two.name)
# print(memnber_three.name)


# class Member:
#     def __init__(self, first_name, middle_name, last_name):
#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name


# # memnber_one = Member()
# # print(memnber_one.__class__)

# # Member()
# memnber_one = Member(first_name="John")
# memnber_two = Member(first_name="Doe")
# memnber_three = Member(first_name="Jane")
# # print(type(memnber_one))
# print(memnber_one.name)
# print(memnber_two.name)
# print(memnber_three.name)


class Member:
    def __init__(self, first_name, middle_name, last_name):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name

    def full_name(self):
        return f"{self.fname} {self.mname} {self.lname}"
