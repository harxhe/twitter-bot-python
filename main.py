import tweepy
from dotenv import load_dotenv
import json
import random
import os

def get_client():
    load_dotenv()
    CONSUMER_KEY = os.getenv("CONSUMER_KEY")
    CONSUMER_SECRET= os.getenv("CONSUMER_SECRET")
    ACCESS_TOKEN= os.getenv("ACCESS_TOKEN")
    ACCESS_SECRET= os.getenv("ACCESS_SECRET")

    client = tweepy.Client(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET
    )

    return client

def get_quote():
    with open("quotes.json", "r", encoding="utf-8") as file:
        quotes = json.load(file)

    # Select a random quote from the database
    quote = random.choice(quotes)
    tweet = f"{quote['sentence']} - {quote['character'].capitalize()}"

    return tweet 

def create_tweet():
    client = get_client()
    
    for _ in range(3):  # Retry up to 3 times if duplicate error occurs
        quote = get_quote()
        try:
            client.create_tweet(text=quote)
            print(f"Tweet posted: {quote}")
            return {"status": "success", "tweet": quote}
        except tweepy.errors.Forbidden as e:
            if "duplicate content" in str(e).lower():
                print("Duplicate tweet detected. Retrying...")
                continue  # Retry with a new quote
            else:
                print(f"Error posting tweet: {e}")
                return {"status": "error", "message": str(e)}
    
    print("All retries failed. No unique tweet found.")
    return {"status": "error", "message": "All retries failed due to duplicate tweets."}

if __name__ == "__main__":
    create_tweet()