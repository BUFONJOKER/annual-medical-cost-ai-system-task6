# import joblib to load the model and scaler
import joblib

# load the model, scaler, and mae from the pickle file
model_scaler_mae = joblib.load("model/model_scaler_mae.pkl")
model = model_scaler_mae['model']
scaler = model_scaler_mae['scaler']
mae = model_scaler_mae['mae']