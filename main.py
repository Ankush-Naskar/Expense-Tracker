from user import addChategories
from modules import menu, Input

# expenses list
expensesList = []

# chategory list
chategoriez = []
chategories = ["Grocery", "Food", "Gadget", "Others"]
chategories.extend(addChategories)
i = 1
for element in chategories:
    chategoriez.append(f"{i}. {element}")
    i += 1


try:
    while True:

        menu()
        choice = int(input("Enter your Choice : "))

    # Add Expense
        if choice==1:

            expensesList.append(Input(chategoriez))
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

except Exception as e:
    print("error ocurs\n", e)