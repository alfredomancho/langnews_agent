from langchain_core.prompts import PromptTemplate

LONG_HEADLINE_PROMPT = PromptTemplate.from_template(
    """Take the list of news headlines and rewrite each headline so that it is at least 15 words long while preserving its original news content and meaning:

{headlines}

Return a list of rewritten headlines where each one is at least 15 words long."""
)
