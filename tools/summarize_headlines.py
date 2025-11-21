from langchain.tools import tool
from langchain_core.output_parsers import StrOutputParser
from prompts.summary_prompt import SUMMARY_PROMPT
from agents.llm.ollama_llm_agent import OllamaAgentRunnable

@tool
def summarize_headlines(headlines: list) -> str:
    """Takes a list of news headlines and summarizes each of them into concise bullet points. Always use this tool to summarize headlines and never do it in-model.

    Args:
        headlines: List of strings (news headlines)

    Returns:
        A list with bullet points that summarizes each news headline.
    """
    llm = OllamaAgentRunnable()
    chain = SUMMARY_PROMPT | llm | StrOutputParser()
    print("Called tool summarize_headlines")
    return chain.invoke({"headlines": headlines})  
