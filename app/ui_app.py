import streamlit as st
import requests

API_URL = "https://eta-prediction-api.onrender.com/predict"

st.set_page_config(page_title="ETA Predictor", page_icon="🚚")

st.title("🚚 ETA Prediction System")

st.markdown("Enter delivery details to predict ETA")

distance = st.slider("Distance (km)", 0.5, 10.0, 3.0)
hour = st.slider("Order Hour", 0, 23, 13)
traffic = st.slider("Traffic Level", 1, 5, 3)
prep = st.slider("Preparation Time (min)", 5, 40, 20)
weather = st.selectbox("Weather Condition", [1, 2, 3])
rating = st.slider("Delivery Rating", 1.0, 5.0, 4.5)

if st.button("Predict ETA"):
    payload = {
        "distance_km": distance,
        "order_hour": hour,
        "traffic_level": traffic,
        "prep_time": prep,
        "weather": weather,
        "delivery_rating": rating
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        result = response.json()

        st.success(f"⏱️ Estimated Delivery Time: {round(result['predicted_eta'], 2)} minutes")

    except Exception as e:
        st.error("⚠️ API error. Check backend or URL.")