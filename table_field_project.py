import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import filedialog

def show_table(data):
    for row in table.get_children():
        table.delete(row)

    for row_data in data:
        table.insert("", "end", values=row_data)

def calculate_total(data):
    total = 0.0
    for row_data in data:
        total += row_data[2]
    return round(total, 2)

def calculate_category_total(category_name, data):
    total = 0.0
    for row_data in data:
        if row_data[0] == category_name:
            total += row_data[2]
    return round(total, 2)

def calculate_and_update_total(data):
    total = calculate_total(data)
    total_label.config(text=f"Total: {total}")

def calculate_and_update_category_total(category_name, data):
    total = calculate_category_total(category_name, data)
    category_total_labels[category_name].config(text=f"Total {category_name}: {total}")

def create_category_buttons_frame():
    category_buttons_frame2 = tk.Frame(root, bg="#082740")
    category_buttons_frame2.pack()

    categories2 = ["GRÂU COMUN de toamnă", "PORUMB", "MAZĂRE BOABE", "FLOAREA SOARELUI", "GRÂU COMUN de primăvară"]

    for idx, category_name in enumerate(categories2):
        button = tk.Button(category_buttons_frame2, text=category_name, command=lambda name=category_name: calculate_and_update_category_total(name, data), font=("Arial", 12, "bold"), bg="#FFD700", fg="#000000")
        button.grid(row=0, column=idx, padx=5, pady=15)

        category_total_labels[category_name] = tk.Label(category_buttons_frame2, text=f"Total {category_name}: 0.0", bg="#082740", fg="#FFFFFF")
        category_total_labels[category_name].grid(row=1, column=idx, padx=5, pady=15)

def import_data_from_excel(file_path):
    global data
    try:
        df = pd.read_excel(file_path)
        data = df.values.tolist()
        show_table(data)
        calculate_and_update_total(data)
        for category_name in category_total_labels:
            calculate_and_update_category_total(category_name, data)
        print("Data imported successfully.")
    except Exception as e:
        print(f"Error importing data from Excel: {e}")

    root.deiconify()  # Show the root window after importing data

def clear_table():
    global data
    data = []
    show_table(data)
    calculate_and_update_total(data)
    for category_name in category_total_labels:
        calculate_and_update_category_total(category_name, data)
    print("Table cleared successfully.")

# Dati di esempio presi dal documento Excel
data = [
    ["GRÂU COMUN de toamnă", 101, 1.45],
    ["GRÂU COMUN de toamnă", 101, 9.00],
    ["GRÂU COMUN de toamnă", 101, 1.50],
    ["GRÂU COMUN de toamnă", 101, 5.90],
    ["PORUMB", 108, 1.32],
    ["FLOAREA SOARELUI", 201, 5.10],
    ["GRÂU COMUN de primăvară", 1010, 5.45],
    ["FLOAREA SOARELUI", 201, 3.65],
    ["GRÂU COMUN de toamnă", 101, 0.40],
    ["GRÂU COMUN de toamnă", 101, 1.75],
    ["GRÂU COMUN de toamnă", 101, 7.28],
    ["FLOAREA SOARELUI", 201, 18.95],
    ["GRÂU COMUN de primăvară", 1010, 1.06],
    ["FLOAREA SOARELUI", 201, 2.23],
    ["GRÂU COMUN de toamnă", 101, 2.88],
    ["GRÂU COMUN de toamnă", 101, 2.37],
    ["MAZĂRE BOABE", 1511, 11.50],
    ["GRÂU COMUN de toamnă", 101, 3.17],
    ["GRÂU COMUN de toamnă", 101, 4.20],
    ["FLOAREA SOARELUI", 201, 3.43],
    ["GRÂU COMUN de toamnă", 101, 4.25],
    ["GRÂU COMUN de toamnă", 101, 1.02],
    ["GRÂU COMUN de primăvară", 1010, 2.20],
    ["FLOAREA SOARELUI", 201, 0.51],
    ["GRÂU COMUN de toamnă", 101, 9.46],
    ["GRÂU COMUN de toamnă", 101, 8.33],
    ["GRÂU COMUN de toamnă", 101, 1.77],
    ["FLOAREA SOARELUI", 201, 0.55],
    ["PORUMB", 108, 1.30],
    ["GRÂU COMUN de toamnă", 101, 1.05],
    ["GRÂU COMUN de toamnă", 101, 9.96],
    ["GRÂU COMUN de toamnă", 101, 6.14],
    ["PORUMB", 108, 1.12],
    ["FLOAREA SOARELUI", 201, 0.69],
    ["PORUMB", 108, 0.30],
    ["PORUMB", 108, 1.00],
    ["MAZĂRE BOABE", 1511, 1.09],
    ["MAZĂRE BOABE", 1511, 2.00],
    ["MAZĂRE BOABE", 1511, 1.00],
    ["GRÂU COMUN de toamnă", 101, 0.52],
    ["MAZĂRE BOABE", 1511, 1.20],
    ["GRÂU COMUN de toamnă", 101, 1.37],
    ["GRÂU COMUN de primăvară", 1010, 1.00],
    ["GRÂU COMUN de toamnă", 101, 0.35],
    ["GRÂU COMUN de toamnă", 101, 0.50],
    ["GRÂU COMUN de toamnă", 101, 0.36],
    ["GRÂU COMUN de toamnă", 101, 0.65],
    ["FLOAREA SOARELUI", 201, 0.43],
    ["GRÂU COMUN de toamnă", 101, 0.35],
    ["MAZĂRE BOABE", 1511, 0.30],
    ["MAZĂRE BOABE", 1511, 0.47],
    ["FLOAREA SOARELUI", 201, 2.06],
    ["FLOAREA SOARELUI", 201, 1.68],
    ["FLOAREA SOARELUI", 201, 0.54],
    ["FLOAREA SOARELUI", 201, 0.40],
    ["FLOAREA SOARELUI", 201, 0.63],
    ["FLOAREA SOARELUI", 201, 0.37],
    ["FLOAREA SOARELUI", 201, 0.42],
    ["FLOAREA SOARELUI", 201, 0.68],
    ["FLOAREA SOARELUI", 201, 0.42],
    ["FLOAREA SOARELUI", 201, 0.74],
    ["FLOAREA SOARELUI", 201, 0.75],
    ["FLOAREA SOARELUI", 201, 0.32],
    ["FLOAREA SOARELUI", 201, 1.16],
    ["FLOAREA SOARELUI", 201, 0.47],
    ["FLOAREA SOARELUI", 201, 0.80],
    ["FLOAREA SOARELUI", 201, 0.62],
    ["FLOAREA SOARELUI", 201, 0.46],
    ["GRÂU COMUN de toamnă", 101, 0.82],
    ["GRÂU COMUN de toamnă", 101, 0.36],
    ["FLOAREA SOARELUI", 201, 0.50],
    ["GRÂU COMUN de toamnă", 101, 0.30],
    ["FLOAREA SOARELUI", 201, 0.60],
    ["MAZĂRE BOABE", 1511, 1.01],
    ["GRÂU COMUN de toamnă", 101, 0.93],
    ["PORUMB", 108, 0.50],
    ["GRÂU COMUN de toamnă", 101, 0.68],
    ["FLOAREA SOARELUI", 201, 0.50],
    ["PORUMB", 108, 0.50],
    ["GRÂU COMUN de toamnă", 101, 0.50],
    ["GRÂU COMUN de toamnă", 101, 0.40],
    ["GRÂU COMUN de toamnă", 101, 1.00],
    ["FLOAREA SOARELUI", 201, 0.40],
    ["FLOAREA SOARELUI", 201, 0.49],
    ["GRÂU COMUN de toamnă", 101, 0.47],
    ["PORUMB", 108, 1.05],
    ["GRÂU COMUN de toamnă", 101, 2.50],
    ["PORUMB", 108, 0.35],
    ["PORUMB", 108, 0.30],
    ["GRÂU COMUN de toamnă", 101, 0.37],
    ["FLOAREA SOARELUI", 201, 0.44],
    ["GRÂU COMUN de toamnă", 101, 0.62],
    ["FLOAREA SOARELUI", 201, 1.50],
    ["FLOAREA SOARELUI", 201, 0.50],
    ["MAZĂRE BOABE", 1511, 0.35],
    ["FLOAREA SOARELUI", 201, 0.60],
    ["FLOAREA SOARELUI", 201, 0.45],
    ["GRÂU COMUN de toamnă", 101, 0.64],
    ["FLOAREA SOARELUI", 201, 0.99],
    ["FLOAREA SOARELUI", 201, 0.30],
]



root = tk.Tk()
root.title("Apia Data")
root.geometry("800x400")
root.configure(background="#082740")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

table = ttk.Treeview(frame)

table["columns"] = ("Column 1", "Column 2", "Column 3")
table["show"] = "headings"

table.heading("Column 1", text="Column 1")
table.heading("Column 2", text="Column 2")
table.heading("Column 3", text="Column 3")

table.column("Column 1", width=200)
table.column("Column 2", width=200)
table.column("Column 3", width=200)

table.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame, orient="vertical", command=table.yview)
scrollbar.pack(side="right", fill="y")

table.configure(yscrollcommand=scrollbar.set)

show_table(data)

calculate_button = tk.Button(root, text="Calculate the Total", command=lambda: calculate_and_update_total(data))
calculate_button.pack(pady=5)

total_label = tk.Label(root, text="Total: 0.0")
total_label.pack()

category_buttons_frame = tk.Frame(root)
category_buttons_frame.pack()

category_total_labels = {}

create_category_buttons_frame()

# Function to handle the "Import Data" button click event
def import_data_button_click():
    from tkinter import filedialog

    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        root.withdraw()  # Hide the root window while importing data
        import_data_from_excel(file_path)

# Create a button to import data from an Excel file
import_button = tk.Button(root, text="Import Data", command=import_data_button_click)
import_button.pack(pady=5)

# Function to handle the "Clear Table" button click event
def clear_table_button_click():
    clear_table()

# Create a button to clear the table
clear_button = tk.Button(root, text="Clear Table", command=clear_table_button_click)
clear_button.pack(pady=5)

root.mainloop()