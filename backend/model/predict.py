# import necessary libraries
# and model, scaler, and mae from load_model
from model.load_model import model, scaler, mae
import pandas as pd

# function to make prediction
def make_prediction(data):

    # convert user input data to DataFrame
    input_data = pd.DataFrame({
    'age': [data.age],
    'bmi': [data.bmi],
    'risk_score': [data.risk_score],
    'chronic_count': [data.chronic_count],
    'provider_quality': [data.provider_quality]
    })
    
    # scale the input data and make prediction
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)
    
    return prediction