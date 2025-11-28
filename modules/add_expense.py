import os
import pandas as pd
from user_settings import file_name


def save_as_xl(expense):
    df = pd.DataFrame(expense)
    excel_file = f"{file_name}.xlsx"
    
    try:

        if not os.path.exists(excel_file):
            df.to_excel(excel_file, index=False)
            print(f"Created new expense file: {excel_file} ✅ ")
            return
        
        with pd.ExcelWriter(excel_file, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
            
            book = writer.book
            sheet = book.active
            start_row = sheet.max_row
            sheet_name = sheet.title 
            
            df.to_excel(writer, sheet_name=sheet_name, index=False, header=False, startrow=start_row)
    except PermissionError:
        print("❌ Permission denied: Please CLOSE the Excel file before running this script.")
    except Exception as e:
        print(f"❌ An unexpected error occurred during file saving: {e}")