# التكليف 01
# my_list = [1, 2, 3, 3, 4, 5, 1]
# unique_list = set(my_list)

# my_list_again = list(unique_list)
# print(my_list_again)
# print(type(my_list_again))
# my_list_again.remove(5)
# print(my_list_again)

print("*" * 50)
# التكليف 02
# nums = {1, 2, 3}
# letters = {"A", "B", "C"}

# numAndLetter = nums | letters
# numAndLetter2 = nums.union(letters)
# nums.update(letters)
# print(numAndLetter)
# print(numAndLetter2)
# print(nums)

print("*" * 50)
# التكليف 03
# my_set = {1, 2, 3}
# letters = {"A", "B", "C"}

# print(my_set)
# my_set.clear()
# print(my_set)
# my_set.add("A")
# my_set.add("B")
# my_set.discard("C")
# print(my_set)


print("*" * 50)
# التكليف 04
# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}

# print(set_one.issubset(set_two))

# التكليف 05

my_dict = {
    "HTML": 100,
    "CSS": 90,
    "JS": 80
}

my_dict.update({"Python": 70})

print(f" - HTML progress is {my_dict['HTML']}")
print(f" - CSS progress is {my_dict['CSS']}")
print(f" - JS progress is {my_dict['JS']}")
print(f" - Python progress is {my_dict['Python']}")
