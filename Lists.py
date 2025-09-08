myList = ["Red", "Green", "Blue"]
print(myList)

myList[1] = "Orange"
print(myList)

myList.append(10)
print(myList[0])

x = input("Enter your name:")
myList.append(x)
print(myList)

myList.remove(myList[1])
print(myList)

myList.pop()
print(myList)

for i in range(0, len(myList)):
    print(myList[i])