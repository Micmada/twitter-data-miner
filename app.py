import streamlit as st
import subprocess

def scrape_and_analyze():
    st.write("Scraping tweets...")
    result_miner = subprocess.run(["python", "miner.py"], capture_output=True, text=True)
    st.text(result_miner.stdout)
    
    st.write("Analyzing tweets...")
    result_analyze = subprocess.run(["python", "analyse.py"], capture_output=True, text=True)
    st.text(result_analyze.stdout)
    
    st.success("Scraping and analysis complete!")

def start_dashboard():
    st.write("Starting Streamlit dashboard...")
    subprocess.Popen(["python", "-m","streamlit", "run", "dashboard.py"])
    st.success("Dashboard is running!")

st.title("Twitter Sentiment Analyzer")
st.write("Scrape and analyze tweets related to ChatGPT.")

if st.button("Scrape & Analyze"):
    scrape_and_analyze()

if st.button("Start Dashboard"):
    start_dashboard()
 