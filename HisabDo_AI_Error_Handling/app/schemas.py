from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    language: str | None = None
    user_id: str | None = None

class ChatResponse(BaseModel):
    success: bool = True
    answer: str
    request_id: str
    source: str
