import joblib
from sklearn.ensemble import RandomForestClassifier
from data_preprocessing import load_and_preprocess_data

X_train, X_test, y_train, y_test = load_and_preprocess_data('../data/ai4i2020.csv')

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, '../models/atm_rf_model.pkl')  # Save model
print("Model training complete. Model saved as atm_rf_model.pkl.")
