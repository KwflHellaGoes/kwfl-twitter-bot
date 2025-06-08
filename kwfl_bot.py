

import tweepy
import random
import os
from dotenv import load_dotenv # type: ignore

# Load the environment variables from .env file
load_dotenv()

# Authenticate with Twitter using v2 API
client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET")
)

# List of tweets for the bot to choose from
kwfl_bars = [
    "Lunch don’t wait. Neither do I. #KWFL",
    "Bars hotter than spicy ramen. 🍜 #KWFL",
    "Posted at the Asian food court again. It’s tradition. #KWFL",
    "No crumbs left, just punchlines. #KWFL",
    "Pulled up in the lunch line like it’s halftime. #KWFL"
]

# This function picks a tweet and sends it
def tweet_kwfl():
    tweet = random.choice(kwfl_bars)
    try:
        response = client.create_tweet(text=tweet)
        print(f"Tweeted: {tweet}")
    except Exception as e:
        print("Error tweeting:", e)

# Run the function when you launch the script
if __name__ == '__main__':
    tweet_kwfl()
