from .errors import AIServiceError

class ModelProvider:
    def generate(self, prompt: str) -> str:
        # Replace with an approved Ollama or API provider during integration.
        if not prompt:
            raise AIServiceError("Empty prompt")
        return "Based on the available verified information, I can help with this request."

provider = ModelProvider()
