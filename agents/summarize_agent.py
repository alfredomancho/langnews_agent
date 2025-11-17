from langchain_openai import ChatOpenAI
#from langchain_core.prompts import PromptTemplate   
from prompts.summary_prompt import SUMMARY_PROMPT
from langchain_core.output_parsers import StrOutputParser
from agents.llm.ollama_llm_agent import OllamaAgent
from tools.news_scraper import fetch_top_headlines

def run_agent():
    headlines = fetch_top_headlines()
    headlines_text = "\n".join(headlines)
    
#    llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.3)
    llm = OllamaAgent(model="mistral:7b")
    chain = SUMMARY_PROMPT | llm | StrOutputParser()

    summary = chain.invoke({"headlines_text": headlines_text})

    return summary

### old
#    prompt = SUMMARY_PROMPT
#    summarize_chain = LLMChain(
#        llm=llm,
#        prompt=SUMMARY_PROMPT
#    )
#    summary = summarize_chain.run(headlines=headlines_text)
#    return summary
###

if __name__ == "__main__":
    print(run_agent())
