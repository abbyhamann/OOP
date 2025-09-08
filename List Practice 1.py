myList = []

while True:
    print("1. Append to the list")
    print("2. Remove from the list")
    print("3. Pop an element from the list")
    print("4. Display the list")
    print("5. Quit")

    option = input("Enter your choice")

    if option == "1":
        append = input("Enter what you'd like to append")
        myList.append(append)
    elif option == "2":
        remove = input("Please enter what you'd like to remove")
        myList.remove(remove)
    elif option == "3":
        myList.pop()
    elif option == "4":
        print(myList)
    elif option == "5":
        break
    else:
        print("User input is invalid. Please enter an integer 1-5")