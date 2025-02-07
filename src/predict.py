import joblib
import pandas as pd

# Load trained model
model = joblib.load('../models/atm_rf_model.pkl')

def predict_failure(data):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return "Failure" if prediction[0] == 1 else "No Failure"

if __name__ == "__main__":
    sample_data = {'Air temperature [K]': 300, 'Process temperature [K]': 310,
                   'Rotational speed [rpm]': 1200, 'Torque [Nm]': 40, 'Tool wear [min]': 100}
    print(predict_failure(sample_data))
