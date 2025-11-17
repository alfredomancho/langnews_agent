import requests

class OllamaAgent:
    def __init__(self, model="mistral:7b"):
        self.model = model

    def generate(self, prompt):
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": self.model, "prompt": prompt, "stream": False}
        )
        response.raise_for_status()
        return response.json()["response"]
