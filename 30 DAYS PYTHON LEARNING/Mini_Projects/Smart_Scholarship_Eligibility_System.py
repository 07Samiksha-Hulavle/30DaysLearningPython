# Smart Scholarship Eligibility System:

marks = int(input("Enter marks out of 100 :"))
income = int(input("Enter Family Annual Income :"))
category = input("general / obc / sc / st :")
extra_curricular = input("yes / no :")
backlogs = input("yes / no :")

if(marks < 60 or backlogs == "yes"):
    print("❌ Reject")

elif(marks >= 90 and income < 300000):
    print("🟢 Full Scholarship (100%)")

elif(category.lower() in ["sc","st"] and marks >= 65):
    print("🔵 Special Category Scholarship (70%)")

elif((marks >= 75 and income < 500000) or (extra_curricular == "yes")):
    print("🟡 Partial Scholarship (50%)")

else:
    print("❌ Not Eligible")    
