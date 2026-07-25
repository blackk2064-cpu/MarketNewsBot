import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def analyze_news(title, link):
    prompt = f"""
أنت محلل مالي محترف.

حلل الخبر التالي واكتب النتيجة بالعربية بهذا التنسيق:

🚨 عنوان الخبر

📰 ملخص الخبر (3 أسطر)

📊 التأثير المتوقع:
- الذهب
- الدولار
- الأسهم
- العملات الرقمية

⭐ قوة التأثير من 1 إلى 10

هاشتاقات مناسبة.

الخبر:
{title}

الرابط:
{link}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
