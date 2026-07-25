import json
import os

FILE_NAME = "posted_news.json"

def load_posted():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_posted(posted):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(posted, f, ensure_ascii=False, indent=2)

def is_posted(link):
    return link in load_posted()

def mark_posted(link):
    posted = load_posted()
    posted.append(link)
    save_posted(posted)
