import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from streamlit_autorefresh import st_autorefresh


st_autorefresh(interval=2000, key="refresh")

st.set_page_config(
    page_title="Industrial Predictive Maintenance",
    layout="wide"
)


st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Rajdhani:wght@400;600&display=swap');

/* -------- LIGHT TECH BACKGROUND -------- */

html, body, [class*="css"] {
    font-family:'Rajdhani',sans-serif;
    color:white;

    background-image:url("https://www.transparenttextures.com/patterns/cubes.png");
    background-color:#0a3a66;

    background-size:300px;
}

/* -------- MAIN PANEL -------- */

.main .block-container{
    background:rgba(0,20,50,0.45);
    padding:40px;
    border-radius:18px;
    backdrop-filter: blur(4px);
}

/* -------- TITLE -------- */

.title-box{
    background:linear-gradient(90deg,#00c6ff,#0072ff);
    padding:25px;
    border-radius:16px;
    text-align:center;
    box-shadow:0px 0px 25px rgba(0,170,255,0.7);
    margin-bottom:25px;
}

.title-box h1{
    font-family:'Orbitron',sans-serif;
    font-size:42px;
    letter-spacing:2px;
}

/* -------- SECTION LABELS -------- */

.section-box{
    background:rgba(0,50,120,0.45);
    border:1px solid rgba(0,200,255,0.6);
    padding:12px;
    border-radius:12px;
    text-align:center;
    font-size:22px;
    margin-top:25px;
    margin-bottom:15px;
}

/* -------- METRIC COLORS -------- */

[data-testid="stMetricValue"]{
    color:#9be7ff;
    font-size:36px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-box">
<h1>Industrial Predictive Maintenance Control Center</h1>
</div>
""", unsafe_allow_html=True)


BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "prediction_log.csv"

if not csv_path.exists():
    st.error("Prediction log not found. Run inference_worker first.")
    st.stop()

df = pd.read_csv(csv_path)
latest = df.iloc[-1]

rul = latest["predicted_RUL"]
temperature = latest["sensor11"]
vibration = latest["sensor12"]


st.markdown('<div class="section-box">Live Machine Metrics</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=rul,
        title={'text': "Remaining Useful Life"},
        gauge={
            'axis': {'range':[0,300]},
            'bar': {'color':"lightgreen"},
            'steps':[
                {'range':[0,50],'color':'red'},
                {'range':[50,120],'color':'orange'},
                {'range':[120,300],'color':'green'}
            ]
        }
    ))

    st.plotly_chart(fig,use_container_width=True)

with col2:

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=temperature,
        title={'text': "Temperature"},
        gauge={
            'axis': {'range':[0,100]},
            'bar': {'color':'cyan'}
        }
    ))

    st.plotly_chart(fig,use_container_width=True)

with col3:

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=vibration,
        title={'text': "Vibration"},
        gauge={
            'axis': {'range':[0,600]},
            'bar': {'color':'lime'}
        }
    ))

    st.plotly_chart(fig,use_container_width=True)


st.markdown('<div class="section-box">Sensor Telemetry</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:

    fig = px.line(
        df,
        y="sensor11",
        title="Temperature History"
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(fig,use_container_width=True)

with c2:

    fig = px.line(
        df,
        y="sensor12",
        title="Vibration History"
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(fig,use_container_width=True)


st.markdown('<div class="section-box">Remaining Useful Life Trend</div>', unsafe_allow_html=True)

fig = px.line(
    df,
    y="predicted_RUL",
    title="Predicted Remaining Useful Life"
)

fig.update_layout(template="plotly_dark")

st.plotly_chart(fig,use_container_width=True)



st.markdown('<div class="section-box">Engine Health Status</div>', unsafe_allow_html=True)

if rul < 50:
    st.error("⚠️ CRITICAL: Machine Failure Imminent")

elif rul < 120:
    st.warning("⚠️ Maintenance Required Soon")

else:
    st.success("✔ Machine Operating Normally")
