# Customer Churn Prediction

This project predicts whether a credit card customer is likely to churn (leave) based on their demographics and usage patterns. It includes:

- Data preprocessing and exploratory data analysis (EDA)
- Feature engineering and encoding categorical variables
- Training multiple machine learning models with hyperparameter tuning
- Saving the best model and scaler for future use
- A Streamlit web app for interactive churn prediction

## How to run the Streamlit app locally

1. Clone this repository  
   ```bash
   git clone https://github.com/yourusername/credit-card-churn-prediction.git
   cd credit-card-churn-prediction

2. Install the required packages
   pip install -r requirements.txt

3. Run the Streamlit app

The app will open in your browser. Enter customer details to get a churn prediction instantly.

## File Descriptions

- app.py — Streamlit app for making churn predictions
- data_preprocessing.py — Script for preprocessing and feature engineering
- model.pkl — Trained churn prediction model
- scaler.pkl — Scaler used to normalize inputs
- requirements.txt — Python packages needed to run the project
- README.md — Project documentation (this file)

## Dataset

- Source: Credit Card Customers Dataset – Kaggle
- Target Variable: Attrition_Flag (1 = Churned, 0 = Active)

## Notes