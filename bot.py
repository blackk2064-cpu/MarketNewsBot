import os
import feedparser
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

feeds = [
    "https://www.forexlive.com/feed/",
]

message = "📈 اختبار البوت"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message,
    },
)

print(response.status_code)
print(response.text)
