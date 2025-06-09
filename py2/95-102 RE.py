import re

# mysearch = re.search(r"[A-Z]{2}", "HHello World")

# print(mysearch)
# print(mysearch.group())
# print(mysearch.span())
# print(mysearch.string)


# email = input("Enter your email: ")
# mysearch = re.findall(r"[A-z0-9\.]+@[A-z0-9-]+\.com|net", email)

# empty_List = []

# if mysearch != []:
#     empty_List.append(mysearch)
#     print("Valid email found:", mysearch)
# else:
#     print("No valid email found")

# for email in empty_List:
#     print(email)


one = "I Love Python"

search_one = re.split(r"\s", one, 1)
print(search_one)
