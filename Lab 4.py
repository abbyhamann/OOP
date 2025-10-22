class Customer:
    def __init__(self):
        self.cid=""
        self.acc_no=""
        self.cname=""
        self.phone=""
        self.email=""
        self.Balance=0.0
    def add_customer(self):
        self.cid=input("Enter the customer ID")
        self.acc_no=input("Enter the account number")
        self.cname=input("Enter the customer name")
        self.phone=input("Enter the phone number")
        self.email=input("Enter the email")
        self.Balance=float(input("Enter the account balance"))
    def edit_customer(self):
        self.cid=input("Enter the new customer ID")
        self.acc_no=input("Enter the new account number")
        self.cname=input("Enter the new customer name")
        self.phone=input("Enter the new phone number")
        self.email=input("Enter the new email")
        self.Balance=float(input("Enter the new account balance"))
    def debit_from(self, n):
        self.Balance=self.Balance-float(n)
    def credit_to(self, m):
        self.Balance = self.Balance + float(m)
    def display_all(self):
        print("Customer ID:", self.cid)
        print("Account Number:", self.acc_no)
        print("Customer Name:", self.cname)
        print("Phone Number:", self.phone)
        print("Email:", self.email)
        print("Balance:", self.Balance)
c1=Customer()
c1.add_customer()
c2=Customer()
c2.add_customer()
c1.debit_from(100)
c2.credit_to(100)
c1.display_all()
c2.display_all()