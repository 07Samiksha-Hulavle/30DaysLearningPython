# Write a Python program to create a Graphical User Interface (GUI) for dynamic data cleaning automation.
# The GUI should allow the user to:
# 1. Browse and select a raw Excel file as input.
# 2. Display multiple data-cleaning options as checkboxes, including but not limited to:
# 3. Remove duplicate rows
# 4. Remove blank rows
# 5. Remove leading and trailing spaces from text columns only
# 6. Make Title Text style means First letter will be capital of each word for all Text columns
# Browse and select an output folder location where the cleaned file will be saved.
# 1. The GUI should include the following buttons:
# 2. Clean Data: Applies the selected data-cleaning options to the chosen file and exports the
# cleaned Excel file to the selected output location.
# 3. Reset Paths: Clears the selected input file and output location.
# 4. Reset Checkboxes: Unchecks all selected data-cleaning options.
# The program should apply only the selected cleaning operations and work dynamically for any Excel file
# chosen by the user. The cleaned file should be automatically saved in the chosen output folder.


import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

# ==========================================
# Global Variables
# ==========================================

input_file = ""
output_folder = ""

# ==========================================
# Browse Excel File
# ==========================================

def browse_input_file():
    global input_file

    input_file = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel Files", "*.xlsx *.xls")]
    )

    input_path_var.set(input_file)


# ==========================================
# Browse Output Folder
# ==========================================

def browse_output_folder():
    global output_folder

    output_folder = filedialog.askdirectory(
        title="Select Output Folder"
    )

    output_path_var.set(output_folder)


# ==========================================
# Clean Data
# ==========================================

def clean_data():

    global input_file
    global output_folder

    if not input_file:
        messagebox.showerror(
            "Error",
            "Please select an Excel file."
        )
        return

    if not output_folder:
        messagebox.showerror(
            "Error",
            "Please select output folder."
        )
        return

    try:

        df = pd.read_excel(input_file)

        # ----------------------------------
        # Remove Duplicates
        # ----------------------------------
        if duplicate_var.get():
            df = df.drop_duplicates()

        # ----------------------------------
        # Remove Blank Rows
        # ----------------------------------
        if blank_rows_var.get():
            df = df.dropna(how="all")

        # ----------------------------------
        # Text Columns Only
        # ----------------------------------
        text_columns = df.select_dtypes(
            include="object"
        ).columns

        # ----------------------------------
        # Remove Spaces
        # ----------------------------------
        if trim_spaces_var.get():

            for col in text_columns:
                df[col] = (
                    df[col]
                    .astype(str)
                    .str.strip()
                )

        # ----------------------------------
        # Title Case
        # ----------------------------------
        if title_case_var.get():

            for col in text_columns:
                df[col] = (
                    df[col]
                    .astype(str)
                    .str.title()
                )

        # ----------------------------------
        # Save File
        # ----------------------------------

        output_file = os.path.join(
            output_folder,
            "Cleaned_Data.xlsx"
        )

        df.to_excel(
            output_file,
            index=False
        )

        messagebox.showinfo(
            "Success",
            f"File Saved Successfully!\n\n{output_file}"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# ==========================================
# Reset Paths
# ==========================================

def reset_paths():

    global input_file
    global output_folder

    input_file = ""
    output_folder = ""

    input_path_var.set("")
    output_path_var.set("")


# ==========================================
# Reset Checkboxes
# ==========================================

def reset_checkboxes():

    duplicate_var.set(False)
    blank_rows_var.set(False)
    trim_spaces_var.set(False)
    title_case_var.set(False)


# ==========================================
# GUI Window
# ==========================================

root = tk.Tk()

root.title(
    "Dynamic Excel Data Cleaning Automation"
)

root.geometry("700x500")

# ==========================================
# Variables
# ==========================================

input_path_var = tk.StringVar()
output_path_var = tk.StringVar()

duplicate_var = tk.BooleanVar()
blank_rows_var = tk.BooleanVar()
trim_spaces_var = tk.BooleanVar()
title_case_var = tk.BooleanVar()

# ==========================================
# Input File Section
# ==========================================

tk.Label(
    root,
    text="Input Excel File"
).pack(pady=5)

tk.Entry(
    root,
    textvariable=input_path_var,
    width=80
).pack()

tk.Button(
    root,
    text="Browse Excel File",
    command=browse_input_file
).pack(pady=5)

# ==========================================
# Output Folder Section
# ==========================================

tk.Label(
    root,
    text="Output Folder"
).pack(pady=5)

tk.Entry(
    root,
    textvariable=output_path_var,
    width=80
).pack()

tk.Button(
    root,
    text="Browse Output Folder",
    command=browse_output_folder
).pack(pady=5)

# ==========================================
# Cleaning Options
# ==========================================

tk.Label(
    root,
    text="Select Cleaning Options",
    font=("Arial", 12, "bold")
).pack(pady=10)

tk.Checkbutton(
    root,
    text="Remove Duplicate Rows",
    variable=duplicate_var
).pack(anchor="w", padx=50)

tk.Checkbutton(
    root,
    text="Remove Blank Rows",
    variable=blank_rows_var
).pack(anchor="w", padx=50)

tk.Checkbutton(
    root,
    text="Remove Leading & Trailing Spaces",
    variable=trim_spaces_var
).pack(anchor="w", padx=50)

tk.Checkbutton(
    root,
    text="Convert Text Columns To Title Case",
    variable=title_case_var
).pack(anchor="w", padx=50)

# ==========================================
# Buttons
# ==========================================

tk.Button(
    root,
    text="Clean Data",
    bg="lightgreen",
    command=clean_data
).pack(pady=10)

tk.Button(
    root,
    text="Reset Paths",
    command=reset_paths
).pack(pady=5)

tk.Button(
    root,
    text="Reset Checkboxes",
    command=reset_checkboxes
).pack(pady=5)

# ==========================================
# Run GUI
# ==========================================

root.mainloop()

