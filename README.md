# ⚙️ Industrial Predictive Maintenance System

A real-time **AI-powered predictive maintenance platform** that simulates industrial sensor streams, predicts machine health using machine learning, and visualizes system status through an interactive monitoring dashboard.

---

## 🧠 Project Overview

Industrial equipment such as turbines, pumps, and engines produce large amounts of telemetry data. Detecting failures early can prevent costly downtime and catastrophic damage.

This project simulates a **complete predictive maintenance pipeline**, including:

• Sensor data simulation
• Real-time machine learning inference
• Failure prediction (Remaining Useful Life)
• Live monitoring dashboard

The system continuously processes sensor telemetry and predicts the **Remaining Useful Life (RUL)** of machinery.

---

## 🏗️ System Architecture

```
Sensor Simulator
      │
      ▼
MQTT / Streaming Layer
      │
      ▼
Inference Worker (ML Model)
      │
      ▼
Prediction Log Storage
      │
      ▼
Real-Time Monitoring Dashboard
```

### Components

| Component               | Description                              |
| ----------------------- | ---------------------------------------- |
| **Sensor Simulator**    | Generates realistic industrial telemetry |
| **Inference Worker**    | Loads ML model and predicts RUL          |
| **Prediction Logger**   | Stores predictions for visualization     |
| **Streamlit Dashboard** | Real-time monitoring interface           |

---

## 📊 Dashboard Features

The monitoring dashboard provides:

• Real-time machine health metrics
• Remaining Useful Life prediction
• Temperature sensor monitoring
• Vibration monitoring
• Sensor telemetry history
• Machine health alerts

### Dashboard Preview

<img width="1919" height="868" alt="image" src="https://github.com/user-attachments/assets/c525d849-808c-49ad-8e83-ddeaaa13b779" />
<img width="1919" height="761" alt="image" src="https://github.com/user-attachments/assets/4b396b67-3b90-4d70-86ca-e42a8232df23" />
<img width="1909" height="1069" alt="image" src="https://github.com/user-attachments/assets/c5747b24-ef26-4cf0-b4ee-f90e52db41eb" />




```
Live Machine Metrics
 ├─ Remaining Useful Life
 ├─ Temperature
 └─ Vibration

Sensor Telemetry
 ├─ Temperature History
 └─ Vibration History

Health Status Alerts
```

---

## 🤖 Machine Learning Model

The system uses a trained regression model to estimate **Remaining Useful Life (RUL)**.

### Dataset

NASA Turbofan Engine Degradation Dataset

The model learns degradation patterns from sensor signals to estimate how many cycles remain before failure.

### Input Features

```
sensor1 → sensor21
engine operating conditions
statistical rolling features
```

### Output

```
Predicted Remaining Useful Life (RUL)
```

---

## 📁 Project Structure

```
predictive_maintenance/
│
├── api/
│   └── server.py
│
├── dashboard/
│   └── monitoring_app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── rul_model.pkl
│
├── streaming/
│   ├── sensor_simulator.py
│   └── inference_worker.py
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── predict.py
│
└── main.py
```

---

## 🚀 Installation

Clone the repository

```
git clone https://github.com/ojas4414/industrial-predictive-maintenance.git
cd industrial-predictive-maintenance
```

Create environment

```
python -m venv venv
source venv/bin/activate
```

Install dependencies

```
pip install -r predictive_maintenance/requirements.txt
```

---

## ▶️ Running the System

### 1️⃣ Start sensor simulation

```
python predictive_maintenance/streaming/sensor_simulator.py
```

### 2️⃣ Start inference worker

```
python predictive_maintenance/streaming/inference_worker.py
```

### 3️⃣ Launch monitoring dashboard

```
streamlit run predictive_maintenance/dashboard/monitoring_app.py
```

The dashboard will open at:

```
http://localhost:8501
```

---

## ⚠️ Health Status Logic

The system triggers alerts based on predicted RUL.

| RUL   | Status                |
| ----- | --------------------- |
| < 50  | Critical Failure Risk |
| < 120 | Maintenance Required  |
| > 120 | Normal Operation      |

---

## 🛠️ Technologies Used

| Technology   | Purpose                    |
| ------------ | -------------------------- |
| Python       | Core programming           |
| Streamlit    | Dashboard interface        |
| Plotly       | Interactive visualizations |
| Pandas       | Data processing            |
| Scikit-Learn | Machine learning           |
| MQTT         | Streaming architecture     |

---

## 🔮 Future Improvements

• Real industrial sensor integration
• Anomaly detection models
• Failure probability estimation
• Distributed streaming (Kafka)
• Time-series database integration
• Multi-machine monitoring

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Ojas Tulshian**

Electronics and Communication Engineering
Interest areas: AI, Machine Learning, Industrial AI Systems

---

⭐ If you find this project useful, consider giving the repository a star.
