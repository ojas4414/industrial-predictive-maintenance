import streamlit as st
import requests
import random
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
from pathlib import Path

API_URL="http://127.0.0.1:8000/predict"

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_PATH = BASE_DIR / "prediction_log.csv"

st.set_page_config(page_title="Predictive Maintenance Control Center",layout="wide")

st_autorefresh(interval=2000,key="refresh")

st.title("⚙ Industrial Predictive Maintenance Control Center")

sensor_data={
"setting1":random.random(),
"setting2":random.random(),
"setting3":100,
"sensor1":random.uniform(500,550),
"sensor2":random.uniform(600,650),
"sensor3":random.uniform(1500,1600),
"sensor4":random.uniform(1300,1400),
"sensor5":random.uniform(10,20),
"sensor6":random.uniform(20,30),
"sensor7":random.uniform(500,600),
"sensor8":2388,
"sensor9":random.uniform(800,900),
"sensor10":random.uniform(1,2),
"sensor11":random.uniform(40,50),
"sensor12":random.uniform(500,550),
"sensor13":2388,
"sensor14":random.uniform(8000,9000),
"sensor15":random.uniform(8,9),
"sensor16":random.uniform(0,0.1),
"sensor17":random.uniform(380,420),
"sensor18":2388,
"sensor19":100,
"sensor20":random.uniform(35,45),
"sensor21":random.uniform(20,30)
}

try:
    r=requests.post(API_URL,json=sensor_data)
    rul=r.json()["predicted_RUL"]
except:
    rul=0

temperature=sensor_data["sensor2"]
vibration=sensor_data["sensor9"]

col1,col2,col3=st.columns(3)

with col1:
    st.metric("Remaining Useful Life",round(rul,2))

with col2:
    st.metric("Temperature",round(temperature,2))

with col3:
    st.metric("Vibration",round(vibration,2))

if LOG_PATH.exists():

    df=pd.read_csv(LOG_PATH)

    fig1=go.Figure()
    fig1.add_trace(go.Scatter(y=df["predicted_RUL"],mode="lines"))
    fig1.update_layout(title="RUL Prediction History",template="plotly_dark")

    st.plotly_chart(fig1,use_container_width=True,key="rul_history")

    if "sensor2" in df.columns:

        fig2=go.Figure()
        fig2.add_trace(go.Scatter(y=df["sensor2"],mode="lines"))
        fig2.update_layout(title="Temperature History",template="plotly_dark")

        st.plotly_chart(fig2,use_container_width=True,key="temp_history")

    if "sensor9" in df.columns:

        fig3=go.Figure()
        fig3.add_trace(go.Scatter(y=df["sensor9"],mode="lines"))
        fig3.update_layout(title="Vibration History",template="plotly_dark")

        st.plotly_chart(fig3,use_container_width=True,key="vib_history")

gauge=go.Figure(go.Indicator(
mode="gauge+number",
value=rul,
title={"text":"Engine Health"},
gauge={
"axis":{"range":[0,200]},
"steps":[
{"range":[0,50],"color":"red"},
{"range":[50,100],"color":"orange"},
{"range":[100,200],"color":"green"}
]
}
))

st.plotly_chart(gauge,use_container_width=True,key="health_gauge")

if rul<50:
    st.error("CRITICAL: Engine failure likely soon")

elif rul<100:
    st.warning("Maintenance recommended soon")

else:
    st.success("Engine operating normally")