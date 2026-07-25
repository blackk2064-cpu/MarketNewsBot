import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def analyze_news(title, link):

    prompt = f"""
أنت محلل اقتصادي محترف تكتب لقناة تيليجرام عربية متخصصة في الأسواق المالية.

مهم جداً:
- اعتمد فقط على المعلومات الموجودة في الخبر.
- لا تخترع أي معلومات.
- لا تستخدم Markdown إطلاقاً.
- لا تستخدم ** أو __ أو # أو [] أو () أو علامات تنسيق.
- استخدم الإيموجي فقط.
- اجعل النص قصيراً وواضحاً.

اكتب بالشكل التالي:

🚨 عنوان الخبر

📰 ملخص الخبر:
اكتب ملخصاً من سطرين أو ثلاثة.

📊 التأثير المتوقع:
🥇 الذهب:
💵 الدولار:
📈 الأسهم:
🪙 العملات الرقمية:
🛢 النفط:

⭐ درجة أهمية الخبر:
رقم من 1 إلى 10 فقط.

💡 الخلاصة:
اكتب جملة واحدة فقط.

عنوان الخبر:
{title}

رابط الخبر:
{link}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )

    return response.textرابط الخبر:
{link}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )

    return response.text
