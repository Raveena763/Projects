import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Set up the app
st.title("Credit Risk Assessment")
st.sidebar.header("Upload CSV File")

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.write(df.head())
    
    # Select features and target
    if "Loan_Status" in df.columns:
        X = df.drop(columns=["Loan_Status"])
        y = df["Loan_Status"].map({'Y': 1, 'N': 0})  # Convert labels to 0/1
        
        # Handle categorical variables
        X = pd.get_dummies(X, drop_first=True)
        
        # Train-Test Split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train a RandomForest Model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Predictions and evaluation
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)
        
        st.subheader("Model Performance")
        st.write(f"Accuracy: {accuracy:.2f}")
        st.json(report)
        
        # Feature Importance Visualization
        feature_importance = pd.Series(model.feature_importances_, index=X.columns)
        fig, ax = plt.subplots()
        feature_importance.nlargest(10).plot(kind='bar', ax=ax, color='blue')
        ax.set_title("Top 10 Feature Importances")
        st.pyplot(fig)
    else:
        st.error("Dataset must contain a 'Loan_Status' column to proceed.")
