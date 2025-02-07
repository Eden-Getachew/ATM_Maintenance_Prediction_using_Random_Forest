import streamlit as st
import requests

st.title("ATM Maintenance Prediction")

air_temp = st.number_input("Air Temperature [K]", min_value=200, max_value=400)
process_temp = st.number_input("Process Temperature [K]", min_value=200, max_value=400)
speed = st.number_input("Rotational Speed [rpm]", min_value=500, max_value=3000)
torque = st.number_input("Torque [Nm]", min_value=0, max_value=100)
tool_wear = st.number_input("Tool Wear [min]", min_value=0, max_value=300)

if st.button("Predict"):
    input_data = {
        "Air temperature [K]": air_temp,
        "Process temperature [K]": process_temp,
        "Rotational speed [rpm]": speed,
        "Torque [Nm]": torque,
        "Tool wear [min]": tool_wear
    }
    response = requests.post("http://127.0.0.1:8000/predict/", json=input_data)
    st.write(response.json())
