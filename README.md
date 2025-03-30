# Game of Thrones Twitter Bot

This bot automatically posts iconic quotes from Game of Thrones on Twitter at regular intervals.

## How It Works
- The bot is built using Python and the `tweepy` library to interact with the Twitter API.
- It selects a random quote from a `quotes.json` file containing Game of Thrones quotes.
- The bot is scheduled to run using PythonAnywhere's scheduled tasks.
- The quotes file is sourced from the [Game of Thrones XYZ API](https://xyzapi.com) (credit to them for the quotes data).

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/harxhe/twitter-bot-python.git
   cd twitter-bot-python
   ```
2. Install dependencies:
   ```bash
   pip install tweepy
   ```
3. Set up Twitter API keys:
   - Get API keys from the Twitter Developer Portal.
   - Create a `.env` file and store your keys:
     ```
     CONSUMER_KEY=your_consumer_key
     CONSUMER_SECRET=your_consumer_secret
     ACCESS_TOKEN=your_access_token
     ACCESS_SECRET=your_access_secret
     ```
4. Run the bot manually:
   ```bash
   python main.py
   ```
5. Deploy on PythonAnywhere:
   - Schedule the script to run at a fixed interval using the built-in task scheduler.

