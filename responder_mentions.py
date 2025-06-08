import tweepy
import os
import json
import random

# Authenticate using OAuth 1.0a
auth = tweepy.OAuth1UserHandler(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET"),
    os.getenv("ACCESS_TOKEN"),
    os.getenv("ACCESS_SECRET")
)
api = tweepy.API(auth)

# KWFL bars
kwfl_replies = [
    "Lunch don’t wait. Neither do I. 👑🍴 #KWFL",
    "Get that Big Fat Gyro and walk like a meal king. 💨 #KWFL",
    "Pull up to CAVA like you're building a mixtape. Layers on layers. 🥗🎶 #KWFL",
    "Cane’s 3-Finger Combo. No slaw. Extra toast. Classic. 🔥🍗 #KWFL",
    "Order like you’re headlining the food court. Pad Thai, extra heat. 🌶️🍜 #KWFL",
    "Lunch break’s a runway — Double-Double plain, animal-style fries. 🍔🍟 #KWFL",
    "Big bowl energy. Chipotle, heavy on the guac, bars extra. 🥑💬 #KWFL",
    "No crumbs left — just greatness. Try that fried chicken banh mi. 🥖🔥 #KWFL",
    "Lunch hits different with oxtail and plantains. If you know, you know. 🍛👑 #KWFL",
    "Takeout flex: sesame chicken, side of wontons, extra sauce. 🥡💦 #KWFL",
    "Smash that poke bowl like a freestyle — raw, clean, and layered. 🐟🎤 #KWFL",
    "Lunch Time King eats like every bite is an intro. Get the gyro. 🥙🎧 #KWFL",
    "Back to the Asian food court. You know how I do. 🍜📍 #KWFL",
    "Sushi at noon, bars by 2. Keep it rollin’. 🍣🌀 #KWFL",
    "Feeling reckless? Nashville hot with pickles. Tongue on tilt. 🔥🥵 #KWFL",
    "Lunch like it’s halftime: pizza slice, wings, and a soda freestyle. 🍕🍗🥤 #KWFL",
    "Elevate the midday. Falafel wrap, tabbouleh, and bars. 🌯📈 #KWFL",
    "This isn’t a craving, it’s a prophecy: go shawarma or go home. 🔮🥙 #KWFL",
    "Spin the lunch wheel: today it's Thai green curry. Bring the heat. 🥵🇹🇭 #KWFL",
    "You didn’t come this far to microwave something. Let’s eat right. 👑🍽️ #KWFL",
    "Mac and cheese with confidence. Add brisket, walk off. 🧀🔥 #KWFL",
    "KBBQ calling. Lunch should sizzle. 🥓🔥 #KWFL",
    "You know it’s a good lunch if it needs two napkins and a recovery plan. 🧻💥 #KWFL"
]

# Track already replied tweet IDs
replied_file = 'replied_to.json'
if os.path.exists(replied_file):
    with open(replied_file, 'r') as f:
        replied_to = set(json.load(f))
else:
    replied_to = set()

# Get latest mentions
mentions = api.mentions_timeline(count=10)

for tweet in mentions:
    tweet_id = str(tweet.id)
    if tweet_id in replied_to:
        continue
    if "kwfl" not in tweet.text.lower():
        continue

    try:
        reply_text = f"@{tweet.user.screen_name} " + random.choice(kwfl_replies)
        api.update_status(status=reply_text, in_reply_to_status_id=tweet.id)
        print(f"✅ Replied to tweet ID: {tweet.id}")
        replied_to.add(tweet_id)
        break  # only reply to one per run
    except Exception as e:
        print(f"❌ Error replying to tweet ID {tweet.id}: {e}")

# Save updated list
with open(replied_file, 'w') as f:
    json.dump(list(replied_to), f)
