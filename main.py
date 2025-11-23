import os
from user import addChategories
from modules.coments import menu, total_menu
from modules.add_expense import Input, save_as_xl


chategories = ["Grocery", "Food", "Gadget", "Others"]
chategories.extend(addChategories)


try:
    while True:
        menu()
        choice = int(input("Enter your Choice : "))

    # Add Expense
        if choice==1:
            expense = Input(chategories)
            save_as_xl(expense)

            print("Expenses added succesfully")

        

    # View Expense
        elif(choice == 2):
            excel_file = r"D:\my projects\price_tracker\expenses.xlsx"
            os.startfile(excel_file)


    # View Total Amount
        elif(choice == 3):
            from modules import total_expense
           
            total_menu()
            choice = int(input("Enter your Choice : "))

            if choice == 1:
                total_expense.get_todays_expense()
            elif choice == 2:
                total_expense.get_daily_summary()
            elif choice == 3:
                total_expense.get_monthly_summary()
            elif choice == 4:
                total_expense.get_yearly_summary()
            else:
                
                print("Invalid choice....")

    # Exit
        elif(choice == 4):
            break

    # Other
        else:
            print("Invalid choice....")

except Exception as e:
    print("error ocurs\n", e)