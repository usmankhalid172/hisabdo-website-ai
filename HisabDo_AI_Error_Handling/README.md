# HisabDo AI Copilot — Error Handling

Production-oriented error handling for the FastAPI AI service.

Covers invalid input, unknown intents, missing knowledge, RAG failures,
financial API failures, model timeouts, retries, logging, safe fallbacks,
standard error codes, and protection against unsupported financial answers.

Core flow:
User Request -> Validation -> Intent Detection -> AI Orchestrator
-> FAQ/RAG/Financial Module -> Verified Context -> Response Validation
-> User Response or Safe Fallback.

Security:
- Never expose stack traces, provider errors, API keys, database errors, or internal details.
- Never guess financial values when verified data is unavailable.
- Retry only transient failures.
- Use request IDs for server-side tracing.
