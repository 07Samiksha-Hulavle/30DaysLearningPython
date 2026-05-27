#whil lopp:

#basic 
i = 1
while (i <= 5):
    print(i)
    i += 1

#countdown    
n = 5
while n>0:
    print(n)
    n -= 1

# ask user until valid input:
num = ""
while not num.isnumeric():
    num = input("Enter any value:")
    print("Please enter only number")
print("Number Accepted:",num) 

#loop through list using while:

items = ["Apple","Banana","Grapes"]
i = 0
while i < len(items):
    print(items[i])
    i += 1

#using break:
n = 1
while n <= 10:
    if n == 5:
        break
    print(n)
    n += 1


n = 1
while n <= 10:
    print(n)
    if n == 5:
        break
    n += 1    

 #using continue:
# (odd) 
y = 0
while y < 10:
    y += 1
    if y % 2 == 0:
        continue
    print(y)

# (Even)
y = 0
while y < 10:
    y += 1
    if y % 2 == 1:
        continue
    print(y)

#password system (advanced):
password = ""
attempts = 0

while password != "admin@123" and attempts < 3:
    password = input("Enter Password:")
    attempts += 1
    if password == "admin@123":
        print("Login Successful")
    else:
        print("Wrong Password Try Again Attempt Count :",attempts)
    if attempts == 3:
        print("3 Attempt Expired")        