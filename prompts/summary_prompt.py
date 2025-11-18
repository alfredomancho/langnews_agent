from langchain_core.prompts import PromptTemplate

SUMMARY_PROMPT = PromptTemplate.from_template(
    "Summarize the following news headlines into ONLY one concise bullet point for each category and state what the category is for each bullet point. Do not translate non-English headlines.\n"
    "{headlines}"
)
