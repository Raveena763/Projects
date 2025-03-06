# Projects
### *1. Portfolio Management Documentation*

#### *What is the Project?*
The Portfolio Management project is a financial tool designed to help users track and analyze their investment portfolios. It allows users to upload their portfolio data, which includes details such as asset type, invested amount, and current value. The system processes this data to provide insights into investment distribution, performance, and returns. The goal is to help users make informed decisions about their investments by visualizing their portfolio's performance over time.

#### *What Has Been Done?*
The project processes uploaded portfolio data using Python libraries like *Pandas* and *NumPy* to calculate key metrics such as total investment, current portfolio value, and returns. It also generates visualizations using *Matplotlib* to display the distribution of assets and performance trends. The user interface is built using *Streamlit*, making it easy for users to interact with the tool and upload their data in CSV format.

#### *Main Libraries Used*
- *Streamlit*: For creating the user-friendly web interface.
- *Pandas*: For data manipulation and analysis.
- *NumPy*: For numerical calculations.
- *Matplotlib*: For generating visualizations like pie charts and line graphs.

#### *How to Run the Project?*
1. Ensure Python and the required libraries (Streamlit, Pandas, NumPy, Matplotlib) are installed.
2. Download the project files and navigate to the project directory in the terminal.
3. Run the command:  
   bash
   streamlit run portfolio_management.py
   
4. The Streamlit app will open in your browser. Upload your portfolio data in CSV format (with columns like Date, Asset Type, Invested Amount, and Current Value).
5. The app will process the data and display insights, including investment distribution and returns.

---
###Link
https://github.com/Raveena763/Portfolio_Management
### *2. Credit Risk Assessment Documentation*

#### *What is the Project?*
The Credit Risk Assessment project is a machine learning-based tool designed to evaluate the creditworthiness of loan applicants. It analyzes financial data such as income, loan amount, credit history, and employment details to predict the likelihood of default. The goal is to help financial institutions or individuals assess the risk associated with lending money to applicants.

#### *What Has Been Done?*
The project uses machine learning models (e.g., logistic regression, decision trees) built with *Scikit-learn* to analyze applicant data. The dataset includes features like income, loan amount, credit history, and loan status. The system processes this data, trains the model, and provides predictions on whether an applicant is likely to default. The user interface is built using *Streamlit*, allowing users to upload applicant data and view risk predictions.

#### *Main Libraries Used*
- *Streamlit*: For creating the web interface.
- *Pandas*: For data manipulation and preprocessing.
- *NumPy*: For numerical calculations.
- *Scikit-learn*: For building and training machine learning models.

#### *How to Run the Project?*
1. Install Python and the required libraries (Streamlit, Pandas, NumPy, Scikit-learn).
2. Download the project files and navigate to the project directory in the terminal.
3. Run the command:  
   bash
   streamlit run credit_risk.py
   
4. The Streamlit app will open in your browser. Upload the applicant data in CSV format (with columns like Income, Loan Amount, Credit History, etc.).
5. The app will process the data, apply the machine learning model, and display the risk assessment results.

---
###Link
https://github.com/Raveena763/Credit_Risk_Assesment
### *3. Budget Analysis Documentation*

#### *What is the Project?*
The Budget Analysis project is a financial management tool that helps users track their income and expenses. Users can input transactions manually, categorize them, and analyze spending trends over time. The goal is to provide users with a clear understanding of their financial habits and help them make better budgeting decisions.

#### *What Has Been Done?*
The project allows users to input transactions, which are then categorized and analyzed using *Pandas. Visualizations are generated using **Matplotlib* and *Seaborn* to display spending trends, income vs. expenses, and category-wise breakdowns. The user interface is built using *Streamlit*, making it easy for users to interact with the tool and input their financial data.

#### *Main Libraries Used*
- *Streamlit*: For creating the web interface.
- *Pandas*: For data manipulation and analysis.
- *Matplotlib* and *Seaborn*: For generating visualizations like bar charts, pie charts, and line graphs.

#### *How to Run the Project?*
1. Install Python and the required libraries (Streamlit, Pandas, Matplotlib, Seaborn).
2. Download the project files and navigate to the project directory in the terminal.
3. Run the command:  
   bash
   streamlit run budget_analysis.py
   
4. The Streamlit app will open in your browser. Input your transactions manually or upload a CSV file with columns like Date, Category, Amount, and Type (income/expense).
5. The app will process the data and display visualizations of your spending trends and budget breakdown.

---
###Link
https://github.com/Raveena763/Budget_Analysis
### *4. Stock Price Prediction Documentation*

#### *What is the Project?*
The Stock Price Prediction project is a machine learning-based tool designed to predict future stock prices using historical data from the National Stock Exchange (NSE). The project fetches historical stock data, processes it, and applies machine learning models to predict future prices. The goal is to help investors make informed decisions by providing accurate stock price predictions.

#### *What Has Been Done?*
The project fetches historical stock data (Open, High, Low, Close, Volume) and processes it using *Pandas. Machine learning models (e.g., linear regression, random forest) are built using **Scikit-learn* to predict future stock prices. Visualizations are generated using *Matplotlib* and *Seaborn* to display historical trends and predicted prices. The user interface is built using *Streamlit*, allowing users to select a stock and view predictions.

#### *Main Libraries Used*
- *Streamlit*: For creating the web interface.
- *Pandas*: For data manipulation and preprocessing.
- *NumPy*: For numerical calculations.
- *Scikit-learn*: For building and training machine learning models.
- *Matplotlib* and *Seaborn*: For generating visualizations.

#### *How to Run the Project?*
1. Install Python and the required libraries (Streamlit, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn).
2. Download the project files and navigate to the project directory in the terminal.
3. Run the command:  
   bash
   streamlit run stock_price.py
   
4. The Streamlit app will open in your browser. Select a stock from the dropdown menu or input a stock symbol.
5. The app will fetch historical data, process it, and display visualizations of historical trends and predicted prices.

---
###Link
https://github.com/Raveena763/Stock_Price_Predictor
