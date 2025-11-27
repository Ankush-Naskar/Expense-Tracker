import os
from modules.comments import menu, total_menu, get_default_config_text
if not os.path.exists("user_settings.py"):
    with open("user_settings.py", "w") as f:
        f.write(get_default_config_text())

from user_settings import addCategories, file_name
from modules.add_expense import Input, save_as_xl
from modules import total_expense


categories = ["Grocery", "Food", "Gadget", "Others"]
categories.extend(addCategories)

try:

    while True:
        menu()
        try:
            choice = int(input("Enter your Choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue


        # Add Expense
        if (choice == 1):
            expense = Input(categories)
            save_as_xl(expense)

            print("Expenses added: ")

        

        # View Expense
        elif(choice == 2):
            excel_file = rf"D:\my projects\price_tracker\{file_name}.xlsx"
            os.startfile(excel_file)


        # View Total Amount
        elif(choice == 3):
            
            total_menu()
            try:
                sub_choice = int(input("Enter your Choice : "))
            except ValueError:
                print("Please enter a valid number.")
                continue

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
                case _:
                    print("Invalid choice....")
                    continue

        # Exit
        elif(choice == 4):
            break

        # Other
        else:
            print("Invalid choice....")
            continue

except Exception as e:
    print("Error occurred: ", e)