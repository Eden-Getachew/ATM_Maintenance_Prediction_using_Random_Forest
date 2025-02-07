import streamlit as st
import pandas as pd
import requests

# FastAPI endpoint URL
API_URL = "https://atm-maintenance-prediction-using-random.onrender.com/predict"  # Update with your deployed API URL

# Streamlit app UI
st.title("ATM Maintenance Prediction")

st.write("This app predicts whether ATM maintenance is needed based on the input features.")

# Input fields for user to provide test data
air_temp = st.number_input("Air temperature [K]", value=300.0)
process_temp = st.number_input("Process temperature [K]", value=290.0)
rotational_speed = st.number_input("Rotational speed [rpm]", value=3500)
torque = st.number_input("Torque [Nm]", value=55.0)
tool_wear = st.number_input("Tool wear [min]", value=15.0)
type_m = st.selectbox("Type_M", [1, 0])
type_l = st.selectbox("Type_L", [1, 0])

# Prepare the input data in the same format the model expects
input_data = {
    "Air temperature [K]": [air_temp],
    "Process temperature [K]": [process_temp],
    "Rotational speed [rpm]": [rotational_speed],
    "Torque [Nm]": [torque],
    "Tool wear [min]": [tool_wear],
    "Type_M": [type_m],
    "Type_L": [type_l]
}

# Convert the input data to a pandas DataFrame
input_df = pd.DataFrame(input_data)

# Display the input data
st.write("Input Data (for prediction):")
st.write(input_df)

# Button to send the data for prediction
if st.button("Predict Maintenance Status"):
    try:
        # Send data to FastAPI endpoint for prediction
        response = requests.post(API_URL, json=input_data)
        
        # Check if the response is successful
        if response.status_code == 200:
            prediction = response.json()
            prediction_label = "Failure" if prediction['prediction'] == 1 else "No Failure"
            st.write(f"Prediction: {prediction_label}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")

