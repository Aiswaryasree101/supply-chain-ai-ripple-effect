import streamlit as st
import pandas as pd
import subprocess

st.set_page_config(layout="wide")

st.title("AI-Driven Supply Chain Resilience Dashboard")

mode = st.selectbox("Select Strategy", ["Baseline", "AI"])

if st.button("Run Simulation"):
    if mode == "Baseline":
        subprocess.run(["python", "evaluation/run_baseline.py"])
        file = "evaluation/baseline_results.csv"
    else:
        subprocess.run(["python", "evaluation/run_ai_eval.py"])
        file = "evaluation/ai_results.csv"

    df = pd.read_csv(file, header=None, names=["Cost", "Unmet Demand"])

    st.success("Simulation completed")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Average Cost", round(df["Cost"].mean(),2))

    with col2:
        st.metric("Average Unmet Demand", round(df["Unmet Demand"].mean(),2))

    st.subheader("Episode Results")
    st.dataframe(df)

    st.subheader("Performance Charts")
    st.line_chart(df)
