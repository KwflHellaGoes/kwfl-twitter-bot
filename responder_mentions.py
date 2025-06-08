import tweepy
import os
import json
import random

client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET")
)

bot_username = "kwflhellagoes"

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

replied_file = 'replied_to.json'
if os.path.exists(replied_file):
    with open(replied_file, 'r') as f:
        replied_to = set(json.load(f))
else:
    replied_to = set()

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
            break  # Only reply to one tweet per run
        except Exception as e:
            print(f"❌ Error replying to tweet ID {tweet.id}: {e}")

with open(replied_file, 'w') as f:
    json.dump(list(replied_to), f)
