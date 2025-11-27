
# MENU
def menu():
    print("===========MENU===========")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Amount")
    print("4. Exit")

def total_menu():
    print("===========MENU===========")
    print("1. Today")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly")
    print("5. Yearly")

def get_default_config_text():
    return ('addCategories = ["cloathes", "utilities", "entertainment"]\nfile_name = "expenses"')