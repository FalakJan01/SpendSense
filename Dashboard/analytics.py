def calculate_summary(df):

    income = df[df["type"] == "Income"]["amount"].sum()

    expense = df[df["type"] == "Expense"]["amount"].sum()

    savings = income - expense

    transactions = len(df)

    return {
        "income": income,
        "expense": expense,
        "savings": savings,
        "transactions": transactions
    }