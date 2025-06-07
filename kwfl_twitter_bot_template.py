
import tweepy
import time
import random

# Twitter API credentials
API_KEY = 'miWda3QmMLAqHK7R98RufJ1Tl'
API_SECRET = 'WdIUPm78BCA6psyautxzl7dzHaIJ0DeuOisMrviLRihWiCqMwU'
ACCESS_TOKEN = '1931243241871167488-ujCemYSeUO7G7TDerUT3LZGFU6fsEI'
ACCESS_SECRET = 'tzVtzfhxc1hjMQYxQizYlER8WCzVCJnTtlKAo0oBDFHM8'

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Sample tweets — KWFL style
kwfl_bars = [
    "Lunch don't wait. Neither do I. #KWFL",
    "Bars hotter than spicy ramen. 🍜 #KWFL",
    "Posted at the Asian food court again. It's tradition. #KWFL",
    "No crumbs left, just punchlines. #KWFL",
    "Pulled up in the lunch line like it's halftime. #KWFL"
]

# Function to tweet
def tweet_kwfl():
    tweet = random.choice(kwfl_bars)
    try:
        api.update_status(tweet)
        print(f"Tweeted: {tweet}")
    except Exception as e:
        print("Error tweeting:", e)

# Tweet every 6 hours (optional loop if you want to run it persistently)
if __name__ == '__main__':
    tweet_kwfl()
    # Optional: time.sleep(21600) to run repeatedly
