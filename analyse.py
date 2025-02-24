import json
from textblob import TextBlob
import sys


with open("tweets.json", "r", encoding="utf-8") as f:
    tweets = json.load(f)
    sys.stdout.write(tweets)

def analyse_sentiment(text):
    analysis = TextBlob(text)
    return "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"

for tweet in tweets:
    tweet["sentiment"] = analyse_sentiment(tweet["tweet"])
    
with open("tweets_with_sentiment.json", "a", encoding="utf-8") as f:
    json.dump(tweets, f, indent=4)
    
print("Sentiment analysis completed! Results saved to tweets_with_sentiment.json.")