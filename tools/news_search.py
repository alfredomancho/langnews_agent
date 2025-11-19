from langchain.tools import tool
from tools.news_scraper import fetch_top_headlines

@tool("search_news")
def search_news(query: str, limit: int=50, country: str="ca,us", language: str="en", category: str="technology"):
    """Search for recent news headlines containing the given query.
    
    Args:
        query: The keyword to search for (e.g., "iPhone")
        limit: Maximum number of headlines to fetch
        country: Comma-separated country codes (e.g., "us,ca")
        language: Language code (e.g., "en")
        category: News category (e.g., "technology")

    Returns:
        List of headline strings that contain the query.
    """
    headlines = fetch_top_headlines(limit=limit, country=country, language=language, category=category)
    print("Called tool search_news")
    print(f"limit is {limit}")
    print(f"query is {query}")
    filtered = [h for h in headlines if query.lower() in h.lower()]
    return filtered
