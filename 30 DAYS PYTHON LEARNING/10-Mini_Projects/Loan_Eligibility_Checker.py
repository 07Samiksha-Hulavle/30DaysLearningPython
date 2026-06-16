print("------Loan Eligibility Checker------")

age = int(input("Enter your age:"))
salary = int(input("Enter your monthly salary:"))
credit_score = int(input("Enter your credit score:"))
emp_type = input('Enter "salaried" or "self-employed"')
exist_loan = input("Enter yes / no:")
experience = int(input("Enter years of work experience:"))

if(age>=21 and age<=60 and salary>=25000):
    
    #High Approval:
    if(credit_score>750 and experience>=3 and exist_loan.lower()=="no"):
        print("✅ Loan Aproved\nLow Risk\nLoan Type: Premium Loan")
        

    #Medium Approval:
    elif(credit_score>=650 and credit_score<=750 and experience>=2 and salary>50000 and exist_loan.lower()=="no"):
        print("✅ Loan Approved\nMedium Risk\nType: Standard Loan")

    #Low Approval:
    elif(credit_score>=550 and credit_score<=650 and exist_loan.lower()=="yes"):
         print("✅ Loan Approved with Conditions\nHigh Risk\nLoan Type: Basic Loan")
       
       
    else:   
        print("❌Loan Rejected")

else:
    print("❌Not Eligible for Loan")        

