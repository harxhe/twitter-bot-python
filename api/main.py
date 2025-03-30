import tweepy
import requests
from dotenv import load_dotenv
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
    try:
        response = requests.get("https://api.gameofthronesquotes.xyz/v1/author/tyrion", timeout=5)
        response.raise_for_status()  
        
        data = response.json()
        return data.get("sentence", "A Lannister always pays his debts.") 
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}")
        return "A Lannister always pays his debts."  # fallback quote

def create_tweet():
    client=get_client()
    quote= get_quote()

    try:
        client.create_tweet(text=quote)
        print(f"Tweet posted: {quote}")
        return {"status": "success", "tweet": quote}
    except Exception as e:
        print(f"Error posting tweet: {e}")
        return {"status": "error", "message": str(e)}

def handler(request):
    return create_tweet()