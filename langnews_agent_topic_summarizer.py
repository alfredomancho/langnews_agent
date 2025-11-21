from agents.agent_executor import make_agent
import langchain

print(f"LangChain version is: {langchain.__version__}")

if __name__ == "__main__":
    agent_app = make_agent()  # returns langgraph app

    query = (
        "Search for at least 8 unique news headlines about the iPhone 16, extend and summarize each headline. Use the search_news tool with appropriate arguments and other available tools as necessary to achieve the goal. "
        "Output each search result as a single numbered bullet point indicating the source and date of the headline. DO NOT output anything else."
    )

    result = agent_app.invoke({
        "messages": [("human", query)]  # start the react loop
    })

    # Extract final answer (LLM's conclusion)
    final_message = result["messages"][-1]
    print("Result:\n", final_message.content)
