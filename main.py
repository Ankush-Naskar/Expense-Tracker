import os
from modules.comments import menu, total_menu, get_default_config_text
if not os.path.exists("user_settings.py"):
    with open("user_settings.py", "w") as f:
        f.write(get_default_config_text())

from user_settings import addCategories, file_name
from modules.add_expense import save_as_xl
from modules.input_function import input_for_add, input_for_total_amount


categories = ["Grocery", "Food", "Gadget", "Others"]
categories.extend(addCategories)

try:

    while True:
        menu()
        try:
            choice = int(input("Enter your Choice: "))
        except ValueError:
            print("⚠️  Please enter a valid number.")
            continue

        match choice:

            # =====  1. Add Expense  =====
            case 1:
                while True:
                    expense = input_for_add(categories)
                    save_as_xl(expense)
                    again_run = input("\nAdd another expense? (y/n): ").lower()
                    if not again_run == "y" :
                        break

            # =====  2. View Expense  =====
            case 2:
                excel_file = f"{file_name}.xlsx"
                os.startfile(excel_file)

            # =====  3. View Total Amount  =====
            case 3:
                # total_menu()
                input_for_total_amount()

            # =====  4. Exit  =====
            case 4:
                break

            # =====  Other  =====
            case _:
                print("⚠️  Invalid choice....")
                continue

except Exception as e:
    print("❌ Error occurred: ", e)