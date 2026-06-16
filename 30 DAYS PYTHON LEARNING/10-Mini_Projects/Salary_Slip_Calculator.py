# Salary slip Calculator

employee_name = input("Enter Employee Name :")
basic_salary = float(input("Enter Salary :"))
bonus_amount = float(input("Enter Bonus Amount :"))
tax_percentage = float(input("Enter tax % :"))

gross_salary = basic_salary + bonus_amount
tax_amount = (gross_salary * tax_percentage) / 100
net_salary = gross_salary - tax_amount


print("\n---Salary Slip---")
print("Employee Name :",employee_name)
print("Gross Salary :",gross_salary)
print("Tax :",tax_amount)
print("Net Salary :",net_salary)


###################################################

def salary_calculator():
    print("---- Salary Calculator ----")

    name = input("Enter your name: ")
    basic_salary = float(input("Enter basic salary: "))
    bonus = float(input("Enter bonus: "))
    tax_percentage = float(input("Enter tax percentage: "))

    gross_salary = basic_salary + bonus
    tax_amount = gross_salary * (tax_percentage / 100)
    net_salary = gross_salary - tax_amount

    print("\n----- Salary Details -----")
    print(f"Hello {name} 👋")
    print(f"Gross Salary: ₹{gross_salary:.2f}")
    print(f"Tax Amount: ₹{tax_amount:.2f}")
    print(f"Net Salary: ₹{net_salary:.2f}")

# Run the program
salary_calculator()
