import streamlit as st
import requests
import time
import pandas as pd
import json
import os

API_URL = "https://eta-prediction-api.onrender.com/predict"

st.set_page_config(page_title="ETA ML System", page_icon="🚚", layout="wide")

users = {
    "admin": "1234",
    "rajesh": "ml123"
}

def login():
    st.sidebar.title("🔐 Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username in users and users[username] == password:
            st.session_state["auth"] = True
            st.session_state["user"] = username
        else:
            st.sidebar.error("Invalid credentials")

if "auth" not in st.session_state:
    login()
    st.stop()

st.title("🚚 ETA Prediction System")
st.caption(f"Welcome, {st.session_state['user']} 👋")

st.markdown("### 🔌 System Status")
try:
    requests.get(API_URL.replace("/predict", "/"), timeout=2)
    st.success("✅ Backend API Connected")
except:
    st.error("❌ API Not Reachable")

st.divider()

tab1, tab2 = st.tabs(["🔮 Prediction", "📊 Analytics"])


with tab1:

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📥 Input Features")

        distance = st.slider("📍 Distance (km)", 0.5, 10.0, 3.0)
        hour = st.slider("🕒 Order Hour", 0, 23, 13)
        traffic = st.slider("🚦 Traffic Level", 1, 5, 3)
        prep = st.slider("🍽️ Prep Time (min)", 5, 40, 20)
        weather = st.selectbox("🌦️ Weather", [1, 2, 3])
        rating = st.slider("⭐ Delivery Rating", 1.0, 5.0, 4.5)

    payload = {
        "distance_km": distance,
        "order_hour": hour,
        "traffic_level": traffic,
        "prep_time": prep,
        "weather": weather,
        "delivery_rating": rating
    }

    with col2:
        st.markdown("### 📊 Input Summary")
        st.table({
            "Feature": list(payload.keys()),
            "Value": list(payload.values())
        })

    st.markdown("### 🚀 Prediction")

    if st.button("Predict ETA"):
        with st.spinner("Processing prediction..."):
            try:
                response = requests.post(API_URL, json=payload, timeout=10)
                result = response.json()
                time.sleep(1)

                eta = round(result["predicted_eta"], 2)

                st.metric("⏱️ Estimated Delivery Time", f"{eta} min")

                if eta < 25:
                    st.success("🚀 Fast delivery expected")
                elif eta < 40:
                    st.warning("⏳ Moderate delivery time")
                else:
                    st.error("🚦 Delay expected")

                os.makedirs("logs", exist_ok=True)
                with open("logs/ui_log.json", "a") as f:
                    f.write(json.dumps({
                        "input": payload,
                        "prediction": eta
                    }) + "\n")

            except:
                st.error("⚠️ API request failed")


with tab2:
    st.markdown("## 📊 Analytics Dashboard")

    log_file = "logs/ui_log.json"

    if os.path.exists(log_file):

        df = pd.read_json(log_file, lines=True)

        st.metric("Total Predictions", len(df))
        st.metric("Average ETA", round(df["prediction"].mean(), 2))

        st.markdown("### 📈 Prediction Trend")
        st.line_chart(df["prediction"])

        st.markdown("### 🚦 Traffic Distribution")
        traffic_data = df["input"].apply(lambda x: x["traffic_level"])
        st.bar_chart(traffic_data.value_counts())

    else:
        st.info("No prediction data available yet.")

st.divider()
st.markdown(
    "<center>👨‍💻 Built by Rajesh | ML Engineer Portfolio 🚀</center>",
    unsafe_allow_html=True
)

