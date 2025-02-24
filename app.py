import streamlit as st
import subprocess

def scrape():
    st.write("Scraping tweets...")
    result_miner = subprocess.run(["python", "miner.py"], capture_output=True, text=True)
    st.text(result_miner.stdout)

def analyse():
    st.write("Analyzing tweets...")
    result_analyze = subprocess.run(["python", "analyse.py"], capture_output=True, text=True)
    st.text(result_analyze.stdout)
    st.write(result_analyze.stdout)
    print(result_analyze.stdout)
    st.text("banana")

def start_dashboard():
    st.write("Starting Streamlit dashboard...")
    subprocess.Popen(["python", "-m","streamlit", "run", "dashboard.py"])
    st.success("Dashboard is running!")

st.title("Twitter Sentiment Analyzer")
st.write("Scrape and analyze tweets related to ChatGPT.")

if st.button("Scrape"):
    scrape()
    
if st.button("Analyze"):
    analyse()

if st.button("Start Dashboard"):
    start_dashboard()
 