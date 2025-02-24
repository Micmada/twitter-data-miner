import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt

with open("tweets_with_sentiment.json", "r", encoding="utf-8") as f:
    tweets = json.load(f)

df = pd.DataFrame(tweets)

st.title("ChatGPT Sentiment Analysis Dashboard")

st.subheader("Raw Tweet Data")
st.dataframe(df[["tweet", "sentiment"]])

st.subheader("Sentiment Distribution")
sentiment_counts = df["sentiment"].value_counts()

fig, ax = plt.subplots()
ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", colors=["green", "red", "gray"])
st.pyplot(fig)

sentiment_filter = st.selectbox("Filter by Sentiment", ["All", "Positive", "Negative", "Neutral"])
if sentiment_filter != "All":
    filtered_df = df[df["sentiment"] == sentiment_filter]
    st.dataframe(filtered_df[["username", "tweet"]])

