from langgraph.prebuilt import create_react_agent  # v1.0.3 modern react agent
from langchain_ollama import ChatOllama
from tools.search_news import search_news
from tools.summarize_headlines import summarize_headlines
from tools.extend_headlines import extend_headlines


def make_agent():
    llm = ChatOllama(model="mistral:7b", temperature=0.0) # use low temp for reliable reasoning

    tools = [search_news, summarize_headlines, extend_headlines]

    # for a custom prompt: app = create_react_agent(llm, tools, state_modifier="custom system prompt")
#    app = create_react_agent(llm, tools, debug=True, checkpointer=None)
    app = create_react_agent(llm, tools)

    return app
