# Gender Male -> 1 and female -> 0
# Churn Yes -> 1 and No -> 0
# scaler is exported as scaler.pkl
# model is exported as model.pkl
# order of x is: -> 'Age', 'Gender', 'Tenure', 'MonthlyCharges'

import streamlit as st
import joblib
import numpy as np

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("Churn Prediction app")

st.divider()

st.write("Please enter the values and hit the predict button for getting a prediction.")

st.divider()

age = st.number_input("Enter Age", min_value= 10, max_value= 100, value=30)
tenure = st.number_input("Enter Tenure", min_value=0, max_value=130, value=10)
monthly_charges = st.number_input("Enter Monthly Charge", min_value= 30, max_value= 150)
gender = st.selectbox("Enter Gender", options=["Male", "Female"])

st.divider()

if st.button("Predict"):
    gender = 1 if gender == "Male" else 0
    input_data = np.array([[age, gender, tenure, monthly_charges]])
    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)
    st.write("Churn Prediction:", "Yes" if prediction[0] == 1 else "No")

else:
    st.write("Please enter the values and use the predict button.")
