import os
import requests

from news import get_news
from ai import analyze_news
from storage import is_posted, mark_posted
from filters import KEYWORDS

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

API = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

news = get_news()

print(f"عدد الأخبار: {len(news)}")

for item in news:
    title = item["title"]

    # تجاهل الأخبار غير المهمة
    if not any(keyword.lower() in title.lower() for keyword in KEYWORDS):
        print(f"تم تجاهل الخبر: {title}")
        continue

    print(f"خبر مهم: {title}")

    # تجاهل الأخبار المنشورة سابقًا
    if is_posted(item["link"]):
        print("تم نشره سابقًا")
        continue

    try:
        print("إرسال إلى Gemini...")

        text = analyze_news(item["title"], item["link"])

        print("إرسال إلى تيليجرام...")

        response = requests.post(
            API,
            data={
                "chat_id": CHAT_ID,
                "text": text,
                "parse_mode": "Markdown"
            }
        )

        print(response.text)

        if response.status_code == 200:
            mark_posted(item["link"])
            print("✅ تم نشر الخبر بنجاح")
            break
        else:
            print("❌ فشل إرسال الرسالة")
            print(response.text)

    except Exception as e:
        print(f"حدث خطأ: {e}")
