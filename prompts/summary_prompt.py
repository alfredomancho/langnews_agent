from langchain_core.prompts import PromptTemplate

SUMMARY_PROMPT = PromptTemplate.from_template(
        """You are an expert news summarizer.
Here are the headlines about the topic:
{headlines}

Create exactly 5 concise, neutral bullet points that capture information from different categories.  State the source for each bullet point.
Do not add any commentary outside the bullets."""
)
