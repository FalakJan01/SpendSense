import plotly.express as px


def expense_by_category(df):

    expense_df = df[df["type"] == "Expense"]

    expense_summary = (
        expense_df
        .groupby("category")["amount"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        expense_summary,
        x="category",
        y="amount",
        title="Expense by Category"
    )

    return fig