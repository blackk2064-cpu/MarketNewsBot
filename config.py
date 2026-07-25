import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

RSS_FEEDS = [
    "https://www.forexlive.com/feed/",
    "https://finance.yahoo.com/rss/topstories",
    "https://www.fxstreet.com/rss/news",
]
