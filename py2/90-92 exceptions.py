x = -10

# if x < 0:
#     print(f"{x} is negative")
#     raise Exception("Negative value encountered")
#     print("This line will not execute")
# elif x:
#     print(f"{x} is Good")

# try:
#     print(10/0)

# except:
#     print("An error occurred")


file = None
tries = 5
while tries > 0:
    try:
        print(f"Tries left: {tries}")
        print("Enter the file name and PATH")
        print("Example : e:/python/py1/py2/file_nam.extension")
        fileNameAndPath = input("File name  >>  ").strip()
        file = open(fileNameAndPath)
        print(file.read())
        break
    except FileNotFoundError:
        print("File Not Found")
        tries -= 1
    except:
        print("An error occurred")
        tries -= 1

    finally:
        if file is not None:
            file.close()
            print("File closed")
else:
    print("No more tries left")
