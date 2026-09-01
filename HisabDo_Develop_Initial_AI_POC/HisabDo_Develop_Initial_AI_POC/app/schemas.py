from pydantic import BaseModel, Field
from typing import Optional, Any

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000)
    language: Optional[str] = "auto"
    conversation_id: Optional[str] = None

class ChatResponse(BaseModel):
    success: bool
    type: str
    message: str
    source: Optional[dict[str, Any]] = None
