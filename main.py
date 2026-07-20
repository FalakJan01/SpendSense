from storage import load_data, save_data
from finance import add_income, add_expense
from reports import view_transactions, monthly_report
from export import export_csv

transactions = load_data()

while True:

    print("\n====== PERSONAL FINANCE TRACKER ======")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Monthly Report")
    print("5. Export CSV")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_income(transactions)
        save_data(transactions)

    elif choice == "2":

        add_expense(transactions)
        save_data(transactions)

    elif choice == "3":

        view_transactions(transactions)

    elif choice == "4":

        monthly_report(transactions)

    elif choice == "5":

        export_csv(transactions)

    elif choice == "6":

        print("Thank you for using Personal Finance Tracker.")
        break

    else:

        print("Invalid Choice!")