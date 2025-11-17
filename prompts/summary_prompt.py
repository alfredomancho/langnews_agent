from langchain.prompts import PromptTemplate

SUMMARY_PROMPT = PromptTemplate(
    input_variables=["headlines"],
    template=(
        "Summarize the following news headlines into three concise bullet points:\n"
        "{headlines}"
    )
)

