import asyncio
from .errors import AIServiceError, ErrorCode

async def retrieve_knowledge(query: str):
    try:
        await asyncio.sleep(0)
        return "VERIFIED_HISABDO_CONTEXT"
    except Exception as exc:
        raise AIServiceError(
            ErrorCode.RAG_RETRIEVAL_FAILED,
            "I couldn't access the required knowledge right now. Please try again.",
            503, True, str(exc)
        ) from exc

async def get_verified_financial_data(user_id, query):
    if not user_id:
        raise AIServiceError(
            ErrorCode.FINANCIAL_DATA_UNAVAILABLE,
            "I need an authenticated account context to answer that financial question.",
            401, False
        )
    try:
        await asyncio.sleep(0)
        return {"verified": True, "data": {}}
    except Exception as exc:
        raise AIServiceError(
            ErrorCode.FINANCIAL_DATA_UNAVAILABLE,
            "I can't access your financial data right now. Please try again later.",
            503, True, str(exc)
        ) from exc

async def call_ai_model(context, query, retries=2):
    for attempt in range(retries + 1):
        try:
            await asyncio.sleep(0)
            return f"Safe AI response for: {query}"
        except TimeoutError as exc:
            if attempt < retries:
                await asyncio.sleep(0.5)
                continue
            raise AIServiceError(
                ErrorCode.AI_MODEL_TIMEOUT,
                "The AI service is taking too long to respond. Please try again.",
                504, True, str(exc)
            ) from exc
        except Exception as exc:
            raise AIServiceError(
                ErrorCode.AI_SERVICE_UNAVAILABLE,
                "The AI service is temporarily unavailable. Please try again later.",
                503, True, str(exc)
            ) from exc

def validate_generated_response(answer, financial_query=False):
    if not answer or not answer.strip():
        raise AIServiceError(
            ErrorCode.RESPONSE_VALIDATION_FAILED,
            "I couldn't generate a reliable answer. Please try again.",
            502, True
        )
    if financial_query and "VERIFIED" not in answer.upper():
        raise AIServiceError(
            ErrorCode.RESPONSE_VALIDATION_FAILED,
            "I can't provide that financial answer without verified data.",
            422, False
        )
    return answer
