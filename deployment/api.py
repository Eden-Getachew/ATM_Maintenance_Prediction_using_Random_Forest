import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

# Load the model
try:
    model = joblib.load('models/atm_rf_model.pkl')  # Ensure the path is correct relative to the location of api.py
    print("Model loaded successfully.")
    print("Model features:", model.feature_names_in_)  # Inspect model features
except Exception as e:
    print(f"Error loading model: {e}")
    model = None  # Set model to None in case of an error

class InputData(BaseModel):
    Air_temperature_K: float
    Process_temperature_K: float
    Rotational_speed_rpm: float
    Torque_Nm: float
    Tool_wear_min: float
    Type_M: int
    Type_L: int

@app.post("/predict")
def predict(data: InputData):
    if model is None:
        raise HTTPException(status_code=500, detail="Model loading failed.")

    try:
        # Convert input data to DataFrame
        input_data = pd.DataFrame([data.dict()])
        
        # Rename columns to match the feature names in the model
        input_data.rename(columns={
            'Air_temperature_K': 'Air temperature [K]',
            'Process_temperature_K': 'Process temperature [K]',
            'Rotational_speed_rpm': 'Rotational speed [rpm]',
            'Torque_Nm': 'Torque [Nm]',
            'Tool_wear_min': 'Tool wear [min]'
        }, inplace=True)

        # Reorder columns to match the order during model training
        expected_order = model.feature_names_in_  # Get the expected feature order
        input_data = input_data[expected_order]  # Reorder input data based on model's expected order

        print(f"Input Data (renamed and reordered): {input_data.head()}")  # Debugging input data
        
        # Make prediction using the loaded model
        prediction = model.predict(input_data)
        print(f"Prediction: {prediction}")  # Debugging prediction result
        
        # Map the prediction to readable format
        prediction_label = "Failure" if prediction[0] == 1 else "No Failure"
        
        return {"prediction": prediction_label}
    
    except Exception as e:
        print(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
