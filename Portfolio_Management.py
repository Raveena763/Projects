import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the app
st.title("Portfolio Management System")
st.sidebar.header("Upload Portfolio Data")

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Portfolio Data Preview")
    st.write(df.head())
    
    # Portfolio Summary
    st.subheader("Portfolio Summary")
    total_investment = df['Investment_Amount'].sum()
    total_returns = df['Current_Value'].sum() - total_investment
    roi = (total_returns / total_investment) * 100
    
    st.write(f"Total Investment: ₹{total_investment:.2f}")
    st.write(f"Total Returns: ₹{total_returns:.2f}")
    st.write(f"Return on Investment (ROI): {roi:.2f}%")
    
    # Asset Allocation
    st.subheader("Asset Allocation")
    asset_allocation = df.groupby("Asset_Type")['Investment_Amount'].sum()
    fig, ax = plt.subplots()
    asset_allocation.plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=90)
    ax.set_ylabel("")
    ax.set_title("Portfolio Asset Allocation")
    st.pyplot(fig)
    
    # Risk Analysis
    st.subheader("Risk Analysis")
    df['Daily_Return'] = df['Current_Value'].pct_change()
    volatility = df['Daily_Return'].std() * np.sqrt(252)
    st.write(f"Portfolio Volatility (Annualized): {volatility:.2f}")
    
    # Performance Trend
    st.subheader("Portfolio Performance Over Time")
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    st.line_chart(df['Current_Value'])

st.write("---")
st.write("Developed using Streamlit")
