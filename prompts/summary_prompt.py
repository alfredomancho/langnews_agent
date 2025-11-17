from langchain_core.prompts import PromptTemplate

#SUMMARY_PROMPT = PromptTemplate.from_template(
SUMMARY_PROMPT = (
    "Summarize the following news headlines into three concise bullet points.\n"
    "{headlines}"
)
