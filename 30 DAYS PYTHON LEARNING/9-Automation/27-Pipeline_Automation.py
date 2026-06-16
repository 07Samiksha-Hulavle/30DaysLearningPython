# I have a raw sales CSV file with columns like:
# Order_ID,Order_Date,Customer_Name,City,State,Product_Category,
# Product_Name,Quantity,Unit_Price,Discount,Payment_Mode,Sales_
# Channel
# Create a Pandas automation pipeline to:
# 1. Clean customer names, city and state values
# 2. Remove duplicate orders
# 3. Convert numeric columns properly
# 4. Calculate Total_Sales = (Quantity * Unit_Price) - Discount
# 5. Categorize orders as High / Medium / Low value
# 6. Create summary reports:
#  - Total sales by City
#  - Total sales by Product_Category
# 7. Sort summaries in descending order
# 8. Export cleaned data and summaries to CSV files


import pandas as pd

# ==========================================
# 1. Load CSV File
# ==========================================
df = pd.read_csv(r"C:\Users\admin\OneDrive\Attachments\Desktop\30 DAYS PYTHON LEARNING\8-Libraries\raw_sales_data.csv")

# ==========================================
# 2. Clean Customer Name, City, State
# ==========================================

# Remove extra spaces and standardize text
df["Customer_Name"] = df["Customer_Name"].astype(str).str.strip().str.title()

df["City"] = df["City"].astype(str).str.strip().str.title()

df["State"] = df["State"].astype(str).str.strip().str.title()

# ==========================================
# 3. Remove Duplicate Orders
# ==========================================

df = df.drop_duplicates(subset=["Order_ID"])

# ==========================================
# 4. Convert Numeric Columns
# ==========================================

numeric_cols = ["Quantity", "Unit_Price", "Discount"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows with invalid numeric values
df = df.dropna(subset=numeric_cols)

# ==========================================
# 5. Calculate Total Sales
# ==========================================

df["Total_Sales"] = (df["Quantity"] * df["Unit_Price"]) - df["Discount"]

# ==========================================
# 6. Categorize Orders
# ==========================================

def order_category(sales):
    if sales >= 10000:
        return "High"
    elif sales >= 5000:
        return "Medium"
    else:
        return "Low"

df["Order_Value"] = df["Total_Sales"].apply(order_category)

# ==========================================
# 7. Summary Report - City Wise Sales
# ==========================================

city_summary = (
    df.groupby("City")["Total_Sales"]
      .sum()
      .reset_index()
      .sort_values(by="Total_Sales", ascending=False)
)

# ==========================================
# 8. Summary Report - Category Wise Sales
# ==========================================

category_summary = (
    df.groupby("Product_Category")["Total_Sales"]
      .sum()
      .reset_index()
      .sort_values(by="Total_Sales", ascending=False)
)

# ==========================================
# 9. Export Files
# ==========================================

df.to_csv("cleaned_sales_data.csv", index=False)

city_summary.to_csv("city_sales_summary.csv", index=False)

category_summary.to_csv("category_sales_summary.csv", index=False)

print("Data Cleaning Completed Successfully!")
print("Files Generated:")
print("1. cleaned_sales_data.csv")
print("2. city_sales_summary.csv")
print("3. category_sales_summary.csv")