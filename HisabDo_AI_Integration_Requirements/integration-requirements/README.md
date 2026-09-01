# HisabDo AI Integration Requirements

## Files

- `HisabDo_AI_Integration_Requirements.docx` — Professional technical integration document.
- `integration_api_config.json` — Separate API and architecture configuration/specification.
- `README.md` — Module overview.

## Core Flow

React Chat UI → Express Backend → FastAPI AI Service → AI Orchestrator →
Knowledge/RAG or Verified Financial API → Response Validation → User Response.

The LLM never receives unrestricted database access. Financial information is retrieved
through controlled, authenticated, and user-scoped application APIs.
