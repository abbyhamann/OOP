class Person:
    def __init__(self, nn, dd, gg):
        self.pname = nn
        self.dob = dd
        self.gender= gg
    def display(self):
        print("Person Name:", self.pname)
        print("Person DOB:", self.dob)
        print("Person Gender:", self.gender)
        return ""
class Student(Person):
    def __init__(self, x, y, z, a, b):
        Person.__init__(self, x, y, z)
        self.dept=a
        self.id=b
    def display(self):
        print(Person.display(self))
        print("Student Department:",  self.dept)
        print("Student ID:", self.id)

class Faculty(Person):
    def __init__(self, x, y, z, a, b):
        Person.__init__(self, x, y, z)
        self.salary=a
        self.position=b
    def display(self):
        print(Person.display(self))
        print("Faculty Salary:", self.salary)
        print("Faculty Position:", self.position)

s1=Student("Jim", "2004", "Male", "CS", "123")
s1.display()
f1 = Faculty("Justus", "1992", "Male", "$$$", "Professor")
f1.display()