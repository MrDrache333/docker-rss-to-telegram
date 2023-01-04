import json
import logging
import os
import ssl
import time

import feedparser
import requests

# Configuration file path
CONFIG_FILE = "config.json"


def load_config():
    # Load the configuration file, if it exists
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
    else:
        # Create an empty configuration file if it does not exist
        config = {}
        save_config(config)

    return config


def save_config(config):
    # Save the configuration to the configuration file
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)


def fetch_rss(url):
    # Parse the RSS feed
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
    feed = feedparser.parse(url)

    return feed["items"]


def send_items(items, bot_token, chat_id):
    # Get the timestamp of the last sent message, if it exists
    last_timestamp = config.get("last_timestamp", None)

    # Iterate through the items in the RSS feed
    for item in items:
        # Get the timestamp and link of the item
        timestamp = item["published_parsed"]
        link = item["link"]

        # Convert the timestamp of the feed item to a Unix timestamp
        unix_timestamp = time.mktime(timestamp)

        # Check if the item has a newer timestamp than the last sent message
        if last_timestamp is None or unix_timestamp > last_timestamp:
            # Get the title and content of the item
            title = item["title"]
            content = item["summary"]
            published = item["published"]

            # Create the message in Markdown format
            message = f"*{title}*\n_{published}_\n\n{content}\n\n[Read full article]({link})"

            url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=MARKDOWN"
            request = requests.get(url)
            if request.status_code != 200:
                print("Error sending the Message")

    # Update the last sent timestamp
    config["last_timestamp"] = time.time()
    save_config(config)


if __name__ == '__main__':
    while True:
        # Load the configuration
        config = load_config()

        # Set up logging
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

        # Check if the required environment variables are set
        if "FEED_URL" not in os.environ or "TELEGRAM_BOT_TOKEN" not in os.environ or "TELEGRAM_CHAT_ID" not in os.environ:
            logging.error("Missing required environment variables")
            exit(1)
        # Get the RSS feed
        news = fetch_rss(os.getenv("FEED_URL"))

        # Send the items in the feed to Telegram
        send_items(news, os.getenv("TELEGRAM_BOT_TOKEN"), os.getenv("TELEGRAM_CHAT_ID"))

        # Sleep for 1 hour
        time.sleep(3600)
