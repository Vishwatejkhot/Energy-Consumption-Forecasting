import streamlit as st
import pandas as pd
import numpy as np
import pickle

from config import get_llm
from agents import energy_forecast_agent, cost_agent, anomaly_agent

st.set_page_config(page_title="Energy AI Assistant", page_icon="⚡", layout="wide")

model = pickle.load(open("Model/xgb_energy_model.pkl", "rb"))
feature_columns = pickle.load(open("Model/feature_columns.pkl", "rb"))

llm = get_llm()

st.title("⚡ Smart Energy AI Assistant")

mode = st.sidebar.selectbox(
    "Assistant Mode",
    ["Energy Advisor", "Cost Optimizer", "Anomaly Detection"]
)

st.sidebar.subheader("🕒 Time Information")

hour = st.sidebar.slider("Hour of Day", 0, 23, 12)
dayofweek = st.sidebar.slider("Day of Week (0 = Monday)", 0, 6, 3)
month = st.sidebar.slider("Month", 1, 12, 6)

st.sidebar.subheader("⚡ Recent Energy Usage")

last_hour_usage = st.sidebar.number_input(
    "Energy used in the last hour (kW)",
    value=1.0
)

two_hours_ago_usage = st.sidebar.number_input(
    "Energy used 2 hours ago (kW)",
    value=1.0
)

yesterday_same_time = st.sidebar.number_input(
    "Energy used yesterday at this same time (kW)",
    value=1.0
)

last_week_same_time = st.sidebar.number_input(
    "Energy used last week at this same time (kW)",
    value=1.0
)

avg_last_24_hours = st.sidebar.number_input(
    "Average energy usage over last 24 hours (kW)",
    value=1.0
)

def create_input():
    df = pd.DataFrame(index=[0])

    df["hour"] = hour
    df["dayofweek"] = dayofweek
    df["month"] = month

    df["hour_sin"] = np.sin(2 * np.pi * hour / 24)
    df["hour_cos"] = np.cos(2 * np.pi * hour / 24)
    df["dow_sin"] = np.sin(2 * np.pi * dayofweek / 7)
    df["dow_cos"] = np.cos(2 * np.pi * dayofweek / 7)

    df["lag_1"] = last_hour_usage
    df["lag_2"] = two_hours_ago_usage
    df["lag_24"] = yesterday_same_time
    df["lag_168"] = last_week_same_time
    df["rolling_mean_24"] = avg_last_24_hours

    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0

    return df[feature_columns]

if st.button("Run Energy Analysis"):

    input_df = create_input()

    pred_log = model.predict(input_df)
    prediction = np.expm1(pred_log)[0]

    st.success(f"Forecasted Next Hour Usage: {prediction:.4f} kW")

    if llm:

        if mode == "Energy Advisor":
            result = energy_forecast_agent(llm, prediction, version="v1")

        elif mode == "Cost Optimizer":
            result = cost_agent(llm, prediction)

        elif mode == "Anomaly Detection":
            result = anomaly_agent(llm, prediction)

        st.markdown("### 🤖 AI Assistant Response")
        st.write(result)

    else:
        st.warning("GROQ_API_KEY not found in environment")