import joblib

model = joblib.load("model/model.pkl")

def predict_eta(features: list):
    pred = model.predict([features])
    return float(pred[0])