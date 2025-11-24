import os
from user_settings import addCategories
from modules.comments import menu, total_menu
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
            excel_file = r"D:\my projects\price_tracker\expenses.xlsx"
            os.startfile(excel_file)


        # View Total Amount
        elif(choice == 3):
            
            total_menu()
            try:
                sub_choice = int(input("Enter your Choice : "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if sub_choice == 1:
                total_expense.get_todays_expense()
            elif sub_choice == 2:
                total_expense.get_daily_summary()
            elif sub_choice == 3:
                total_expense.get_monthly_summary()
            elif sub_choice == 4:
                total_expense.get_yearly_summary()
            else:
                
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