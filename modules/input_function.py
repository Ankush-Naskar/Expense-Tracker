from datetime import datetime
from modules import total_expense
from modules.comments import total_menu


# === MODULE FOR INPUT DATA  ===
def input_for_add(categories):

    i = 1
    category_list = []
    for element in categories:
        category_list.append(f"{i}. {element}")
        i += 1

    #  === INPUT CATEGORY ===
    try:
        category_index = int(input(f"Enter category NO. : {category_list} : "))
        if category_index < 1 or category_index > len(categories):
            print("\n⚠️  Category number out of range.")
            return None
    except ValueError:
        print("\n⚠️  Please enter a valid category number.")
        return None
    
    # === INPUT PRODUCT NAME ===
    product_name = input("Product Name : ")

    # === INPUT AMOUNT ===
    try:
        amount = float(input("Enter the amount : "))
    except ValueError:
        print("\n⚠️  Please enter a valid numeric amount. ")
        return None
    
    print("Expenses added successfully ✅")
    
    # === Date ====
    entry_date = datetime.now().strftime("%d-%m-%Y")

    # === category ====
    category = categories[category_index - 1]

    # === DATA LIST === 
    expense = {
        "Date": [entry_date],
        "Category": [category],
        "Product":[product_name],
        "Amount": [amount]
        }

    return expense


# ==== MODULE FOR INPUT TOTAL DATA ====
def input_for_total_amount():
    while True:
        total_menu()
        try:
            sub_choice = int(input("Enter your Choice : "))
        except ValueError:
            print("⚠️  Please enter a valid number.")
            break

        match sub_choice:
            case 1:
                total_expense.get_todays_expense() 
            case 2:
                total_expense.get_daily_summary()
            case 3:
                total_expense.get_last_8_weeks_summary()
            case 4:
                total_expense.get_monthly_summary()
            case 5:
                total_expense.get_yearly_summary()
            case 6:
                break
            case _:
                print("⚠️  Invalid choice .... ")
                break