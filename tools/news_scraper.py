import requests
from config.settings import NEWSDATA_API_KEY, NEWSDATA_API_URL

def fetch_top_headlines(limit: int=50, country: str="ca,us", language: str="en", category: str="top,technology"):
    
    # build query url
    url = NEWSDATA_API_URL + "?" + "apikey=" + NEWSDATA_API_KEY + "&country=" + country + "&language=" + language + "&category=" + category

    print(f"Query URL is: {url}")
    print("Called fetch_top_headlines()")
    print(f"fetch_top_headlines limit is: {limit}")
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    articles = data.get("results", [])[:limit]
    return [article.get("title") for article in articles if article.get("title")]




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
