import os
import random
import datetime
from subprocess import run

now = datetime.datetime.utcnow()
key = '.last_tweet'
should_run = True

if os.path.exists(key):
    with open(key) as f:
        last = datetime.datetime.fromisoformat(f.read().strip())
        delta = (now - last).days
        should_run = delta >= 3

if should_run:
    if random.randint(0, 23) == now.hour:
        run(['python', 'kwfl_bot.py'])
        with open(key, 'w') as f:
            f.write(now.isoformat())
    else:
        print("Skipped: not the random hour")
else:
    print("Skipped: not the 3rd day yet")
