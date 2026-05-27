#program for access in the meeting:

security_code = int(input("Enter Security Code:"))

if(security_code == 5566):
    emp_department = input("Enter Employee Department:")
    
    if(emp_department.lower() == "finance"):
        access_level = int(input("Enter Access Level:"))

        if(access_level >= 5):
            print("Access Granted:Welcome to the meeting room")

        else:
            print("Insufficient access level")

    else:
        print("Access denied:Department not allowed")

else:
    print("Invalid Security code")        






