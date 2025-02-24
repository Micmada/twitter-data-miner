import tweepy
import keys
import json

client = tweepy.Client(bearer_token=keys.Keys.bearer_token)

search_query = 'ChatGPT -from:OpenAI -from:sama -from:miramurati -from:gdb -is:retweet'
tweet_count = 10

tweets = client.search_recent_tweets(query=search_query, max_results=tweet_count, tweet_fields=["created_at", "public_metrics"], user_fields=["username"], expansions="author_id")

data = []
for tweet in tweets.data:
    data.append({
        "username": tweet.author_id,  
        "tweet": tweet.text,
        "created_at": tweet.created_at.isoformat(),
        "likes": tweet.public_metrics["like_count"],
        "retweets": tweet.public_metrics["retweet_count"]
    })

with open("tweets.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("Tweets collected and saved!")

