myStudents = {}
while True:
    print("1. Add a student")
    print("2. Remove a student")
    print("3. Edit a Student")
    print("4. Print the students")
    print("5. Quit")

    choice = input("Please enter the number of your choice")
    if choice == "1":
        name = input("Please enter the name of the student")
        major = input("Please enter the major of the student")
        year = input("Please enter the year of the student")
        credits = input("Please enter the student's credit hours")
        gpa = input("Please enter the student's GPA")
        key = input("Please enter the number of student this is you have added to the dictionary")
        myStudents.update({key:{
                        "name":name,
                        "major":major,
                        "year": year,
                        "credits": credits,
                        "gpa":gpa
                        }})
    elif choice == "2":
        key = input("Please enter the number of the student you'd like to remove")
        del myStudents[key]
    elif choice == "3":
        key = input("Please enter the number of the student you'd like to edit")
        name = input("Please enter the name of the student")
        major = input("Please enter the major of the student")
        year = input("Please enter the year of the student")
        credits = input("Please enter the student's credit hours")
        gpa = input("Please enter the student's GPA")
        myStudents.update({key:{
            "name": name,
            "major": major,
            "year": year,
            "credits": credits,
            "gpa": gpa
        }})
    elif choice == "4":
        print(myStudents)
    elif choice == "5":
        break

