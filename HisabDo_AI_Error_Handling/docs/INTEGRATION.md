# Integration

Recommended architecture:

React Chat UI
  -> Express Backend
  -> FastAPI AI Service
  -> AI Orchestrator
  -> FAQ / RAG / Financial Module
  -> Verified Data / Knowledge
  -> Response

Express responsibilities:
1. Authenticate the user.
2. Authorize access.
3. Attach trusted user context.
4. Call FastAPI.
5. Return safe errors to React.
6. Preserve X-Request-ID.

FastAPI responsibilities:
1. Validate request.
2. Detect intent.
3. Route to the correct module.
4. Retrieve verified context.
5. Validate the generated response.
6. Return standardized success/error responses.

React should display error.message and use error.code for UI behavior.
