from langchain_core.prompts import PromptTemplate

SUMMARY_PROMPT = PromptTemplate.from_template(
        """You are an expert news summarizer.
Here are news headlines about different topics:
{headlines}

Create exactly one concise, neutral paragraph that captures information from the news headlines.
Do not add any commentary outside the paragraph."""
)
