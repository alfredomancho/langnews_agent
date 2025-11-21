from langchain.tools import tool
from langchain_core.output_parsers import StrOutputParser
from prompts.long_headline_prompt import LONG_HEADLINE_PROMPT  # You will need to create this prompt file
from agents.llm.ollama_llm_agent import OllamaAgentRunnable

@tool
def extend_headlines(headlines: list) -> str:
    """Takes a list of news headlines and rewrites each headline so it is at least 15 words long. Always use this tool to extend the length of headlines and never do it in-model.

    Args:
        headlines: List of strings (news headlines)

    Returns:
        A list with headlines rewritten to be at least 15 words each.
    """
    llm = OllamaAgentRunnable()
    chain = LONG_HEADLINE_PROMPT | llm | StrOutputParser()
    print("Called tool extend_headlines")
    return chain.invoke({"headlines": headlines})

