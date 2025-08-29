stu_name = input("Enter the student Name:")

course1 = int(input("Enter the grade points for Course1:"))
course2 = int(input("Enter the grade points for Course2"))
course3 = int(input("Enter the grade points for Course3"))
course4 = int(input("Enter the grade points for Course4"))
course5 = int(input("Enter the grade points for Course5"))

total = course1+course2+course3+course4+course5
average = total/5
print("The total is", total)
print("The average is", average)

if average <= 100 and average >= 90:
    print("Grade A")
elif average < 90 and average >=80:
    print("The Grade is B")
elif average <80 and average >=70:
    print("The Grade is C")
elif average <70 and average >=60:
    print("The Grade is D")
else:
    print("The Grade is F")

