import logging
import uuid
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .errors import AIServiceError
from .orchestrator import process_query
from .schemas import ChatRequest, ChatResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hisabdo-ai")

app = FastAPI(title="HisabDo AI Service", version="1.0.0")

@app.middleware("http")
async def request_id_middleware(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    request.state.request_id = request_id
    try:
        response = await call_next(request)
    except Exception:
        logger.exception("Unhandled internal error | request_id=%s", request_id)
        return JSONResponse(
            status_code=500,
            content={"success": False, "error": {
                "code": "INTERNAL_ERROR",
                "message": "Something went wrong. Please try again later."
            }, "request_id": request_id}
        )
    response.headers["X-Request-ID"] = request_id
    return response

@app.exception_handler(AIServiceError)
async def ai_error_handler(request: Request, exc: AIServiceError):
    request_id = getattr(request.state, "request_id", str(uuid.uuid4()))
    logger.error(
        "AI error | request_id=%s | code=%s | retryable=%s | details=%s",
        request_id, exc.code, exc.retryable, exc.details
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "error": {
            "code": exc.code.value,
            "message": exc.user_message
        }, "request_id": request_id}
    )

@app.get("/health")
async def health():
    return {"status": "ok", "service": "hisabdo-ai"}

@app.post("/api/v1/ai/chat", response_model=ChatResponse)
async def chat(payload: ChatRequest, request: Request):
    answer, source = await process_query(payload.message, payload.user_id)
    return ChatResponse(
        answer=answer,
        request_id=request.state.request_id,
        source=source
    )
