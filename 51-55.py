# التكليف 01
# my_nums = [15, 81, 5, 17, 20, 21, 13]
# my_nums.sort(reverse=True)
# count = 1
# for num in my_nums:
#     if num % 5 == 0:
#         print(f"{count} - {num}")
#         count += 1
# print("All Numbers Printed")


# print("*" * 50)
# التكليف 02

# for number in range(1, 21, 1):

#     if number in [6, 8, 12]:
#         continue
#     if number < 10:
#         print(f"0{number}")
#     else:
#         print(number)
# print("All Numbers Printed")


# print("*" * 50)
# التكليف 03

# my_ranks = {
#     'Math': 'A',
#     "Science": 'B',
#     'Drawing': 'A',
#     'Sports': 'C'
# }

# for subject, rank in my_ranks.items():
#     if rank == 'A':
#         print(f"My Rank in {subject} is {rank} This Equal 100 Points")
#     elif rank == 'B':
#         print(f"My Rank in {subject} is {rank} This Equal 80 Points")
#     elif rank == 'C':
#         print(f"My Rank in {subject} is {rank} This Equal 40 Points")

# print("All Ranks Printed")


my_ranks = {
    'Math': 'A',
    'Science': 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

my_points = {
    "A": 100,
    "B": 80,
    "C": 40
}
sum = 0
for subject in my_ranks:
    for point in my_points:
        if my_ranks[subject] == point:
            sum += my_points[point]
            print(
                f"My Rank in {subject} is {my_ranks[subject]} This Equal {my_points[point]} Points")
print(f"Total Points: {sum}")


print("*" * 50)
# التكليف 04
