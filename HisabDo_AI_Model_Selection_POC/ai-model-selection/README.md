# AI Model Selection – HisabDo AI Copilot

## Files

- `AI_Model_Selection_POC.docx` — Professional technical and research document.
- `model_selection_config.json` — Separate implementation/configuration file.

## Purpose

These files define the evaluation and selection approach for the HisabDo AI Copilot initial POC.

The recommended approach is provider-agnostic:
React → Express → FastAPI → AI Orchestrator → RAG / Verified Financial APIs → Response.

A final LLM should be selected only after benchmarking candidate local and API-based approaches against HisabDo-specific English and Roman Urdu test cases.
