from .errors import AIServiceError, ErrorCode
from .services import retrieve_knowledge, get_verified_financial_data, call_ai_model, validate_generated_response

def classify_intent(message):
    text = message.lower()
    if any(w in text for w in ("balance", "expense", "receivable", "payment")):
        return "financial"
    if any(w in text for w in ("how", "what is", "feature", "help", "faq")):
        return "knowledge"
    return "unknown"

async def process_query(message, user_id=None):
    if not message.strip():
        raise AIServiceError(ErrorCode.INVALID_INPUT, "Please enter a question or message.", 400)

    intent = classify_intent(message)

    if intent == "unknown":
        raise AIServiceError(
            ErrorCode.UNKNOWN_INTENT,
            "I'm not sure what you're asking. Please ask about HisabDo features, help, or supported financial information.",
            422
        )

    if intent == "financial":
        data = await get_verified_financial_data(user_id, message)
        if not data.get("verified"):
            raise AIServiceError(
                ErrorCode.FINANCIAL_DATA_UNAVAILABLE,
                "I couldn't verify the financial information required for this answer.",
                503
            )
        answer = "VERIFIED financial response: requested information was obtained from the authorized backend."
        return validate_generated_response(answer, True), "verified-financial-api"

    context = await retrieve_knowledge(message)
    answer = await call_ai_model(context, message)
    return validate_generated_response(answer), "verified-knowledge"
