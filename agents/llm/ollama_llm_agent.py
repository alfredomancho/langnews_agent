from langchain_core.runnables import Runnable # legacy
from langchain_core.language_models.base import BaseLanguageModel
from langchain_core.outputs import Generation, LLMResult
from langchain_core.messages import BaseMessage
import requests
from typing import Any, List, Optional

class OllamaAgentBaseModel(BaseLanguageModel):
    llm_type: str = "ollama"  

    def __init__(self, model="mistral:7b"):
        super().__init__()
        self.model = model

    def _generate(
        self, messages: List[BaseMessage], stop: Optional[List[str]] = None, **kwargs: Any
    ) -> LLMResult:

        prompt_parts = []
        for msg in messages:
            role = msg.__class__.__name__.lower()  
            if hasattr(msg, 'content'):
                content = msg.content
                if isinstance(content, dict) and "headlines" in content:
                    content = "\n".join(content["headlines"])
                prompt_parts.append(f"{role.capitalize()}: {content}")
            if hasattr(msg, 'tool_calls') and msg.tool_calls:
                for tc in msg.tool_calls:
                    prompt_parts.append(f"Tool Call: {tc['name']} with args {tc['args']}")
        prompt = "\n".join(prompt_parts) + "\nAssistant: "  

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "stop": stop or ["\nObservation:", "\nFinal Answer:"], 
                "options": kwargs.get("options", {})
            }
        )
        response.raise_for_status()
        text = response.json()["response"]

        return LLMResult(generations=[Generation(text=text)])

    # Legacy invoke (for summarizer tool)
    def invoke(self, input: Any, config: Optional[Any] = None, **kwargs: Any) -> str:
        if isinstance(input, dict) and "headlines" in input:
            prompt = "\n".join(input["headlines"])
        else:
            prompt = str(input)
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": self.model, "prompt": prompt, "stream": False}
        )
        response.raise_for_status()
        return response.json()["response"]

class OllamaAgentRunnable(Runnable):
    def __init__(self, model="mistral:7b"):
        self.model = model

    def invoke(self, prompt, config=None):
        if isinstance(prompt, dict) and "headlines" in prompt:
            prompt = "\n".join(prompt["headlines"])
        elif hasattr(prompt, "to_string"):
            prompt = prompt.to_string()
        elif hasattr(prompt, "value"):
            prompt = prompt.value
        else:
            prompt = str(prompt)

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": self.model, "prompt": prompt, "stream": False}
        )
        response.raise_for_status()
        return response.json()["response"]
