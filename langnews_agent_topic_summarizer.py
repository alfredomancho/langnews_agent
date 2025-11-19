from agents.agent_executor import make_agent
import langchain

print(f"LangChain version is: {langchain.__version__}")

if __name__ == "__main__":
    agent_app = make_agent()  # returns langgraph app

    query = (
        "Find at least 22 different news headlines about the iPhone, "
        "then summarize each headline into one numbered bullet point and state the source."
        "Use the search and summarize tools as needed."
    )

    result = agent_app.invoke({
        "messages": [("human", query)]  # start the react loop
    })

    # Extract final answer (LLM's conclusion)
    final_message = result["messages"][-1]
    print("Result:\n", final_message.content)
