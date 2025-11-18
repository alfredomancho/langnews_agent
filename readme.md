## News Summarizer Agent Using LangChain Framework 

## Overview

This project demonstrates how to build a modular Python agent with the LangChain framework.  The agent fetches live news headlines using a free, open news API (NewsData.io), then summarizes the headlines into concise bullet points using a LLM (mistral:7b).

The codebase demonstrates:
- Chaining of LLM prompts (LangChain)
- Basic web API data retrieval
- Separation of configuration, tools, and agent logic
- CLI for quick execution
- Automatic selection of tools and makes all critical decisions until specified goal is met

## Structure
- **config/settings.py:**: Centralized configuration (API endpoints and keys)
- **prompts/summary_prompt.py:**: Contains prompt templates for summarization
- **tools/news_scraper.py:**: Scripts for fetching news headlines from the NewsData.io API
- **agents/summarize_agent.py:**: LangChain agent logic for summarizing headlines
- **agents/llm/ollama_llm_agent.py:**: Use mistral:7b LLM model via Ollama
- **langnews_agent_main.py:**: Run the full agent (CLI entry point)

- **requirements.txt**: List of required packages and dependencies.

## Sample Data
This agent fetches live headlines from the NewsData.io API.

API documentation:
https://newsdata.io/docs

## How to Run
1. **Install dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

2. **Set environment variables**  
Get a NewsData.io API key (free registration).
    ```bash
    export NEWSDATA_API_KEY='your_api_key_here'
    ```

3. **Run Agent**  
    ```bash
    python langnews_agent_main.py
    ```
