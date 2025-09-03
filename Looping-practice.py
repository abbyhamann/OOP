p = int(input("Please print  the principal loan amount"))
R = int(input("Please enter the rate of interest"))
n = int(input("Please enter the duration of the loan"))

r = R/(12*100)
emi = p * r * ((1 + r) ** n)/ ((1+r)**n - 1)

for i in range(1,n):
    p = p-emi
    print("EMI:", emi)
    print("Balance:", p)

