# Input and Typecasting:

name = input("Enter your Name:")
print("Welcome",name)


age = int(input("Enter your age:"))
print("Your age is",age)
print(type(age))

temp = float(input("enter Todays Temperature :"))
print(type(temp))

#Convert Number to string:
sales = 50000
text = "Total sales:" + str(sales)
print(text)


#Total Sales Calculator:
product = input("Enter product name")
quantity = int(input("Enter quantity solid"))
price_per_unit = float(input("Enter price per unit"))

total_sales = quantity * price_per_unit

print("product:",product)
print("Total Sales Amount:",total_sales)



fnum = int(input("Enter first number:"))
snum = int(input("Enter second number:"))

sum = fnum+snum
print(sum)