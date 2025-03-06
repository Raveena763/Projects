import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the app
st.title("Personal Budget Analysis")
st.sidebar.header("Add Your Transactions")

# Initialize session state for storing transactions
if "transactions" not in st.session_state:
    st.session_state.transactions = pd.DataFrame(columns=["Date", "Category", "Amount", "Type"])

# User inputs for transaction details
date = st.sidebar.date_input("Select Date")
category = st.sidebar.selectbox("Select Category", ["Food", "Rent", "Transport", "Entertainment", "Bills", "Shopping", "Other"])
amount = st.sidebar.number_input("Enter Amount", min_value=0.0, format="%.2f")
type_of_transaction = st.sidebar.radio("Transaction Type", ["Income", "Expense"])

# Add transaction to the session state
if st.sidebar.button("Add Transaction"):
    new_transaction = pd.DataFrame([[date, category, amount, type_of_transaction]],
                                   columns=["Date", "Category", "Amount", "Type"])
    st.session_state.transactions = pd.concat([st.session_state.transactions, new_transaction], ignore_index=True)
    st.sidebar.success("Transaction added successfully!")

# Display Transactions
st.subheader("Transaction History")
st.dataframe(st.session_state.transactions)

# Budget Summary
if not st.session_state.transactions.empty:
    income = st.session_state.transactions[st.session_state.transactions["Type"] == "Income"]["Amount"].sum()
    expenses = st.session_state.transactions[st.session_state.transactions["Type"] == "Expense"]["Amount"].sum()
    balance = income - expenses

    st.subheader("Budget Summary")
    st.write(f"Total Income: ₹{income:.2f}")
    st.write(f"Total Expenses: ₹{expenses:.2f}")
    st.write(f"Remaining Balance: ₹{balance:.2f}")

    # Category-wise Expense Analysis
    st.subheader("Expense Breakdown")
    expense_data = st.session_state.transactions[st.session_state.transactions["Type"] == "Expense"]
    if not expense_data.empty:
        category_expense = expense_data.groupby("Category")["Amount"].sum()
        fig, ax = plt.subplots()
        category_expense.plot(kind='bar', ax=ax, color='skyblue')
        ax.set_title("Expenses by Category")
        ax.set_ylabel("Amount (₹)")
        st.pyplot(fig)

    # Monthly Trends
    st.subheader("Monthly Expense Trends")
    st.line_chart(st.session_state.transactions.groupby("Date")["Amount"].sum())

st.write("---")
st.write("Developed using Streamlit")
