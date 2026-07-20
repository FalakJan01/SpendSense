import streamlit as st
from loader import load_transactions

st.set_page_config(
    page_title="SpendSense Dashboard",
    page_icon="💰",
    layout="wide"
)

st.title("💰 SpendSense Analytics Dashboard")

st.write("Analyze your income and expenses with interactive visualizations.")

df = load_transactions()

st.dataframe(df)