import streamlit as st
import requests

st.set_page_config(
    page_title="Annual Medical Cost AI System",   # This changes the browser tab title
    page_icon="💊",             # Optional: add an emoji or icon
    layout="centered"           # Optional: "wide" or "centered"
)

st.title("Annual Medical Cost AI System")

st.write("This application predicts annual medical costs based on user inputs")

col1, col2, col3 = st.columns(3)
with col1:
    age = st.slider("Age", 0, 100, 25)
    bmi = st.slider("BMI", 10, 60, 22)
with col2:
    risk_score = st.slider("Health Risk Score", 0.0, 1.0, 0.1)
    chronic_count = st.slider("Number of Chronic Conditions", 0, 10, 0)
with col3:
    provider_quality = st.slider("Healthcare Provider Quality (1-10)", 1, 10, 7)

if st.button("Predict Annual Medical Cost"):
    data = {
        "age": int(age),
        "bmi": int(bmi),
        "risk_score": float(risk_score),
        "chronic_count": int(chronic_count),
        "provider_quality": int(provider_quality)
    }

    try:
        response = requests.post("http://localhost:8000/predict", json=data)
        
        result = response.json()
        if response.status_code == 200:
            prediction = result["response"]['prediction']
            mae = result["response"]['mae']
            
            st.header("Prediction Results")
            st.success(f"Cost : ${prediction:.2f}")
            st.error(f"Error : ±${mae:.2f} (MAE)")
  
        else:
            st.error(f"Error: {response.status_code}- {response.text}")
    
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the prediction API. Please ensure the API server is running.")
        