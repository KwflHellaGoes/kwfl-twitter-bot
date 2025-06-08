name: KWFL Responder

on:
  schedule:
    - cron: "*/30 * * * *"  # every 30 minutes
  workflow_dispatch:

jobs:
  reply:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install tweepy python-dotenv

      - name: Run responder script
        env:
          API_KEY: ${{ secrets.API_KEY }}
          API_SECRET: ${{ secrets.API_SECRET }}
          ACCESS_TOKEN: ${{ secrets.ACCESS_TOKEN }}
          ACCESS_SECRET: ${{ secrets.ACCESS_SECRET }}
        run: python responder.py
