from enum import Enum

class ErrorCode(str, Enum):
    INVALID_INPUT = "INVALID_INPUT"
    UNKNOWN_INTENT = "UNKNOWN_INTENT"
    KNOWLEDGE_UNAVAILABLE = "KNOWLEDGE_UNAVAILABLE"
    RAG_RETRIEVAL_FAILED = "RAG_RETRIEVAL_FAILED"
    FINANCIAL_DATA_UNAVAILABLE = "FINANCIAL_DATA_UNAVAILABLE"
    AI_MODEL_TIMEOUT = "AI_MODEL_TIMEOUT"
    AI_SERVICE_UNAVAILABLE = "AI_SERVICE_UNAVAILABLE"
    RESPONSE_VALIDATION_FAILED = "RESPONSE_VALIDATION_FAILED"
    INTERNAL_ERROR = "INTERNAL_ERROR"

class AIServiceError(Exception):
    def __init__(self, code, user_message, status_code=500, retryable=False, details=None):
        super().__init__(details or user_message)
        self.code = code
        self.user_message = user_message
        self.status_code = status_code
        self.retryable = retryable
        self.details = details
