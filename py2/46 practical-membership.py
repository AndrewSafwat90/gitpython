# Admin list

admins = ["Andrew", "Oliver", "Monica", "Safwat"]

# login

name = input("Please Insert your name ").capitalize().strip()

if name in admins:
    print(f"Hello {name} welcome back ")

    option = input("Delete or Update your name ? ").strip().lower()
    if option == "update" or option == "u":
        theNewNAme = input("Please Enter the new Name ").strip().capitalize()
        admins[admins.index(name)] = theNewNAme
        print(f"You Updated your name to {theNewNAme}")
    elif option == "delete" or option == "d":
        admins.remove(name)
        print("You deleted your name")
        print(admins)
    else:
        print("Wrong Option")

else:
    status = input("Yoy are not admin, add you ? y or n ? ").strip()

    if status == "Yes" or status == "y":
        # newAdmin = input("Please insert your Admin Name ").strip().capitalize()
        admins.append(name)
        print(admins)

    else:
        print("You refused to be admin")
