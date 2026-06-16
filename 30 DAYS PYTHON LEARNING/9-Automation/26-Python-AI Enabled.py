# Practical Use Case 1 – AI Generates Pandas Cleaning Code

# 
# I have a CSV file with employee data file name is day24_Employee_Data.csv
# Columns: EmpID,Name,Department,Salary,Age,City

# Generate Pandas code to:
# 1. Clean names and cities
# 2. Remove duplicates
# 3. Add Experience column
# 

import pandas as pd
from datetime import datetime

# Load CSV file
df = pd.read_csv(
    r"C:\Users\admin\OneDrive\Attachments\Desktop\30 DAYS PYTHON LEARNING\9-Pandas\employees.csv"
)
# 1. Clean Name and City columns
df["Name"] = df["Name"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()

# 2. Remove duplicate rows
df = df.drop_duplicates()

# Alternative: Remove duplicates based on EmpID
# df = df.drop_duplicates(subset=["EmpID"])

# 3. Add Joining_Year column
df["Joining_Year"] = datetime.now().year

# Display cleaned data
print(df.head())

# Save cleaned data to a new CSV file
df.to_csv("employees_cleaned.csv", index=False)