import requests
from config.settings import NEWSDATA_API_KEY, NEWSDATA_API_URL

def fetch_top_headlines(limit=5, country="ca,us", language="en", category="top,technology"):
    
    url = NEWSDATA_API_URL + "?" + "apikey=" + NEWSDATA_API_KEY + "&country=" + country + "&language=" + language + "&category=" + category
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    articles = data.get("results", [])[:limit]
    return [article.get("title") for article in articles if article.get("title")]

if __name__ == "__main__":
    print(fetch_top_headlines())


### from news.io
#url = "https://newsdata.io/api/1/latest?
#  apikey=pub_8e4678a9d3ea477f8ec8c178030cd20c
#  &country=ca,us
#  &language=en
#  &category=top,technology"
#response = requests.get(url)
#data = response.json()
#print(data)
###
