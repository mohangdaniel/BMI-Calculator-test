import streamlit as st
from bmi_logic import calculate_bmi, classify_bmi, health_advice

st.title("Smart BMI Calculator")

weight = st.number_input("Enter weight (kg)", min_value=1.0)
height = st.number_input("Enter height (m)", min_value=0.5)

if st.button("Calculate BMI"):

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    advice = health_advice(category)

    st.success(f"Your BMI is: {round(bmi, 2)}")
    st.subheader(f"Category: {category}")
    st.info(advice)