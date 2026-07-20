from datetime import datetime


def add_income(transactions):

    category = input("Income Source: ")
    amount = float(input("Amount: "))

    transaction = {
        "type": "Income",
        "category": category,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    transactions.append(transaction)

    print("Income Added Successfully!")


def add_expense(transactions):

    category = input("Expense Category: ")
    amount = float(input("Amount: "))

    transaction = {
        "type": "Expense",
        "category": category,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    transactions.append(transaction)

    print("Expense Added Successfully!")