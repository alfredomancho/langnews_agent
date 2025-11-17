import langchain
from agents.summarize_agent import run_agent

print(f"LangChain version is: {langchain.__version__}")

if __name__ == "__main__":
    summary = run_agent()
    print("Today's News Summary:\n", summary)
