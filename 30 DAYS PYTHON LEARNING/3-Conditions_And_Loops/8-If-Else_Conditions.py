#if-else:

#eligible to vote or not:
age = 28

if(age>=18):
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")    


#discount checker:
amount =15000

if (amount >= 10000):
    print("You Get a Discount")
else:
    print("No Discount")    


#if-elif-else:
#marks:
marks = 45

if (marks >= 90):
    print("Grade A")
elif (marks >= 75):
    print("Grade B")
elif(marks >= 35): 
    print("Grade C")  
else:
    print("Fail")
     

#sales performance:
sales = 100000

if (sales >= 100000):
    print("High Performer")
elif (sales >= 50000):
    print("Medium Performer")
else:
    print("Low Performer")        


#string comparison example:
city = "Delhi"

if(city.lower() == "delhi"):
    print("City Matched")
else:
    print("City Not Matched")


#password:
password = "sam@123"

if (password == "sam@123"):
    print("Sucessful Login")
else:
    print("Wrong Password")


#email validation:
email = "samu@gmail.com"

if('@' in email and '.' in email):
    print("Correct email")
else:
    print("Wrong email")    


# advanced missing data check:
data = "hdsjjs"

if (data == ""):
    print("Data is Missing")
else:
    print("Data is Not Missing")    

