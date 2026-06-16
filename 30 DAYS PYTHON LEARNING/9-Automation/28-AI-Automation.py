# Write a Python program that asks the user to
# paste the folder path containing multiple CSV
# files when the program runs. After pressing
# Enter, the program should automatically read
# all CSV files from that folder and combine
# them into one Excel workbook.

# Each CSV file should be placed in a separate
# sheet, and the sheet name must match the
# CSV file name. The program should then save
# the Excel workbook in the same folder where
# the CSV files are located, with the name
# “All_CSV_Converted_Into_Sheets.xlsx”.


import pandas as pd
import os
from pathlib import Path

# ==========================================
# Ask User for Folder Path
# ==========================================

folder_path = input("Paste the folder path containing CSV files: ").strip()

# Check if folder exists
if not os.path.exists(folder_path):
    print("Invalid folder path!")
    exit()

# ==========================================
# Get All CSV Files
# ==========================================

csv_files = list(Path(folder_path).glob("*.csv"))

if len(csv_files) == 0:
    print("No CSV files found in the specified folder.")
    exit()

# ==========================================
# Output Excel File Path
# ==========================================

output_file = os.path.join(
    folder_path,
    "All_CSV_Converted_Into_Sheets.xlsx"
)

# ==========================================
# Convert CSV Files into Excel Sheets
# ==========================================

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    for csv_file in csv_files:

        try:
            # Read CSV
            df = pd.read_csv(csv_file)

            # Sheet Name = CSV File Name
            sheet_name = csv_file.stem[:31]  # Excel sheet limit

            # Write to Excel Sheet
            df.to_excel(
                writer,
                sheet_name=sheet_name,
                index=False
            )

            print(f"Added Sheet: {sheet_name}")

        except Exception as e:
            print(f"Error processing {csv_file.name}: {e}")

# ==========================================
# Success Message
# ==========================================

print("\nConversion Completed Successfully!")
print(f"Excel File Saved At:\n{output_file}")