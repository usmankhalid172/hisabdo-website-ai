# AI Error Handling Matrix

| Scenario | Code | User Fallback | Retry |
|---|---|---|---|
| Invalid input | INVALID_INPUT | Ask for a valid question | No |
| Unknown intent | UNKNOWN_INTENT | Explain supported topics | No |
| Knowledge unavailable | KNOWLEDGE_UNAVAILABLE | Try again later | Optional |
| RAG failure | RAG_RETRIEVAL_FAILED | Temporary knowledge message | Yes |
| Financial API failure | FINANCIAL_DATA_UNAVAILABLE | Never guess; retry later | Yes if transient |
| Model timeout | AI_MODEL_TIMEOUT | Ask user to retry | Yes |
| AI unavailable | AI_SERVICE_UNAVAILABLE | Temporary-service message | Yes |
| Unsafe/empty response | RESPONSE_VALIDATION_FAILED | Do not return answer | Controlled |
| Unexpected error | INTERNAL_ERROR | Generic message | Controlled |

## Rules

- Financial answers must use verified backend data.
- The LLM must not access the database directly.
- Never expose stack traces, API keys, tokens, database errors, or provider internals.
- Logs should include request ID, error code, timestamp, and sanitized technical details.
- Logs must not contain passwords, tokens, API keys, or unnecessary financial/PII data.
- Retry transient network/service/timeout failures only.
