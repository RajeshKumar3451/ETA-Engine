import streamlit as st
import requests
import time
import pandas as pd
import json
import os

API_URL = "https://eta-prediction-api.onrender.com/predict"

st.set_page_config(page_title="ETA System", page_icon="🚚", layout="wide")

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
.center-box {
    display: flex;
    justify-content: center;
    align-items: center;
}
.login-card {
    background-color: #1c1f26;
    padding: 30px;
    border-radius: 12px;
    width: 350px;
}
</style>
""", unsafe_allow_html=True)

users = {
    "admin": "1234",
    "rajesh": "ml123",
    "raj": "5313"
}

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<div class='center-box'>", unsafe_allow_html=True)
    st.markdown("<div class='login-card'>", unsafe_allow_html=True)

    st.markdown("## 🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.auth = True
            st.session_state.user = username
            st.rerun()
        else:
            st.error("Invalid credentials")

    st.markdown("</div></div>", unsafe_allow_html=True)
    st.stop()

st.title("🚚 ETA Prediction System")
st.caption(f"Welcome, {st.session_state.user} 👋")

try:
    requests.get(API_URL.replace("/predict", "/"), timeout=2)
    st.success("✅ Backend Connected")
except:
    st.error("❌ API Not Reachable")

st.divider()

tab1, tab2 = st.tabs(["🔮 Prediction", "📊 Analytics"])

with tab1:

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📥 Input Features")

        distance = st.slider("📍 Distance (km)", 0.5, 10.0, 3.0)
        hour = st.slider("🕒 Order Hour", 0, 23, 13)
        traffic = st.slider("🚦 Traffic Level", 1, 5, 3)
        prep = st.slider("🍽️ Prep Time (min)", 5, 40, 20)
        weather = st.selectbox("🌦️ Weather", [1, 2, 3])
        rating = st.slider("⭐ Delivery Rating", 1.0, 5.0, 4.5)

    payload = {
        "Distance (km)": distance,
        "Order Hour": hour,
        "Traffic Level": traffic,
        "Prep Time": prep,
        "Weather": weather,
        "Rating": rating
    }

    rounded_payload = {
        k: round(v, 2) if isinstance(v, float) else v
        for k, v in payload.items()
    }

    with col2:
        st.subheader("📊 Input Summary")
        st.table({
            "Feature": list(rounded_payload.keys()),
            "Value": list(rounded_payload.values())
        })

    st.subheader("🚀 Prediction")

    if st.button("Predict ETA"):
        with st.spinner("Calculating ETA..."):
            try:
                response = requests.post(API_URL, json={
                    "distance_km": distance,
                    "order_hour": hour,
                    "traffic_level": traffic,
                    "prep_time": prep,
                    "weather": weather,
                    "delivery_rating": rating
                }, timeout=10)

                result = response.json()
                time.sleep(1)

                eta = round(result["predicted_eta"], 2)

                st.metric("⏱️ Estimated Delivery Time", f"{eta} min")

                if eta < 25:
                    st.success("🚀 Fast delivery")
                elif eta < 40:
                    st.warning("⏳ Moderate time")
                else:
                    st.error("🚦 Delay expected")

                os.makedirs("logs", exist_ok=True)
                with open("logs/ui_log.json", "a") as f:
                    f.write(json.dumps({
                        "input": rounded_payload,
                        "prediction": eta
                    }) + "\n")

            except:
                st.error("⚠️ API error")


with tab2:
    st.subheader("📊 Analytics Dashboard")

    log_file = "logs/ui_log.json"

    if os.path.exists(log_file):

        df = pd.read_json(log_file, lines=True)

        col1, col2 = st.columns(2)
        col1.metric("Total Predictions", len(df))
        col2.metric("Avg ETA", round(df["prediction"].mean(), 2))

        st.markdown("### 📈 Prediction Trend")
        st.line_chart(df["prediction"])

        st.markdown("### 🚦 Traffic Distribution")
        traffic_data = df["input"].apply(lambda x: x["Traffic Level"])
        st.bar_chart(traffic_data.value_counts())

    else:
        st.info("No data available yet")

st.divider()
st.markdown(
    "<center>👨‍💻 Built by Rajesh | ML Engineer Project 🚀</center>",
    unsafe_allow_html=True
)
