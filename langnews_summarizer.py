import langchain
from agents.summarize_agent import run_agent
from config.settings import NEWS_TOPICS, NEWS_COUNTRY, NEWS_LANGUAGE

print(f"LangChain version is: {langchain.__version__}")

if __name__ == "__main__":
    summary = run_agent(topics=NEWS_TOPICS, country=NEWS_COUNTRY, language=NEWS_LANGUAGE)
    print("Today's News Summary:\n", summary)
