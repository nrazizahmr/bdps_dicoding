import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model, scaler, dan expected_features
model = joblib.load('Submission2/svm_model.joblib')
scaler = joblib.load('Submission2/scaler.pkl')
expected_features = joblib.load('Submission2/expected_features.pkl')

st.title('🎓 Student Dropout Prediction')

# Form Input
with st.form("input_form"):
    st.subheader("Personal Information")
    gender = st.selectbox('Gender', ['Male', 'Female'])
    nationality = st.selectbox('Nationality', ['Portuguese', 'German', 'Spanish', 'Italian', 'Other'])
    displaced = st.selectbox('Displaced', ['Yes', 'No'])

    st.subheader("Academic Information")
    admission_grade = st.slider('Admission Grade', 0.0, 200.0, 150.0)
    scholarship_holder = st.selectbox('Scholarship Holder', ['Yes', 'No'])
    tuition_fees_up_to_date = st.selectbox('Tuition Fees Up to Date', ['Yes', 'No'])
    curricular_units_1st_sem_enrolled = st.number_input('1st Semester Enrolled', 0, 30, 10)
    curricular_units_1st_sem_approved = st.number_input('1st Semester Approved', 0, 30, 8)
    curricular_units_1st_sem_grade = st.number_input('1st Semester Grade', 0.0, 20.0, 12.0)
    curricular_units_2nd_sem_enrolled = st.number_input('2nd Semester Enrolled', 0, 30, 10)
    curricular_units_2nd_sem_approved = st.number_input('2nd Semester Approved', 0, 30, 8)
    curricular_units_2nd_sem_grade = st.number_input('2nd Semester Grade', 0.0, 20.0, 13.0)

    submit = st.form_submit_button("Predict")

# Prediksi
if submit:
    input_dict = {
        'Gender': gender,
        'Nationality': nationality,
        'Displaced': 1 if displaced == 'Yes' else 0,
        'Admission_grade': admission_grade,
        'Scholarship_holder': 1 if scholarship_holder == 'Yes' else 0,
        'Tuition_fees_up_to_date': 1 if tuition_fees_up_to_date == 'Yes' else 0,
        'Curricular_units_1st_sem_enrolled': curricular_units_1st_sem_enrolled,
        'Curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_grade': curricular_units_1st_sem_grade,
        'Curricular_units_2nd_sem_enrolled': curricular_units_2nd_sem_enrolled,
        'Curricular_units_2nd_sem_approved': curricular_units_2nd_sem_approved,
        'Curricular_units_2nd_sem_grade': curricular_units_2nd_sem_grade
    }

    input_df = pd.DataFrame([input_dict])

    # One-hot encoding
    input_df_encoded = pd.get_dummies(input_df)
    for col in expected_features:
        if col not in input_df_encoded.columns:
            input_df_encoded[col] = 0
    input_df_encoded = input_df_encoded[expected_features]

    input_scaled = scaler.transform(input_df_encoded)
    prediction = model.predict(input_scaled)[0]

    status_dict = {0: 'Dropout', 1: 'Enrolled', 2: 'Graduate'}
    predicted_status = status_dict[prediction]

    st.success(f"The model predicts that the student is likely to be: **{predicted_status}** 🎉")
