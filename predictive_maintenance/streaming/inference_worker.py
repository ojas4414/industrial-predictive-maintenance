import json
import pandas as pd
import joblib
from pathlib import Path
import paho.mqtt.client as mqtt
import csv
import time

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "rul_model.pkl"
LOG_PATH = BASE_DIR / "prediction_log.csv"

model = joblib.load(MODEL_PATH)

BROKER = "localhost"
PORT = 1883
TOPIC = "factory/machine1/sensors"

FEATURE_ORDER = [
"setting1","setting2","setting3",
"sensor1","sensor2","sensor3","sensor4","sensor5",
"sensor6","sensor7","sensor8","sensor9","sensor10",
"sensor11","sensor12","sensor13","sensor14","sensor15",
"sensor16","sensor17","sensor18","sensor19","sensor20","sensor21"
]

def log_prediction(prediction, sensors):

    file_exists = LOG_PATH.exists()

    with open(LOG_PATH,"a",newline="") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp","predicted_RUL"] + list(sensors.keys()))

        writer.writerow([time.time(),prediction] + list(sensors.values()))

def on_message(client, userdata, msg):

    data = json.loads(msg.payload.decode())

    ordered = {k:data[k] for k in FEATURE_ORDER}
    df = pd.DataFrame([ordered])

    engineered = {}

    for col in df.columns:
        engineered[col] = df[col].iloc[0]

    for col in df.columns:
        engineered[f"{col}_mean"] = df[col].mean()
        engineered[f"{col}_std"] = df[col].std()

    features_df = pd.DataFrame([engineered])

    prediction = model.predict(features_df)[0]

    log_prediction(float(prediction), ordered)

    print("Predicted RUL:", prediction)

client = mqtt.Client()
client.connect(BROKER, PORT)

client.subscribe(TOPIC)
client.on_message = on_message

print("Inference worker listening...")

client.loop_forever()