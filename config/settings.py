import os
from dotenv import load_dotenv

load_dotenv()

NEWSDATA_API_KEY = os.getenv("NEWS_API_KEY")
#NEWSDATA_API_URL = "https://newsdata.io/api/1/news"  
NEWSDATA_API_URL = "https://newsdata.io/api/1/latest"  
