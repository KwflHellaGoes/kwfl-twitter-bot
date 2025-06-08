import tweepy
import os
import json
import random

# Authenticate with Twitter API v2 using OAuth 1.0a
client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET")
)

# Bot username (no @ symbol)
bot_username = "kwflhellagoes"

# Replies to use
kwfl_replies = [
    "Lunch don’t wait. Neither do I. 👑🍴 #KWFL",
    "Get that Big Fat Gyro and walk like a meal king. 💨 #KWFL",
    "Pull up to CAVA like you're building a mixtape. Layers on layers. 🥗🎶 #KWFL",
    "Cane’s 3-Finger Combo. No slaw. Extra toast. Classic. 🔥🍗 #KWFL",
    "Order like you’re headlining the food court. Pad Thai, extra heat. 🌶️🍜 #KWFL"
]

# Track already replied tweets
replied_file = 'replied_to.json'
if os.path.exists(replied_file):
    with open(replied_file, 'r') as f:
        replied_to = set(json.load(f))
else:
    replied_to = set()

# Get recent mentions
me = client.get_user(username=bot_username).data.id
mentions = client.get_users_mentions(id=me, max_results=10)

if mentions.data:
    for tweet in mentions.data:
        tweet_id = str(tweet.id)
        text_lower = tweet.text.lower()

        if tweet_id in replied_to:
            continue
        if "kwfl" not in text_lower:
            continue

        try:
            response = random.choice(kwfl_replies)
            client.create_tweet(in_reply_to_tweet_id=tweet.id, text=response)
            print(f"✅ Replied to tweet ID: {tweet.id}")
            replied_to.add(tweet_id)
        except Exception as e:
            print(f"❌ Error replying to tweet ID {tweet.id}: {e}")

# Save updated list
with open(replied_file, 'w') as f:
    json.dump(list(replied_to), f)