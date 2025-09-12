nameList = []
ageList = []

while True:
    print("1. Add an element to the list")
    print("2. Remove an element from the list")
    print("3. Replace an element in the list")
    print("4. Sort the elements in the list")
    print("5. Reverse the elements in the list")
    print("6. Print the list")
    print("7. Exit")

    option = input("Enter your choice")

    if option == "1":
        append1 = input("Enter the name of the person you'd like to add")
        append2 = input("Enter the age of the person")
        nameList.append(append1)
        ageList.append(append2)
    elif option == "2":
        remove1 = input("Please enter the name of the person you'd like to remove")
        remove2 = input("Please enter the age of the person you'd like to remove")
        nameList.remove(remove1)
        ageList.remove(remove2)
    elif option == "3":
        index = int(input("Please enter the index of the element you'd like to replace"))
        newName = input("Please enter the name you'd like to replace it with")
        newAge = input("Please enter the age you'd like to replace it with")
        nameList[index] = newName
        ageList[index] = newAge
    elif option == "4":
        print("With the two lists, this will result in the ages and names getting out of order. Please choose another option")
    elif option == "5":
        nameList.reverse()
        ageList.reverse()
    elif option == "6":
        print(nameList)
        print(ageList)
    elif option == "7":
        break
    else:
        print("User input is invalid. Please enter an integer 1-7")