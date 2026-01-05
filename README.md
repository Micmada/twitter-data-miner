---
description: Sentiment analysis of ChatGPT tweets with Streamlit dashboard
details: >
  Scrapes recent tweets about ChatGPT, analyzes sentiment using TextBlob,
  and displays results in an interactive Streamlit dashboard. Filters by sentiment type.
technologies:
  - python
  - streamlit
  - textblob
  - ai
hostedUrl: 
---


# Twitter ChatGPT Sentiment Analyzer

This project scrapes recent tweets about ChatGPT, performs sentiment analysis on them, and provides a Streamlit-based dashboard to visualize the results.

## Features
- **Scrape tweets** about ChatGPT while excluding OpenAI developers.
- **Analyze sentiment** of tweets using TextBlob.
- **View results** in an interactive dashboard with Streamlit.
- **Filter tweets** by sentiment type.

## Setup & Installation

### 1. Clone the Repository
```sh
git clone https://github.com/Micmada/twitter-chatgpt-sentiment.git
cd twitter-chatgpt-sentiment
```

### 2. Create and Activate a Virtual Environment (Recommended)
```sh
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up API Keys
- Create a `keys.py` file in the project directory.
- Add the following code and replace `YOUR_BEARER_TOKEN` with your actual Twitter API bearer token.
```python
class Keys:
    bearer_token = "YOUR_BEARER_TOKEN"
```

## Usage

### 1. Scrape Tweets
Run the `miner.py` script to fetch recent tweets about ChatGPT:
```sh
python miner.py
```
Tweets will be saved to `tweets.json`.

### 2. Analyze Sentiments
Run the `analyse.py` script to analyze tweet sentiments:
```sh
python analyse.py
```
This will create `tweets_with_sentiment.json` containing sentiment analysis results.

### 3. Run the Streamlit App
Start the main Streamlit interface:
```sh
streamlit run app.py
```
- Click **Scrape** to collect new tweets.
- Click **Analyze** to process sentiment.
- Click **Start Dashboard** to open the visual dashboard.

### 4. View Dashboard
To view the sentiment analysis dashboard directly, run:
```sh
streamlit run dashboard.py
```

## Troubleshooting
- If you get a `TooManyRequests` error, wait a while before making another request.
- Ensure your API keys are valid and correctly set up in `keys.py`.


