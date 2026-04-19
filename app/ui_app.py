import streamlit as st
import requests
import time

API_URL = "https://eta-prediction-api.onrender.com/predict"

st.set_page_config(page_title="ETA Predictor", page_icon="🚚", layout="centered")

st.title("🚚 ETA Prediction System")
st.markdown("Enter delivery details to predict estimated delivery time")

st.markdown("### 🔌 System Status")
try:
    requests.get(API_URL.replace("/predict", "/"), timeout=2)
    st.success("✅ Backend API is connected")
except:
    st.error("❌ Backend API is not reachable")

st.markdown("---")

distance = st.slider("Distance (km)", 0.5, 10.0, 3.0)
hour = st.slider("Order Hour", 0, 23, 13)
traffic = st.slider("Traffic Level", 1, 5, 3)
prep = st.slider("Preparation Time (min)", 5, 40, 20)
weather = st.selectbox("Weather Condition", [1, 2, 3])
rating = st.slider("Delivery Rating", 1.0, 5.0, 4.5)

payload = {
    "distance_km": distance,
    "order_hour": hour,
    "traffic_level": traffic,
    "prep_time": prep,
    "weather": weather,
    "delivery_rating": rating
}

st.markdown("### 📥 Input Summary")
st.json(payload)

if st.button("🚀 Predict ETA"):
    with st.spinner("Predicting delivery time... ⏳"):
        try:
            response = requests.post(API_URL, json=payload, timeout=10)
            result = response.json()
            time.sleep(1)

            eta = round(result["predicted_eta"], 2)

            st.markdown("### 📊 Prediction Result")
            st.metric(label="Estimated Delivery Time", value=f"{eta} min")

            st.success(f"⏱️ ETA: {eta} minutes")

        except Exception as e:
            st.error("⚠️ Failed to fetch prediction. Please check API.")

st.markdown("---")
st.markdown("👨‍💻 Built by Rajesh | ML Engineer Project 🚀")
