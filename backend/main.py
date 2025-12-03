# import necessary libraries
from fastapi import FastAPI
from fastapi.responses import JSONResponse
# import user input schema and prediction function
# and model evaluation metric from respective files
from schema.user_input import UserInput
from model.predict import make_prediction
from model.load_model import mae

# initialize FastAPI app
app = FastAPI()

# home endpoint
@app.get("/")
def home():
    return {"message": "Hello, World!"}

# prediction endpoint
@app.post("/predict")
def predict(data: UserInput):
    
    try:
        # make prediction using the user input data
        prediction = make_prediction(data)

        return JSONResponse(status_code=200, content={"response": {"prediction": prediction[0], "mae": mae}})

    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))