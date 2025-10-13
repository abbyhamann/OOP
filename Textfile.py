
file1 = open("test1.txt", "w")

file1.writelines("Hello World!")

file1.close()

file2=open("test1.txt", "r")

for line in file2:
    print(line)

file2.close()

import pickle
d = {"stu1": {"Name": "John", "Age": "21", "Id": "28"}, "stu2":{"Name": "Bob", "Age": "18", "Id": "37"}}

with open("myUsers.dat", "wb") as file1:
    pickle.dump(d, file1)
file1.close()

with open("MyUsers.dat", "rb") as file2:
    myDic = pickle.load(file2)
print(myDic["stu1"]["Name"])

i=1
for x in myDic:
    var = "stu"+str(i)
    print(myDic[var]["Name"])
    i+=1
file2.close()