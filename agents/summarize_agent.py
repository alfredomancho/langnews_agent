from prompts.summary_prompt import SUMMARY_PROMPT
from langchain_core.output_parsers import StrOutputParser
from agents.llm.ollama_llm_agent import OllamaAgentRunnable
from tools.fetch_top_headlines import fetch_top_headlines

def run_agent(topics: str="top", country: str="ca", language: str="en"):
    headlines = fetch_top_headlines(category=topics, country=country, language=language)
    
    llm = OllamaAgentRunnable()
    chain = SUMMARY_PROMPT | llm | StrOutputParser()

    summary = chain.invoke({"headlines": headlines})

    return summary
