expensesList = []

while True:
    print("=====MENU=====")
    print("1. Add Expense")
    print("2. View Total Expense")
    print("3. view Total Amount")
    print("4. exit")

    choice = int(input("Enter your Choice : "))

# Add Expense

    if choice==1:
        date= input("date of expense")
        chategory = input("Enter chategory : ")
        description = input("product name : ")
        amount = float(input("Enter the amount : "))

        expense = {
            "date": date,
            "category": chategory,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("Expenses added succesfully")

# View Total Expense
    elif(choice == 2):
        if len(expensesList)==0:
            print("no expenses added")
        else:
            print("=== your expenses ===")
            count= 1
            for eachExpense in expensesList:
                print(f"{count}. {eachExpense['date']}, {eachExpense['category']}, {eachExpense['description']}, {eachExpense['amount']}")

#  view Total Amount
    elif(choice == 3):
        total = 0
        for eachExpense in expensesList:
            total += eachExpense["amount"]
        print(total)

# Exit
    elif(choice == 4):
        break

    else:
        print("invalid choice")