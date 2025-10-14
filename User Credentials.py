import pickle
users = {
        "usr1":{"uid": "jselwyn", "pwd":"123"},
        "usr2":{"uid": "bjoe", "pwd":"321"},
        "usr3":{"uid": "jbilly", "pwd":"567"},
        "usr4":{"uid": "mjim", "pwd":"877"},
}


with open("myUsers.dat", "wb") as myfile:
    pickle.dump(users, myfile)
myfile.close()

with open("myUsers.dat", "rb") as myfile:
    myDic = pickle.load(myfile)
    uid = input("Enter your user id")
    pwd = input("Please enter your password")
    i=1
    for x in myDic:
        var = "usr"+str(i)
        try1=""
        try2=""
        if uid == myDic[var]["uid"]:
            try1 = "valid"
            if pwd == myDic[var]["pwd"]:
                try2 = "valid"
                print("Welcome")
                break
        i+=1
    if try1 != "valid":
        print("Invalid username")
    elif try2 != "valid":
        print("Invalid password")