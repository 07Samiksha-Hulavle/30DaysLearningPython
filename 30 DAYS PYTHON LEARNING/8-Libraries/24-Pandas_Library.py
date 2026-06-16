# Pandas :

import pandas as pd

# 1. Load CSV File :
df = pd.read_csv("employees.csv")
print("=== Raw Data ===")

print(df)   #All Records

print(df.head())   #Starting 5 Records

print(df.head(15))   #Starting 5 Records

print(df.head(-5)) #Skips Last 5 Records

print(df.tail())    #Bottom 5 Records

print(df.tail(10))   #Bottom 10 records


# 2. Basic Information :
print("\nShape :",df.shape)   #Shows Rows & Columns 

print("\nColumns :",df.columns)    #Shows Columns

print(df.info)

# 3.Clean Text Data :
# Clean Employee Names :
df["Name"] = df["Name"].str.strip().str.title()
print(df.head())

# Clean City Names :
df["City"] = df["City"].str.strip().str.title()
print(df.head())

# Clean Department :
df["Department"] = df["Department"].str.strip().str.title()
print(df.head)

print("\n=== Cleaned Text Columns ===")
print(df[["Name","City","Department"]].head())


# 4.Remove Duplicates :
print("Duplicate rows",df.duplicated().sum())
df = df.drop_duplicates()

print(df)


# 5.Filter Data :
#Employees From Mumbai :
df["City"] = df["City"].str.strip().str.title()
mumbai_employees = df[df["City"] == "Mumbai"]
print(mumbai_employees)

print("Employees from Mumbai",mumbai_employees.shape[0])        # Gives Count of Employees From Mumbai


# Employees with Salary > 60000 :
high_salary = df[df["Salary"] > 100000]
print(high_salary)

print("Employee with Salary > 100000 : ",high_salary.shape[0])


# 6.Sort Data :
# Sort By Salary (DESC) :
df_sorted_salary = df.sort_values('Salary',ascending = False)
print(df_sorted_salary.head())

# 6.Add New Columns :
df["salary_category"] = df["Salary"].apply(lambda x:"High" if x >= 100000 else "Medium" if x >= 50000 else "Low")
print(df)

# 8.Group By Operations :
# Avg Salary By Department :
avg_salary_dept = df.groupby("Department")["Salary"].mean()
print(avg_salary_dept.head())

# Total Salary By City :
df["City"] = df["City"].str.title().str.strip()
total_salary_city = df.groupby("City")["Salary"].sum()
print(total_salary_city)

# Employee Count By Department :
df["Department"] = df["Department"].str.title().str.strip()
emp_count_dept = df.groupby("Department")["EmpID"].count()
print(emp_count_dept)

# 9.EXPORT CLEANED DATA -Sort By Salary (Descending) :

df_sorted_salary = df.sort_values("Salary",ascending=False)
df_sorted_salary.to_csv("employee_sort_by_salary.csv",index=False)

df["City"] = df["City"].str.strip().str.title()
mumbai_emp = df[df["City"] == "Mumbai"]
mumbai_emp.to_csv("Mumbai_emp.csv",index=False)