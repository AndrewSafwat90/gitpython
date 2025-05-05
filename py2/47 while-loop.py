# # a = 0

# # while a < 10:
# #     print(a)
# #     a += 1
# # else:
# #     print("Loop is done")


# list = ["An", "df", "dd", "gg", "jt", "we", "sf", "gj", "ju", "ss"]

# a = 0


# while a < len(list):
#     print(
#         f"#{str(a+1).zfill(2)} and the name is {list[a]} with index : {list.index(list[a])}")
#     a += 1

# else:
#     print("Ending")


myFavWebSites = []

max = 5

while max > 0:
    website = input("Enter the website Name ")
    # editedwebsite = f"www.{website}.com"
    myFavWebSites.append(f"https://www.{website.strip().lower()}.com")
    max -= 1
    print(f"{website} add and max is is {max} ")
    print(f"Done the list is {myFavWebSites}")
else:
    print("Bookmark is full , you can't add more")

if len(myFavWebSites) > max:
    myFavWebSites.sort()

    index = 0
    print("Printint the Website list in sorting")
    while index < len(myFavWebSites):

        print(myFavWebSites[index])
        index += 1
