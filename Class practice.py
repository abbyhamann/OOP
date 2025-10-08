class Student:
    def __init__(self):
        self.stuName=""
        self.stuId=""
        self.major=""
        self.job=""
        self.gpa=0.0
        self.courses=[]
    def addStudent(self):
        self.stuName = input("Enter student name")
        self.stuId = input("Enter student ID")
        self.major = input("Enter student major")
        self.job = input("Enter student job")
        self.gpa = input("Enter student gpa")
    def registerStudent(self, cc1):
        self.courses.append(cc1)
    def editStudent(self):
        self.stuName = input("Enter student name")
        self.stuId = input("Enter student ID")
        self.major = input("Enter student major")
        self.job = input("Enter student job")
        self.gpa = input("Enter student name")
    def displayStudent(self):
        print("Name:", self.stuName)
        print("ID:", self.stuId)
        print("Major:", self.major)
        print("Job:", self.job)
        print("GPA:", self.gpa)
        for x in self.courses:
            print("Course Registered:", x.courseName)
class Course:
        def __init__(self):
            self.courseID = ""
            self.courseName = ""
        def addCourse(self):
            self.courseID = input("Enter course ID:")
            self.courseName = input("Enter course name:")
class Faculty:
    def __init__(self):
        self.facName=""
        self.facId=""
        self.facmajor=""
        self.facjob=""
    def addFaculty(self):
        self.facName = input("Enter student name")
        self.facId = input("Enter student ID")
        self.facmajor = input("Enter student major")
        self.facjob = input("Enter student job")
    def editFaculty(self):
        self.facName = input("Enter student name")
        self.facId = input("Enter student ID")
        self.facmajor = input("Enter student major")
        self.facjob = input("Enter student job")
    def displayFaculty(self):
        print("Name:", self.facName)
        print("ID:", self.facID)
        print("Major:", self.facmajor)
        print("Job:", self.facjob)

s1 = Student()
s1.addStudent()
c1 = Course()
c1.addCourse()
s1.registerStudent(c1)
s1.displayStudent()