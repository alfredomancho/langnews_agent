from langchain_openai import OpenAI
from langchain_core.chains import LLMChain

from langchain.chains import LLMChain
from prompts.summary_prompt import SUMMARY_PROMPT
from tools.news_scraper import fetch_top_headlines

def run_agent():
    headlines = fetch_top_headlines()
    headlines_text = "\n".join(headlines)
    
    llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.3)
    summarize_chain = LLMChain(
        llm=llm,
        prompt=SUMMARY_PROMPT
    )
    summary = summarize_chain.run(headlines=headlines_text)
    return summary

if __name__ == "__main__":
    print(run_agent())
