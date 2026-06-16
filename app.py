import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Page Title
st.title("💰 Personal Finance Tracker Dashboard")

# Load Data
df = pd.read_csv("expenses.csv")

# Show Dataset
st.subheader("Expense Records")
st.dataframe(df)

# Total Expenses
total_expense = df["Amount"].sum()

st.subheader("Total Expenses")
st.success(f"₹ {total_expense}")

# Monthly Income Input
income = st.number_input(
    "Enter Monthly Income",
    min_value=0,
    value=10000
)

# Savings Calculation
savings = income - total_expense

st.subheader("Savings")
st.info(f"₹ {savings}")

# Category Wise Spending
st.subheader("Expenses by Category")

category_expense = df.groupby("Category")["Amount"].sum()

fig1, ax1 = plt.subplots()

ax1.pie(
    category_expense,
    labels=category_expense.index,
    autopct="%1.1f%%"
)

st.pyplot(fig1)

# Bar Chart
st.subheader("Category Spending Comparison")

fig2, ax2 = plt.subplots()

ax2.bar(
    category_expense.index,
    category_expense.values
)

ax2.set_ylabel("Amount")

st.pyplot(fig2)