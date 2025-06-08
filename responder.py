import tweepy
import os
import json
import random
from datetime import datetime

# Authenticate with Twitter
client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET")
)

# KWFL-style replies
kwfl_replies = [
    "Pulled up just in time, Lunch Time King. 🍽️ Get that big fat gyro, no crumbs left. #KWFL",
    "Lunch bar coming in hot: Cane’s 3-Finger Combo, no slaw, extra toast. 🔥 #KWFL",
    "Today feels like a CAVA bowl day. Build it like a verse — layered, bold, balanced. 🎤🥗 #KWFL",
    "Posted at the Asian food court again. It’s tradition. 🍜👑 #KWFL",
    "You already know, Lunch Time King — Double-Double plain with Animal Style fries. 🍔🍟 #KWFL"
]

# Track replies
replied_file = 'replied_to.json'
if os.path.exists(replied_file):
    with open(replied_file, 'r') as f:
        replied_to = set(json.load(f))
else:
    replied_to = set()

# Search for tweets containing "what should I eat"
query = '"what should I eat" -is:retweet -from:kwflhellagoes'
tweets = client.search_recent_tweets(query=query, max_results=10, tweet_fields=["author_id", "created_at"])

if tweets.data:
    for tweet in tweets.data:
        if str(tweet.id) in replied_to:
            continue
        try:
            reply_text = random.choice(kwfl_replies)
            client.create_tweet(in_reply_to_tweet_id=tweet.id, text=reply_text)
            print(f"✅ Replied to tweet ID {tweet.id}")
            replied_to.add(str(tweet.id))
        except Exception as e:
            print(f"❌ Error replying to tweet ID {tweet.id}: {e}")

# Save updated reply history
with open(replied_file, 'w') as f:
    json.dump(list(replied_to), f)
