from agents.agent_executor import make_agent
import langchain

print(f"LangChain version is: {langchain.__version__}")

if __name__ == "__main__":
    agent_app = make_agent()  # returns langgraph app

    query = (
        "Search for at least 8 unique news headlines about the iPhone 16. Extend each headline to at least 15 words. Use the search_news and extend_headlines tools as necessary. "
        "Output a list of numbered bullet points for each headline that includes the source and date of the headline. DO NOT output anything else."
    )

    result = agent_app.invoke({
        "messages": [("human", query)]  # start the react loop
    })

    # Extract final answer (LLM's conclusion)
    final_message = result["messages"][-1]
    print("Result:\n", final_message.content)
