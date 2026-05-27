# Clean Customer Names (strip + title):

import csv

cleaned_rows =[]
with open("raw_data.csv","r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        row["Customer_Name"] = row["Customer_Name"].strip().title()
        cleaned_rows.append(row)

# print(cleaned_rows)    

with open ("cleaned_customer.csv","w",newline = "")   as f:
    writer = csv.DictWriter(f,fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_rows) 

print("Cleaned CSV Created : cleaned_customer.csv")



# Filter Only Mumbai Sales And Write It In New File:
import csv

mumbai_sales = []
with open("sales_data.csv","r") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        if row["City"].strip().lower() == "mumbai":
            mumbai_sales.append(row)

    with open("mumbai_sales.csv","w",newline = "") as f:
        writer = csv.DictWriter(f,fieldnames=reader.fieldnames) 
        writer.writeheader()
        writer.writerows(mumbai_sales)

print("New File Created : mumbai_sales.csv")    


# Correct City spelling And Save New File:
import csv

mapping = {
    "mombai" : "Mumbai",
    "delhii" : "Delhi",
    "pune" : "Pune"
}

output =[]
with open("sales_data.csv") as f:
    reader = csv.DictReader(f)

    for row in reader:
        c=row["City"].strip().title()
        row["City"]=mapping.get(c.lower(),c)
        output.append(row)
    
    with open("cleaned_city.csv","w",newline="") as f:
            writer = csv.DictWriter(f,fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(output)

print("New File Created : cleaned_city.csv")            








