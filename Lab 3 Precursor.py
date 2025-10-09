class Book:
    def __init__(self):
        self.BookID=""
        self.BookName=""
        self.Title=""
        self.Author=""
    def addBook(self):
        self.BookID = input("Enter book ID:")
        self.BookName = input("Enter the book name:")
        self.Title = input("Enter the title:")
        self.Author = input("Enter the author:")
    def editBook(self):
        self.BookID = input("Enter book ID:")
        self.BookName = input("Enter the new book name:")
        self.Title = input("Enter the new title:")
        self.Author = input("Enter the new author:")
    def displayBook(self):
        print("Book ID:", self.BookID)
        print("Book Name:", self.BookName)
        print("Title:", self.Title)
        print("Author:", self.Author)
class User:
    def __init__(self):
        self.UserID=""
        self.UserName=""
        self.BooksBorrowed=[]
    def addUser(self):
        self.UserID = input("Enter user ID:")
        self.UserName = input("Enter user name:")
    def editUser(self):
        self.UserID = input("Enter user ID:")
        self.UserName = input("Enter new user name:")
    def borrowBook(self, b1):
        self.BooksBorrowed.append(b1)
    def displayUser(self):
        print("User ID:", self.UserID)
        print("User Name:", self.UserName)
        print("Books borrowed:", self.BooksBorrowed)


b1 = Book()
b1.addBook()
b2 = Book()
b2.addBook()
b3 = Book()
b3.addBook()
b4 = Book()
b4.addBook()
b5 = Book()
b5.addBook()
u1 = User()
u1.addUser()
u2 = User()
u2.addUser()
u1.borrowBook(b1)
u1.borrowBook(b2)
u2.borrowBook(b3)
u2.borrowBook(b4)
u1.borrowBook(b5)
u1.displayUser()
u2.displayUser()