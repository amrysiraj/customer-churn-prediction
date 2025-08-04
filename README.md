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
   git clone https://github.com/amrysiraj/customer-churn-prediction.git
   cd customer-churn-prediction

2. Install the required packages
   ```bash
   pip install -r requirements.txt

3. Run the Streamlit app
   ```bash
   streamlit run app.py

The app will open in your browser. Enter customer details to get a churn prediction instantly.

## Project Structure

- app.py — Streamlit app for making churn predictions
- data_preprocessing.py — Script for preprocessing and feature engineering
- model.pkl — Trained churn prediction model
- scaler.pkl — Scaler used to normalize inputs
- requirements.txt — Python packages needed to run the project
- README.md — Project documentation (this file)

## Dataset

- **Source:** [Credit Card Customers Dataset – Kaggle](https://www.kaggle.com/datasets/abdullah0a/telecom-customer-churn-insights-for-analysis)  
- **Target Variable:** `Churn` (1 = Churned, 0 = Active)


## Notes

- Gender is encoded as: Male = 1, Female = 0
- Churn prediction output: 1 = Yes (Will Churn), 0 = No (Will Stay)
- Features used include: Age, Gender, Tenure, Total Transaction Count, Credit Limit, etc.

## Tools Used

- Python (Pandas, NumPy, Scikit-learn)
- Streamlit (Web app for predictions)
- VS Code (Development)
- GitHub (Version control and portfolio)

## License

This project is licensed under the [MIT License](LICENSE).
