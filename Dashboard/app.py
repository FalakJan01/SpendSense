import streamlit as st
from loader import load_transactions
from analytics import calculate_summary
from charts import expense_by_category

st.set_page_config(
    page_title="SpendSense Dashboard",
    page_icon="💰",
    layout="wide"
)

st.title("💰 SpendSense Analytics Dashboard")

st.write("Analyze your income and expenses with interactive visualizations.")

# Load data
df = load_transactions()
summary = calculate_summary(df)

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Income", f"₹{summary['income']:,.2f}")

with col2:
    st.metric("💸 Total Expense", f"₹{summary['expense']:,.2f}")

with col3:
    st.metric("💵 Savings", f"₹{summary['savings']:,.2f}")

with col4:
    st.metric("🧾 Transactions", summary["transactions"])

# Divider
st.divider()

# Transaction Table
st.subheader("📋 Transaction History")
st.dataframe(df, use_container_width=True)

# Divider
st.divider()

# Expense Chart
st.subheader("📊 Expense Analysis")

fig = expense_by_category(df)

st.plotly_chart(fig, use_container_width=True)