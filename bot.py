import os
import feedparser
from telegram import Bot

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

bot = Bot(token=TOKEN)

feeds = [
    "https://www.forexlive.com/feed/",
    "https://www.investing.com/rss/news.rss",
]

message = "📈 أهم أخبار الأسواق العالمية\n\n"

for feed in feeds:
    data = feedparser.parse(feed)
    for item in data.entries[:3]:
        message += f"• {item.title}\n{item.link}\n\n"

bot.send_message(chat_id=CHAT_ID, text=message)
