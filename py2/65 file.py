# import os
# print(os.getcwd())
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# print(os.getcwd())

file = open(r"E:\python\py1\py2\andrew.txt", "r")

# print(file)
# print(file.read())

# print(file.read(5))
# print(file.readline())
# print(file.readlines())

for line in file:
    print(line)
    if line.startswith("003"):
        break
file.close()
