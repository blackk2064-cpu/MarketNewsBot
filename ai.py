import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def analyze_news(title, link):
    prompt = f"""
أنت محلل اقتصادي محترف يكتب لقناة تيليجرام عربية.

اعتمد فقط على المعلومات الموجودة في الخبر، ولا تخترع حقائق.

اكتب المنشور بهذا الشكل:

🚨 عنوان مختصر وجذاب

📰 ملخص الخبر
(سطرين أو ثلاثة)

📊 التأثير المتوقع
🥇 الذهب:
💵 الدولار:
📈 الأسهم:
🪙 العملات الرقمية:
🛢️ النفط:

⭐ درجة أهمية الخبر: من 1 إلى 10

💡 الخلاصة:
جملة واحدة تلخص أهم ما يجب أن يعرفه المستثمر.

#اقتصاد #الأسواق_العالمية

عنوان الخبر:
{title}

رابط الخبر:
{link}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )

    return response.text
