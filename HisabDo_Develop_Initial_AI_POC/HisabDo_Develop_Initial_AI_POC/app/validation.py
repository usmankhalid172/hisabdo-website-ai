from .config import MAX_RESPONSE_LENGTH
from .errors import ValidationError

def validate_prompt(prompt: str):
    if not prompt or "You are the HisabDo AI Copilot" not in prompt:
        raise ValidationError("Invalid prompt structure")
    if len(prompt) > 6000:
        raise ValidationError("Prompt exceeds prototype limit")

def validate_response(response: str, has_verified_financial_data: bool = False) -> bool:
    if not response or not response.strip() or len(response) > MAX_RESPONSE_LENGTH:
        return False
    blocked = ["traceback", "internal server error", "system prompt"]
    if any(item in response.lower() for item in blocked):
        return False
    if not has_verified_financial_data and any(token in response.lower() for token in ["pkr ", "balance is", "outstanding is"]):
        return False
    return True
