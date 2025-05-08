# file = open(r"E:\python\py1\py2\andrew.txt", "w")

# file.write("007 test 7\n")
# file.write("008 test 8\n")
# file.write("009 test 9\n")


# file2 = open(r"E:\python\py1\py2\fun.txt", "w")
# file2.write("Andrew Safwat \n" * 1000)
# file3 = open(r"E:\python\py1\py2\fun2.txt", "w")
# file3.writelines(["001 test 1\n", "002 test 2\n", "003 test 3\n"])


# file4 = open(r"E:\python\py1\py2\fun3.txt", "w")
# file4.writelines(["001 test 1\n", "002 test 2\n", "003 test 3\n"])
# file4.write("Test \n")


file4 = open(r"E:\python\py1\py2\fun3.txt", "a")
print(file4.tell())
