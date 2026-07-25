import feedparser

RSS_FEEDS = [
    "https://www.forexlive.com/feed/",
    "https://www.investing.com/rss/news.rss",
    "https://finance.yahoo.com/rss/topstories",
]

def get_news():
    news = []

    for feed in RSS_FEEDS:
        data = feedparser.parse(feed)

        for item in data.entries:
            news.append({
                "title": item.title,
                "link": item.link
            })

    return news
