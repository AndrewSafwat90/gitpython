tries = 4

mainPass = "andrew123"

inputPass = input("please enter your password: ")

while inputPass != mainPass:
    tries -= 1
    print(
        f"please enter the correct password , you have {'LAST' if tries == 0 else tries} times left")
    inputPass = input("please enter your password: ")

    if tries == 0:
        break

# print("loop Ended")
else:
    print("Correct Password")
