from langchain_core.runnables import Runnable
import requests

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
