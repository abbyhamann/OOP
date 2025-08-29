name = input("Hello, employee. What's your name?")
wages = int(input("Please enter your hourly wages"))
hours = int(input("Please enter the number of hours you worked per day"))
days = int(input("Please enter the number of days you worked"))

total_wages = wages*hours*days

print("The employee's name is", name,)
print("The employee has earned",total_wages, "dollars")