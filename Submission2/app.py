import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model, scaler, dan expected_features
model = joblib.load('Submission2/svm_model.joblib')
scaler = joblib.load('Submission2/scaler.pkl')
expected_features = joblib.load('Submission2/expected_features.pkl')

numeric_features = list(scaler.feature_names_in_)

# Prediction function
def predict_status(input_dict):
    # Create DataFrame from input
    input_df = pd.DataFrame([input_dict])

    # One-hot encode categorical inputs
    input_encoded = pd.get_dummies(input_df)

    # Add missing expected features
    for col in expected_features:
        if col not in input_encoded.columns:
            input_encoded[col] = 0

    # Ensure correct column order
    input_encoded = input_encoded[expected_features]

    # Scale numeric features
    input_encoded[numeric_features] = scaler.transform(input_encoded[numeric_features])

    # Predict using the trained model
    pred = model.predict(input_encoded)
    return pred[0]

# Streamlit UI
st.title('🎓 Student Dropout Prediction')
with st.form(key='prediction_form'):
    # Categorical inputs
    marital_status = st.text_input('Marital Status', '')
    application_mode = st.text_input('Application Mode', '')
    application_order = st.number_input('Application Order', min_value=1, step=1, value=1)
    course = st.text_input('Course', '')
    daytime_evening = st.text_input('Daytime/Evening Attendance', '')
    prev_qual = st.text_input('Previous Qualification', '')
    prev_qual_grade = st.text_input('Previous Qualification Grade', '')
    nationality = st.text_input('Nationality', '')
    mother_qual = st.text_input("Mother's Qualification", '')
    father_qual = st.text_input("Father's Qualification", '')
    mother_occ = st.text_input("Mother's Occupation", '')
    father_occ = st.text_input("Father's Occupation", '')

    # Binary inputs
    displaced = st.selectbox('Displaced', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    special_needs = st.selectbox('Educational Special Needs', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    debtor = st.selectbox('Debtor', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    tuition_up_to_date = st.selectbox('Tuition Fees Up to Date', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    gender = st.selectbox('Gender', [0, 1], format_func=lambda x: 'Female' if x == 1 else 'Male')
    scholarship = st.selectbox('Scholarship Holder', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    international = st.selectbox('International', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')

    # Numeric inputs
    admission_grade = st.number_input('Admission Grade', min_value=0.0, step=0.1, value=100.0)
    age_enroll = st.number_input('Age at Enrollment', min_value=15, step=1, value=20)
    cur1_credited = st.number_input('Curricular Units 1st Sem Credited', min_value=0, step=1, value=0)
    cur1_enrolled = st.number_input('Curricular Units 1st Sem Enrolled', min_value=0, step=1, value=0)
    cur1_evaluations = st.number_input('Curricular Units 1st Sem Evaluations', min_value=0, step=1, value=0)
    cur1_approved = st.number_input('Curricular Units 1st Sem Approved', min_value=0, step=1, value=0)
    cur1_grade = st.number_input('Curricular Units 1st Sem Grade', min_value=0.0, step=0.1, value=0.0)
    cur1_without = st.number_input('Curricular Units 1st Sem Without Evaluations', min_value=0, step=1, value=0)
    cur2_credited = st.number_input('Curricular Units 2nd Sem Credited', min_value=0, step=1, value=0)
    cur2_enrolled = st.number_input('Curricular Units 2nd Sem Enrolled', min_value=0, step=1, value=0)
    cur2_evaluations = st.number_input('Curricular Units 2nd Sem Evaluations', min_value=0, step=1, value=0)
    cur2_approved = st.number_input('Curricular Units 2nd Sem Approved', min_value=0, step=1, value=0)
    cur2_grade = st.number_input('Curricular Units 2nd Sem Grade', min_value=0.0, step=0.1, value=0.0)
    cur2_without = st.number_input('Curricular Units 2nd Sem Without Evaluations', min_value=0, step=1, value=0)
    unemployment_rate = st.number_input('Unemployment Rate', min_value=0.0, step=0.1, value=5.0)
    inflation_rate = st.number_input('Inflation Rate', min_value=0.0, step=0.1, value=2.0)
    gdp = st.number_input('GDP', min_value=0.0, step=1.0, value=1000.0)

    submit = st.form_submit_button('Predict')

if submit:
    # Collect inputs into dict
    input_dict = {
        'Marital_status': marital_status,
        'Application_mode': application_mode,
        'Application_order': application_order,
        'Course': course,
        'Daytime_evening_attendance': daytime_evening,
        'Previous_qualification': prev_qual,
        'Previous_qualification_grade': prev_qual_grade,
        'Nacionality': nationality,
        'Mothers_qualification': mother_qual,
        'Fathers_qualification': father_qual,
        'Mothers_occupation': mother_occ,
        'Fathers_occupation': father_occ,
        'Admission_grade': admission_grade,
        'Displaced': displaced,
        'Educational_special_needs': special_needs,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_up_to_date,
        'Gender': gender,
        'Scholarship_holder': scholarship,
        'Age_at_enrollment': age_enroll,
        'International': international,
        'Curricular_units_1st_sem_credited': cur1_credited,
        'Curricular_units_1st_sem_enrolled': cur1_enrolled,
        'Curricular_units_1st_sem_evaluations': cur1_evaluations,
        'Curricular_units_1st_sem_approved': cur1_approved,
        'Curricular_units_1st_sem_grade': cur1_grade,
        'Curricular_units_1st_sem_without_evaluations': cur1_without,
        'Curricular_units_2nd_sem_credited': cur2_credited,
        'Curricular_units_2nd_sem_enrolled': cur2_enrolled,
        'Curricular_units_2nd_sem_evaluations': cur2_evaluations,
        'Curricular_units_2nd_sem_approved': cur2_approved,
        'Curricular_units_2nd_sem_grade': cur2_grade,
        'Curricular_units_2nd_sem_without_evaluations': cur2_without,
        'Unemployment_rate': unemployment_rate,
        'Inflation_rate': inflation_rate,
        'GDP': gdp
    }

    # Predict and display result
    pred_class = predict_status(input_dict)
    status_map = {0: 'Dropout', 1: 'Enrolled', 2: 'Graduate'}
    st.success(f"The model predicts that the student is likely to be: **{status_map.get(pred_class, pred_class)}** 🎉")
