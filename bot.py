import os
import re
import requests

from news import get_news
from ai import analyze_news
from storage import is_posted, mark_posted

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

API = f"https://api.telegram.org/bot{TOKEN}/sendMessage"


def clean_text(text):
    text = re.sub(r"[*_`\[\]()~>#]", "", text)
    return text


KEYWORDS = [
    "gold",
    "oil",
    "bitcoin",
    "crypto",
    "fed",
    "inflation",
    "interest",
    "rate",
    "usd",
    "eur",
    "forex",
    "stock",
    "nasdaq",
    "dow",
    "s&p",
    "trump",
    "iran",
    "china",
    "tariff",
]


news = get_news()

print(f"عدد الأخبار: {len(news)}")

for item in news:

    if is_posted(item["link"]):
        continue

    title = item["title"].lower()

    if not any(k in title for k in KEYWORDS):
        print("تم تجاهل الخبر:", item["title"])
        continue

    print("خبر مهم:", item["title"])

    try:
        print("إرسال إلى Gemini...")

        text = analyze_news(item["title"], item["link"])
        text = clean_text(text)

        print("إرسال إلى تيليجرام...")

        response = requests.post(
            API,
            data={
                "chat_id": CHAT_ID,
                "text": text,
            },
        )

        print(response.text)

        if response.json().get("ok"):
            print("✅ تم الإرسال")
            mark_posted(item["link"])
            break
        else:
            print("❌ فشل الإرسال")
            break

    except Exception as e:
        print("حدث خطأ:", e)

        # إذا انتهت حصة Gemini لا تكمل بقية الأخبار
        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
            print("انتهت حصة Gemini، سيتم إيقاف البوت.")
            break

        break
