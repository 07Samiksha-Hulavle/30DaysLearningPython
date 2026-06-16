# 25 - Advance Pandas (Groupby,Filtering,Sorting)

import pandas as pd

# Load Cleaned Employees Data :
df = pd.read_csv(r"C:\Users\admin\OneDrive\Attachments\Desktop\30 DAYS PYTHON LEARNING\9-Pandas\employees.csv") 

print("\n=== Data Loaded ===")
print(df.head())

# Filtering :

# Employees From Mumbai :
df["City"] = df["City"].str.strip().str.title()
mumbai_emp = df[df["City"] == "Mumbai"]
print(mumbai_emp)

# High salary Employees :
high_salary = df[df["Salary"] > 100000]
print(high_salary)

# Multiple Conditions :
df["City"] = df["City"].str.strip().str.title()
mumbai_high = df[(df["City"] == "Mumbai") & (df["Salary"] > 100000)]
print(mumbai_high)

df["City"] = df["City"].str.strip().str.title()
mumbai_pune = df[(df["City"] == "Mumbai") | (df["City"] == "Pune")]
print(mumbai_pune)

# using isin() :
IT_and_Finance = df[df["Department"].isin(["IT","Finance"])]
print(IT_and_Finance)

# Advance Sorting :
# Sort By Salary Descending :
sorted_salary = df.sort_values("Salary",ascending=False)
print(sorted_salary)

# Sort By Department Then Salary :
df["Department"] = df["Department"].str.strip().str.title()
df_sorted_multi = df.sort_values(["Department","Salary"], ascending = [True, False])
print(df_sorted_multi)


# Group By Operations :
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


# Multiple Aggregations :
df["Department"] = df["Department"].str.strip().str.title()
salary_stats =  df.groupby("Department")["Salary"].agg(["min","max","mean","count"])
print("\n=== Salary Stats ===")
print(salary_stats)


# Sort Group By Result :
df["Department"] = df["Department"].str.strip().str.title()
avg_salary_dept = df.groupby("Department")["Salary"].mean()
sorted_avg_salary = avg_salary_dept.sort_values(ascending=False)
print("\n=== Department By AVG Salary ===")
print(sorted_avg_salary)