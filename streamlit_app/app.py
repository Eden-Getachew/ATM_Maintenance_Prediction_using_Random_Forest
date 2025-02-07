import streamlit as st
import requests
import pandas as pd
import json

# Define the API URL (Make sure to change this to the correct URL if deployed)
api_url = "https://atm-maintenance-prediction-using-random.onrender.com/predict"  # Adjust as per your deployment

# Streamlit interface for inputs
st.title("ATM Maintenance Prediction")

# Input fields
air_temperature = st.number_input('Air temperature [K]', min_value=0.0, value=300.0)
process_temperature = st.number_input('Process temperature [K]', min_value=0.0, value=290.0)
rotational_speed = st.number_input('Rotational speed [rpm]', min_value=0, value=3500)
torque = st.number_input('Torque [Nm]', min_value=0.0, value=55.0)
tool_wear = st.number_input('Tool wear [min]', min_value=0.0, value=15.0)

# Type values (ensure they are integers)
type_m = st.selectbox("Type_M", options=[0, 1], index=1)
type_l = st.selectbox("Type_L", options=[0, 1], index=0)

# Collect the data as a dictionary
input_data = {
    "Air_temperature_K": air_temperature,
    "Process_temperature_K": process_temperature,
    "Rotational_speed_rpm": rotational_speed,
    "Torque_Nm": torque,
    "Tool_wear_min": tool_wear,
    "Type_M": type_m,
    "Type_L": type_l
}

# Convert the input data to JSON format
input_json = json.dumps(input_data)

# Make a POST request to the FastAPI prediction endpoint
if st.button('Predict'):
    try:
        response = requests.post(api_url, data=input_json, headers={'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            result = response.json()
            st.write(f"Prediction Result: {result['prediction']}")
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
