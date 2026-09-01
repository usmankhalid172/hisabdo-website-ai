from fastapi import FastAPI, HTTPException
from .schemas import ChatRequest, ChatResponse
from .orchestrator import handle_query
from .errors import ValidationError

app = FastAPI(title="HisabDo AI POC")

@app.post("/api/ai/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        result = handle_query(request.message)
        return ChatResponse(success=True, **result)
    except ValidationError as exc:
        raise HTTPException(status_code=400, detail="Please enter a valid question.") from exc
    except Exception:
        # Log detailed exception server-side in production.
        raise HTTPException(status_code=503, detail="AI service is temporarily unavailable.")
