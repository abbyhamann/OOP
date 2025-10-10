class Book:
    def __init__(self):
        self.BookID=""
        self.Title=""
        self.AuthorID=""
        self.Publisher=""
        self.YoP=""
        self.AuthorInfo=[]
    def addBook(self):
        self.BookID = input("Enter book ID:")
        self.Title = input("Enter the title:")
        self.AuthorID = input("Enter the author:")
        self.Publisher= input("Enter the publisher:")
        self.YoP= input("Enter the year of publication:")
    def editBook(self):
        self.BookID = input("Enter book ID:")
        self.Title = input("Enter the new title:")
        self.AuthorID = input("Enter the new author:")
        self.Publisher = input("Enter the new publisher:")
        self.YoP = input("Enter the new year of publication:")

    def displayBook(self):
        print("Book ID:", self.BookID)
        print("Title:", self.Title)
        print("Author:", self.AuthorID)
        print("Publisher:", self.Publisher)
        print("Year of Publication:", self.YoP)
class User:
    def __init__(self):
        self.UserID=""
        self.UserName=""
        self.pwd=""
        self.address=""
        self.phone=""
        self.email=""
        self.BooksBorrowed=[]
    def addUser(self):
        self.UserID = input("Enter user ID:")
        self.UserName = input("Enter user name:")
        self.pwd = input("Enter password:")
        self.address = input("Enter address:")
        self.phone = input("Enter phone:")
        self.email = input("Enter email:")
    def editUser(self):
        self.UserID = input("Enter user ID:")
        self.UserName = input("Enter new user name:")
        self.pwd = input("Enter new password:")
        self.address = input("Enter new address:")
        self.phone = input("Enter new phone:")
        self.email = input("Enter new email:")
    def borrowBook(self, b1):
        self.BooksBorrowed.append(b1)
    def displayUser(self):
        print("User ID:", self.UserID)
        print("User Name:", self.UserName)
        print("Password:", self.pwd)
        print("Address:", self.address)
        print("Phone:", self.phone)
        print("Email", self.email)
        print("Books borrowed:", self.BooksBorrowed)
class Author:
    def __init__(self):
        self.AuthorID=""
        self.AuthorName=""
        self.affiliation=""
        self.country=""
        self.phone=""
        self.email=""
        self.booksWritten=[]
    def addAuthor(self):
        self.AuthorID = input("Enter author ID:")
        self.AuthorName = input("Enter author name:")
        self.affiliation = input("Enter affiliation:")
        self.country = input("Enter country:")
        self.phone = input("Enter phone:")
        self.email = input("Enter email:")
    def editAuthor(self):
        self.AuthorID = input("Enter new author ID:")
        self.AuthorName = input("Enter new author name:")
        self.affiliation = input("Enter new affiliation:")
        self.country = input("Enter new country:")
        self.phone = input("Enter new phone:")
        self.email = input("Enter new email:")
    def displayAuthor(self):
        print("Author ID:", self.AuthorID)
        print("Author Name:", self.AuthorName)
        print("Affiliation:", self.affiliation)
        print("Country:", self.country)
        print("Phone:", self.phone)
        print("Email", self.email)
        print("Books written:", self.booksWritten)
    def addBook(self, b1):
        self.booksWritten.append(b1)
b1 = Book()
b1.addBook()
u1 = User()
u1.addUser()
a1 = Author()
a1.addAuthor()
a1.addBook(b1)
u1.borrowBook(b1)

u1.displayUser()
a1.displayAuthor()
b1.displayBook()