
import tweepy
import time
import random

# Twitter API credentials
API_KEY = 'OTuRDIdXAtmzCxfNtrkCjUIaJ'
API_SECRET = 'tyVhEkGShmYLSi1LIOP0wXVTwTYPtZ7J7ZstypFP9RPxXSrrXl'
ACCESS_TOKEN = '1931243241871167488-9ThDc3wHBPGQ12MVgFaIdWE9QC0LUf'
ACCESS_SECRET = 'qHPDiIAn2KkvSnaNAB2zkXgoeK31jHEmEEVWKR8uc361s'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAACdC2QEAAAAAzqpr1sVY2PLPYcA8JIHLnKoM89M%3Dbfs5jefyiqhBzMeMMtuIW9M6davarxowAimiUrbz9EtxEtFdIJ'

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
