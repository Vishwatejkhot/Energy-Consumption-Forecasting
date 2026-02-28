# ⚡ Smart Energy AI Assistant

An intelligent hybrid AI system that combines:

-   📈 XGBoost time-series forecasting\
-   🤖 Groq LLM  insights\
-   🧠 Multi-agent architecture\
-   🎛️ Streamlit interactive dashboard

This project predicts next-hour household energy consumption and
provides AI-powered analysis, cost estimation, and anomaly detection.

------------------------------------------------------------------------

## 🚀 Features

-   Time-series energy forecasting (XGBoost)
-   Prompt versioning system
-   Multi-agent architecture
    -   Energy Advisor
    -   Cost Optimizer
    -   Anomaly Detection
-   Structured system + human prompts
-   Modular architecture
-   Environment-based API key management
-   Non-technical UI for general users

------------------------------------------------------------------------

## 📂 Project Structure

Energy_Consumption_Forecasting/

├── app.py\
├── config.py\
├── prompts.py\
├── agents.py\
├── requirements.txt\
├── .env\
├── README.md

├── Notebook/\
│ └── power_consumption.ipynb

└── Models/\
    ├── xgb_energy_model.pkl\
    └── feature_columns.pkl

------------------------------------------------------------------------

## ⚙️ Installation

Using uv:

uv -r requirements.txt

Using pip:

pip install -r requirements.txt

------------------------------------------------------------------------

## 🔐 Environment Setup

Create a `.env` file in the root directory:

GROQ_API_KEY=your_actual_groq_api_key

------------------------------------------------------------------------

## ▶️ Run the Application

streamlit run app.py

Then open the local URL shown in your terminal.

------------------------------------------------------------------------

## 🧠 How It Works

1.  User inputs recent energy usage\
2.  XGBoost predicts next-hour consumption\
3.  Based on selected mode:
    -   Energy Advisor → Efficiency recommendations\
    -   Cost Optimizer → Estimated cost + savings\
    -   Anomaly Detection → Detect unusual spikes\
4.  Groq LLM generates structured insights

------------------------------------------------------------------------

## 🏗 Architecture Overview

-   Machine Learning Layer → XGBoost forecasting\
-   LLM Layer → Groq (Llama 3)\
-   Prompt Layer → Version-controlled prompts\
-   Agent Layer → Specialized AI agents\
-   UI Layer → Streamlit

This is a hybrid ML + GenAI system.

------------------------------------------------------------------------

## 📦 Requirements

-   streamlit\
-   xgboost\
-   pandas\
-   numpy\
-   langchain\
-   langchain-core\
-   langchain-groq\
-   groq\
-   python-dotenv

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Chat-based conversational assistant\
-   LangGraph orchestration\
-   Real-time CSV ingestion\
-   Vector database for energy bill analysis\
-   Model versioning\
-   Cloud deployment

------------------------------------------------------------------------

## 📌 Authors

Vishwatej Khot\
Bhavika Salunkhe

Energy Forecasting + AI Assistant System
