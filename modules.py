from datetime import datetime
now = datetime.now()
entry_date = f"{now.day}-{now.month}-{now.year}"




def menu():
    print("===========MENU===========")
    print("1. Add Expense")
    print("2. View all Expense")
    print("3. view Total Amount")
    print("4. exit")

def Input(chategoriez):
    chategori = int(input(f"Enter chategory no {chategoriez} : "))
    description = input("product name : ")
    amount = float(input("Enter the amount : "))

    chategory = chategoriez[chategori - 1]

    expense = {
        "date": entry_date,
        "category": chategory,
        "description": description,
        "amount": amount
    }
    return expense


