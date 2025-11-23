import pandas as pd
from openpyxl import load_workbook
from datetime import datetime

now = datetime.now()
entry_date = f"{now.day}-{now.month}-{now.year}"

def Input(chategories):

    i = 1
    chategoriez = []
    for element in chategories:
        chategoriez.append(f"{i}. {element}")
        i += 1

    chategori = int(input(f"Enter Chategory NO. - {chategoriez} : "))
    description = input("Product Name : ")
    amount = float(input("Enter The Amount : "))

    chategory = chategories[chategori - 1]

    expense = {
        "Date": [entry_date],
        "Category": [chategory],
        "Product":[description],
        "Amount": [amount]
        }

    return expense

# For create data sheet
def save_as_xl(expense):
    df = pd.DataFrame(expense)

    excel_file = r"D:\my projects\price_tracker\expenses.xlsx"
    try:
        book = load_workbook(excel_file)
        with pd.ExcelWriter(excel_file, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
            df.to_excel(writer, index=False, header=False, startrow=book.active.max_row)
    except PermissionError:
        print("Permission denied: Close the Excel file before running this script.")
    except FileNotFoundError:
        df.to_excel(excel_file, index=False)

