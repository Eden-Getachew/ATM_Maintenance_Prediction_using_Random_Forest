

ATM Maintenance Prediction System



Overview
The ATM Maintenance Prediction System is a machine learning-based application designed to predict whether an ATM requires maintenance based on sensor data. The system leverages a trained Random Forest Classifier, served via a FastAPI backend, and provides a user-friendly interface using Streamlit.

Features
Machine Learning Model: Predicts potential ATM failures based on sensor data.
FastAPI Backend: Provides API endpoints for real-time predictions.
Streamlit Frontend: Allows users to input data and view predictions interactively.
Cloud Deployment: The model and API are deployed on Render for scalability.Project Structure


ATM_Maintenance_Prediction/
│── api.py                 # FastAPI backend
│── app.py                 # Streamlit frontend
│── model_training.py      # Script for training the model
│── atm_rf_model.pkl       # Trained machine learning model
│── requirements.txt       # Dependencies
│── README.md              # Project documentation





Installation
Prerequisites
Python 3.x
pip
Setup

Clone the repository: 
git clone: https://github.com/Eden-Getachew/ATM_Maintenance_Prediction_using_Random_Forest.git

Install dependencies: 
pip install -r requirements.txt

Model Training
Run the training script to train the model and save it as a .pkl file: 
python model_training.py
The trained model is saved as atm_rf_model.pkl.

Running the FastAPI Backend
Start the FastAPI server: 
uvicorn api:app --reload
1.The API will be accessible at http://127.0.0.1:8000.
2.Test the API using: 
curl -X 'POST' 'http://127.0.0.1:8000/predict' -H 'Content-Type: application/json' -d '{ "Air_temperature_K": 300.0, "Process_temperature_K": 290.0, "Rotational_speed_rpm": 3500, "Torque_Nm": 55.0, "Tool_wear_min": 15.0, "Type_M": 1, "Type_L": 0 }'

Running the Streamlit Frontend
Start the Streamlit app: 
streamlit run app.py

https://atm-maintenance-prediction-using-random-g2yy.onrender.comDeployment


Deploying FastAPI on Render
1.Push the project to GitHub.
2.Create a new Web Service on Render.
3.Connect the repository and set the Start Command to: 
uvicorn api:app --host 0.0.0.0 --port $PORT
4.Deploy and get the public API URL.

Deploying Streamlit on Render
1.Create a new Web Service.
2.Set the Start Command to: 
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
3.Deploy and access the Streamlit UI online.

API Endpoints
1. Predict Maintenance Status
Endpoint: POST /predict
Request Body:
{
  "Air_temperature_K": 300.0,
  "Process_temperature_K": 290.0,
  "Rotational_speed_rpm": 3500,
  "Torque_Nm": 55.0,
  "Tool_wear_min": 15.0,
  "Type_M": 1,
  "Type_L": 0
}
Response:
{
  "prediction": "Failure"
}


Troubleshooting
FastAPI server not running? Ensure uvicorn is installed and the model file exists.
Streamlit UI not loading? Check if the API is running and the correct URL is set in app.py.
Deployment issues? Verify environment variables and logs on Render.
License
This project is licensed under the MIT License.

Contributors
Eden getachew


Acknowledgments

Special thanks to OpenAI, scikit-learn, and the Python community for providing resources to make this project possible.
