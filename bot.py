import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

message = """
📈 أخبار الأسواق العالمية

🇺🇸 مؤشر S&P 500 يتحرك بعد صدور بيانات اقتصادية جديدة.

💵 الدولار يشهد تغيرات أمام العملات الرئيسية.

🪙 بيتكوين تواصل جذب اهتمام المستثمرين.

#الأسواق_العالمية #تداول #اقتصاد
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
