import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def analyze_news(title, link):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="قل مرحبًا فقط."
    )
    return response.text
