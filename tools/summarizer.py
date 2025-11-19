from langchain.tools import tool
from langchain_core.output_parsers import StrOutputParser
from prompts.summary_prompt import SUMMARY_PROMPT
from agents.llm.ollama_llm_agent import OllamaAgentRunnable

@tool
def summarize_headlines(headlines: list) -> str:
    """Take a list of news headlines and summarize each of them into concise bullet points.

    Args:
        headlines: List of strings (news headlines)

    Returns:
        A string with bullet points summarizing the key news.
    """
    llm = OllamaAgentRunnable()
    chain = SUMMARY_PROMPT | llm | StrOutputParser()
    print("Called tool summarize_headlines")
    return chain.invoke({"headlines": headlines})  
