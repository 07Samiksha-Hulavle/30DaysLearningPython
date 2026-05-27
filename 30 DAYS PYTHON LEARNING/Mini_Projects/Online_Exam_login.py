# Program for online exam system:

reg_no = int(input("Enter Register Number:"))

if(reg_no == 1221):
    print("Go Ahead")

    exam_sub=input("Enter Exam Subject:")

    if(exam_sub.lower() == "python"):
        print("Continue")
        password = int(input("Enter Password:"))

        if(password == 8888):
            print("Login successful! Start your Exam")

        else:
            print("Wrong Password")  

    else:
        print("Subject not available")

else:
    print("Registration Failed")    