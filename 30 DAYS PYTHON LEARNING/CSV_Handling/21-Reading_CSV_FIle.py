#Reading CSV File:

import csv

# Read Entire CSV:
with open("sales_data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# Read with DictReader:
with open("sales_data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Order_ID"],row["Customer_Name"],row["Payment_Type"])


# Total Sales:
total = 0
with open("sales_data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += int(row["Price"]) * int(row["Quantity"])
print("Total Sales = ",total)        


# Filter by City:
mumbai = []
with open("sales_data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["City"] == "Mumbai":
            mumbai.append(row)
print(mumbai)            


