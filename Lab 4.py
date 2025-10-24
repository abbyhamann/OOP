class Customer:
    def __init__(self):
        self.cid=""
        self.acc_no=""
        self.cname=""
        self.phone=""
        self.email=""
        self.Balance=0.0
        self.credit_card=[]
        self.debit_card=""
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
    def add_card(self, n):
        card_type=input("Please enter the card type (CC or DC)")
        if card_type == "CC":
            self.credit_card.append(n)
        elif card_type == "DC":
            self.debit_card=n
    def debit_from(self, n):
        self.Balance=self.Balance-float(n)
        if self.Balance < 0:
            self.Balance = self.Balance + float(n)
            print("ERROR. Balance too low for withdrawal")
    def credit_to(self, m):
        self.Balance = self.Balance + float(m)
    def display_all(self):
        print("Customer ID:", self.cid)
        print("Account Number:", self.acc_no)
        print("Customer Name:", self.cname)
        print("Phone Number:", self.phone)
        print("Email:", self.email)
        print("Balance:", self.Balance)
class Card:
    def __init__(self):
        self.type=""
        self.card_no=""
        self.cvv=""
        self.expir_date=""
        self.balance=0.0
    def addCard(self):
        self.type=input("Please enter the type (DC or CC)")
        self.card_no=input("Please enter the card number")
        self.cvv=input("Please enter the CVV")
        self.expir_date=input("Please enter the expiration date")
        self.balance=float(input("Please enter the balance"))
    def editCard(self):
        self.type = input("Please enter the new type (DC or CC)")
        self.card_no = input("Please enter the new card number")
        self.cvv = input("Please enter the new CVV")
        self.expir_date = input("Please enter the new expiration date")
        self.balance = float(input("Please enter the new balance"))
    def displayCard(self):
        print("Type:", self.type)
        print("Card Number:", self.card_no)
        print("CVV:", self.cvv)
        print("Expiration Date:", self.expir_date)
        print("Balance:", self.balance)
import pickle

c1=Customer()
c1.add_customer()
c2=Customer()
c2.add_customer()

m1=Card()
m1.addCard()
m2 = Card()
m2.addCard()

c1.debit_from(input("Please enter the amount you'd like to withdraw"))
c2.credit_to(input("Please enter the amount you'd like to deposit"))

c1.add_card(m1)


c1.display_all()
c2.display_all()

m1.displayCard()
m2.displayCard()

with open("Lab4.dat", "wb") as file1:
    pickle.dump(c1, file1)
    pickle.dump(c2, file1)
    pickle.dump(m1, file1)
    pickle.dump(m2, file1)
file1.close()