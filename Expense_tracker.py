
expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append({"name": name, "amount": amount})
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses yet.")
    else:
        for expense in expenses:
            print(expense["name"], "-", expense["amount"])

def total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print("Total expenses:", total)

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
