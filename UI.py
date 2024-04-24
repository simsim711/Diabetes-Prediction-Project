import streamlit as st
from joblib import load
import pandas as pd

# Load the trained model
model = load('/Users/sarimkazmi/Desktop/model.joblib')

# Define the input fields and collect input data
age = st.number_input('Age', min_value=0, max_value=120, value=30, step=1)
hypertension = st.selectbox('Hypertension', options=['True', 'False'], format_func=lambda x: 'Yes' if x == 'True' else 'No')
heart_disease = st.selectbox('Heart Disease', options=['True', 'False'], format_func=lambda x: 'Yes' if x == 'True' else 'No')
bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=25.0, step=0.1)
hba1c_level = st.number_input('HbA1c Level', min_value=0.0, max_value=15.0, value=5.7, step=0.1)
blood_glucose_level = st.number_input('Blood Glucose Level', min_value=50, max_value=300, value=100, step=1)
gender_male = st.selectbox('Gender Male', options=['True', 'False'], format_func=lambda x: 'Male' if x == 'True' else 'Female')
gender_other = st.selectbox('Gender Other', options=['True', 'False'], format_func=lambda x: 'Other' if x == 'True' else 'Not Specified')
smoking_history_current = st.selectbox('Smoking History Current', options=['True', 'False'], format_func=lambda x: 'Current' if x == 'True' else 'Not Current')
smoking_history_ever = st.selectbox('Smoking History Ever', options=['True', 'False'], format_func=lambda x: 'Ever' if x == 'True' else 'Never')
smoking_history_former = st.selectbox('Smoking History Former', options=['True', 'False'], format_func=lambda x: 'Former' if x == 'True' else 'Not Former')
smoking_history_never = st.selectbox('Smoking History Never', options=['True', 'False'], format_func=lambda x: 'Never' if x == 'True' else 'Ever')
smoking_history_not_current = st.selectbox('Smoking History Not Current', options=['True', 'False'], format_func=lambda x: 'Not Current' if x == 'True' else 'Current')

# Make prediction on button click
if st.button('Predict Diabetes Status'):
    # Create a DataFrame with the input features, mapping True/False back to 1/0
    input_features = pd.DataFrame([[
        age,
        1 if hypertension == 'True' else 0,
        1 if heart_disease == 'True' else 0,
        bmi,
        hba1c_level,
        blood_glucose_level,
        1 if gender_male == 'True' else 0,
        1 if gender_other == 'True' else 0,
        1 if smoking_history_current == 'True' else 0,
        1 if smoking_history_ever == 'True' else 0,
        1 if smoking_history_former == 'True' else 0,
        1 if smoking_history_never == 'True' else 0,
        1 if smoking_history_not_current == 'True' else 0
    ]], columns=[
        'age',
        'hypertension',
        'heart_disease',
        'bmi',
        'HbA1c_level',
        'blood_glucose_level',
        'gender_Male',
        'gender_Other',
        'smoking_history_current',
        'smoking_history_ever',
        'smoking_history_former',
        'smoking_history_never',
        'smoking_history_not current'
    ])

    # Make a prediction
    prediction = model.predict(input_features)
    
    # Display the prediction
    st.write(f'Prediction: {"Diabetic" if prediction[0] else "Not Diabetic"}')
