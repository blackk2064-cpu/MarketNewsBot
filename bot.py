import os
import requests

from news import get_news
from ai import analyze_news
from storage import is_posted, mark_posted

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

API = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

news = get_news()

for item in news:
    if is_posted(item["link"]):
        continue

    try:
        text = analyze_news(item["title"], item["link"])

        requests.post(
            API,
            data={
                "chat_id": CHAT_ID,
                "text": text
            }
        )

        mark_posted(item["link"])
        break

    except Exception as e:
        print(e)
