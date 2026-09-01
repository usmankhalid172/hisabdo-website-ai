from .intents import classify_intent
from .knowledge import search_knowledge
from .prompts import build_prompt
from .validation import validate_prompt, validate_response
from .model_provider import provider
from .errors import ValidationError, AIServiceError

FALLBACK_UNKNOWN = "I could not find verified information for that request."
FALLBACK_FINANCIAL = "I cannot provide financial information without verified account data."
FALLBACK_SERVICE = "The AI assistant is temporarily unavailable. Please try again."

def handle_query(message: str):
    if not message or not message.strip():
        raise ValidationError("A valid question is required.")

    normalized = " ".join(message.strip().split())
    intent = classify_intent(normalized)

    if intent == "FINANCIAL_QUERY":
        return {"type": intent, "message": FALLBACK_FINANCIAL,
                "source": {"type": "verified_data_required"}}

    knowledge = search_knowledge(normalized) if intent == "FAQ_QUERY" else None
    if intent == "FAQ_QUERY" and not knowledge:
        return {"type": intent, "message": FALLBACK_UNKNOWN,
                "source": {"type": "no_verified_knowledge"}}

    context = knowledge["content"] if knowledge else None
    prompt = build_prompt(normalized, context)

    try:
        validate_prompt(prompt)
        generated = provider.generate(prompt)
        if not validate_response(generated):
            return {"type": "fallback", "message": FALLBACK_UNKNOWN,
                    "source": {"type": "response_validation"}}
        return {"type": intent, "message": generated,
                "source": {"type": "verified_knowledge" if knowledge else "controlled_ai"}}
    except (ValidationError, AIServiceError):
        return {"type": "fallback", "message": FALLBACK_SERVICE,
                "source": {"type": "safe_fallback"}}
