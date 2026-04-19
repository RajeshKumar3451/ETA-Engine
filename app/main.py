from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_eta

app = FastAPI()

class InputData(BaseModel):
    distance_km: float
    order_hour: int
    traffic_level: int
    prep_time: int
    weather: int
    delivery_rating: float

@app.get("/")
def home():
    return {"message": "ETA Prediction API Running"}

@app.post("/predict")
def predict(data: InputData):
    features = [
        data.distance_km,
        data.order_hour,
        data.traffic_level,
        data.prep_time,
        data.weather,
        data.delivery_rating
    ]
    
    eta = predict_eta(features)
    
    return {"predicted_eta": eta}