def view_transactions(transactions):

    if not transactions:
        print("No Transactions Found.")
        return

    for item in transactions:

        print("----------------------------")
        print("Type:", item["type"])
        print("Category:", item["category"])
        print("Amount:", item["amount"])
        print("Date:", item["date"])


def monthly_report(transactions):

    income = 0
    expense = 0

    for item in transactions:

        if item["type"] == "Income":
            income += item["amount"]

        else:
            expense += item["amount"]

    savings = income - expense

    print("\nMonthly Report")
    print("----------------------")
    print("Total Income :", income)
    print("Total Expense:", expense)
    print("Savings      :", savings)