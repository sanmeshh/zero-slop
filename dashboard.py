import streamlit as st
import requests
import random

st.set_page_config(page_title="System 1: AI Slop Engine", layout="wide", page_icon="🧠")

st.title("🧠 System 1 Neural Engine: AI Slop Detector")
st.caption("Based on Laya, multilingual, non-autoregressive System 1 decision engine")
st.divider()

MOCK_POST_SLOP = """In today's fast-paced digital landscape, staying ahead is no longer an option. 🚀

Delve deep into what truly matters. It is a testament to our team's relentless hustle and execution paradigms. ✨

Buckle up, because this new framework will completely revolutionize your cross-functional cloud synergy workflows! 💎

Look no further for your next corporate game-changer. Tap the link below to unlock your scaling potential! 👇"""

col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("Target LinkedIn Post")
    input_text = st.text_area("", MOCK_POST_SLOP, height=220)
    trigger_analyze = st.button("Run", type="primary", use_container_width=True)

with col2:
    st.subheader("Model Performance")
    
    if trigger_analyze:
        with st.spinner("Executing"):
            try:
                simulated_latency = round(random.uniform(31.2, 34.8), 2)
                
                
                response = requests.post(
                    "http://127.0.0.1:8000/predict",
                    json={"state": input_text},
                    timeout=60
                )
                
                if response.status_code == 200:
                    metrics = response.json()
                    
                    if "AI SLOP" in metrics["verdict"]:
                        st.error(f"### {metrics['verdict']}")
                    else:
                        st.success(f"### {metrics['verdict']}")
                    
                    kpi1, kpi2, kpi3 = st.columns(3)
                    kpi1.metric(label="Slop Probability", value=metrics["slop_probability"])
                    kpi2.metric(label="Model Confidence", value=metrics["confidence"])
                    
                    
                    st.divider()
                    
                    
                else:
                    st.error(f"Backend Engine returned a processing exception: {response.text}")

            # CATCH TIMEOUT SEPARATELY
            except requests.exceptions.Timeout:
                st.error("The model inference took too long and timed out (>60s). If running on CPU, initial cold starts can take longer.")

            except requests.exceptions.ConnectionError:
                st.error("Could not reach backend framework. Please ensure your FastAPI script (`app.py`) is executing on port 8000.")
    else:
        st.info("System Idle. Click 'Run'")
