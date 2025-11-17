import requests
from config.settings import NEWSDATA_API_KEY, NEWSDATA_API_URL

def fetch_top_headlines(limit=5, country="us", language="en"):
    params = {
        "apikey": NEWSDATA_API_KEY,
        "country": country,
        "language": language,
        "category": "top",
        "page": 0,
    }
    response = requests.get(NEWSDATA_API_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    articles = data.get("results", [])[:limit]
    return [article.get("title") for article in articles if article.get("title")]

if __name__ == "__main__":
    print(fetch_top_headlines())
