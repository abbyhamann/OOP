projects = {}
while True:
    print("1. Project Initiation")
    print("2. Project CLosure")
    print("3. Project Progress Update")
    print("4. Print a specific Project")
    print("5. Print all projects")
    print("6. Quit Application")

    choice = input("Please enter your choice")
    if choice == "1":
        key = input("Please enter the project id")
        title = input("Please enter the project title")
        managers = input("Please enter a manager name")
        manList = [managers]
        moreman = input("Are there more managers? (Enter Y/N)")
        while moreman == "Y":
            manList.append(input("Please enter a manager name"))
            moreman = input("Are there more managers? (Enter Y/N)")
        start_date = input("Please enter the start date of the project")
        end_date = input("Please enter the end date of the project")
        sponsor = input("Please enter the sponsor of the project")
        budget = input("Please enter the budget for the project")
        tech = input("Please enter the technologies for the project")
        techList = [tech]
        moretech = input("Are there more technologies? (Enter Y/N)")
        while moretech == "Y":
            techList.append(input("Please enter a technology for the project"))
            moretech = input("Are there more technologies? (Enter Y/N)")
        team_members = input("Please enter a member of the project")
        memberList = [team_members]
        moremem = input("Are there more members? (Enter Y/N)")
        while moremem == "Y":
            techList.append(input("Please enter a member"))
            memberList = input("Are there more members? (Enter Y/N)")
        projects.update({key:{
            "title": title,
            "manList": manList,
            "start_date":start_date,
            "end_date":end_date,
            "sponsor":sponsor,
            "budget": budget,
            "techList":techList,
            "memberList": memberList,
                        }})

    elif choice == "2":
        key = input("Please enter the project id you'd like to close")
        del projects[key]

    elif choice == "3":
        key = input("Please enter the project id you'd like to update")
        element = input("Please enter the element you'd like to update. Options: title, manList, start_date, end_date, sponsor, budget, techList, memList")
        if element == "managers" or element == "tech" or element == "member":
            update = input("Would you like to add or remove an element from this list?")
            if update == "add":
                projects[key][element].append(input("Please enter what you'd like to add"))
            else:
                projects[key][element].remove(input("Please enter what you'd like to remove"))
        else:
            projects[key][element] = input("Please enter the new value")

    elif choice == "4":
        print(projects[input("Please enter the project id you'd like to print")])

    elif choice == "5":
        print(projects)

    elif choice == "6":
        break
