news = get_news()

print(f"عدد الأخبار: {len(news)}")

for item in news:
    print(item["title"])

    if is_posted(item["link"]):
        print("تم نشره سابقًا")
        continue

    print("إرسال إلى Gemini...")

    text = analyze_news(item["title"], item["link"])

    print("إرسال إلى تيليجرام...")

    response = requests.post(
        API,
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

    print(response.text)

    mark_posted(item["link"])
    break
