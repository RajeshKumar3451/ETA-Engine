# 🚚 ETA Prediction System (End-to-End ML Engineering Project)

> Production-ready machine learning system for real-time delivery ETA prediction with API, deployment, UI, authentication, and analytics.

---

## 🌐 Live Demo

* 🔮 **Frontend (Streamlit UI):** https://your-streamlit-app-url
* ⚙️ **API Docs (FastAPI):** https://your-api-url/docs

---

## 📌 Overview

This project simulates a **real-world food delivery ETA prediction system** similar to Swiggy/Zomato.

It goes beyond model building by implementing a **complete ML system**:

* Model training
* API serving
* Docker containerization
* Cloud deployment
* Interactive frontend
* Logging & analytics

---

## 🧠 Problem Statement

Predict the **Estimated Time of Arrival (ETA)** for a delivery based on:

* Distance
* Order time
* Traffic conditions
* Preparation time
* Weather
* Delivery partner rating

---

## 🏗️ System Architecture

```text
User → Streamlit UI → FastAPI → ML Model → Prediction
                         ↓
                     Logging → Analytics Dashboard
```

---

## ⚙️ Tech Stack

### 🔹 Machine Learning

* Python, Pandas, Scikit-learn

### 🔹 Backend

* FastAPI (REST API)
* Uvicorn

### 🔹 Frontend

* Streamlit (interactive UI)

### 🔹 DevOps

* Docker (containerization)
* Render (deployment)

### 🔹 Data & Analytics

* JSON logging
* Pandas analytics dashboard

---

## 🚀 Features

* ✅ Real-time ETA prediction API
* ✅ Interactive UI (Streamlit)
* ✅ User authentication (session-based)
* ✅ Input validation & structured requests
* ✅ Dockerized application
* ✅ Cloud deployment (public access)
* ✅ Logging of predictions
* ✅ Analytics dashboard (trends & insights)

---

## 📊 Sample Input

```json
{
  "distance_km": 3.5,
  "order_hour": 13,
  "traffic_level": 4,
  "prep_time": 20,
  "weather": 1,
  "delivery_rating": 4.5
}
```

---

## 📈 Sample Output

```json
{
  "predicted_eta": 29.7
}
```

## 📁 Project Structure

```
ml-eta-project/
│
├── app/                # FastAPI app
├── src/                # ML training & prediction logic
├── model/              # Saved model
├── logs/               # Prediction logs
├── ui_app.py           # Streamlit UI
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🧪 How to Run Locally

### 1️⃣ Clone repo

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run API

```bash
uvicorn app.main:app --reload
```

### 4️⃣ Run UI

```bash
streamlit run ui_app.py
```

---

## 🐳 Run with Docker

```bash
docker build -t eta-app .
docker run -p 8000:8000 eta-app
```

---

## 📊 Analytics Dashboard

Tracks:

* Total predictions
* Average ETA
* Traffic distribution
* Prediction trends

---

## 🔐 Authentication

Simple session-based login system implemented in Streamlit UI.

---

## 💬 Key Learnings

* End-to-end ML system design
* API development & deployment
* Handling semi-structured data (JSON logs)
* Building user-facing ML applications
* Monitoring & analytics
---

## 📌 Future Improvements

* Real-time traffic (Google Maps API)
* Database integration (PostgreSQL)
* CI/CD pipeline
* Model versioning
* Scalable microservices architecture

---

## 👤 Author

**Rajesh Kumar**

---

## ⭐ Support

If you found this useful, consider starring ⭐ the repo!