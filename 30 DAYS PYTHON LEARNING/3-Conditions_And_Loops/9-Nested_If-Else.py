#nested if-else:

print("check your Eligibiltiy")

age = int(input("Enter Your Age:"))
if (age >= 18):
    id_no = int(input("Enter your ID No."))
    if (id_no == 7210):
        print("👍 You Can Enter")
    else:
        print("Wrong ID")
else:
    print("You are Underage")        


#Multiple Conditions (AND):

age = int(input("Enter Your Age:"))
licence = input("Do you have licence? ")

if(age>=18 and licence.lower()=="yes"):
    print("Eligible to Drive")
else:
    print("Not Eligible to Drive")    