# HisabDo AI Copilot – Initial AI POC

**Project:** HisabDo Website Enhancement  
**Department:** AI/ML  
**Module:** Develop Initial AI POC  
**Prepared By:** Muhammad Taha  
**Status:** Prototype / Proof of Concept

## 1. Purpose
This document defines the initial Proof of Concept (POC) for the HisabDo AI Copilot. The POC is intentionally lightweight and low-risk. Its purpose is to validate the basic AI request workflow before full production integration.

The POC demonstrates:
- Basic user query handling
- Input validation and normalization
- Lightweight intent classification
- Controlled FAQ/knowledge retrieval
- A selected AI model integration point
- Controlled and verified context handling
- Basic error handling
- Prompt validation
- Response validation
- Safe fallback behavior

## 2. POC Scope
The initial POC focuses on understanding and routing user requests rather than implementing every future AI capability.

### In Scope
1. Receive a user message through an API.
2. Validate the request.
3. Normalize simple input formatting.
4. Classify the request into a supported intent.
5. Search a small verified knowledge base for FAQ/help questions.
6. Prepare controlled context for response generation.
7. Connect to an AI model through an abstraction layer.
8. Validate the generated response.
9. Return a safe fallback when a request cannot be supported.
10. Log errors without exposing internal implementation details.

### Out of Scope
- Direct production database access by the LLM
- Autonomous financial transactions
- Full production authentication
- Advanced predictive analytics
- Complete RAG/vector infrastructure
- Permanent conversation memory
- Full offline local model deployment

## 3. Proposed POC Workflow
User Query
    ↓
Request Validation
    ↓
Input Normalization
    ↓
Intent Classification
    ↓
AI Orchestrator
    ├── FAQ / Product Support → Verified Knowledge Lookup
    ├── General Conversation → Controlled AI Response
    ├── Financial Query → Verified Data Service Placeholder
    └── Unknown / Unsupported → Safe Fallback
    ↓
Prompt Construction
    ↓
Prompt Validation
    ↓
AI Model Adapter
    ↓
Response Validation
    ↓
Fallback if Validation Fails
    ↓
User Response

## 4. Basic Query Handling
The POC accepts a structured request containing a user message and optional language/session metadata. Empty, malformed, or excessively long messages are rejected before AI processing.

## 5. Selected AI Model Integration
The POC uses a model adapter so the underlying model can be replaced without changing the orchestration workflow. The sample implementation contains a mock provider by default and an interface where an Ollama or API-based provider can be connected later.

This separation supports experimentation with:
- Local models
- API-based models
- Multilingual models
- Future production model selection

## 6. FAQ and Knowledge Support
The POC includes a small verified knowledge collection. Knowledge answers are generated only from controlled content returned by the knowledge lookup layer.

If relevant information is unavailable, the system does not invent product functionality. It returns a fallback response.

## 7. Controlled and Verified Data
Financial information must not be fabricated. The sample financial route is intentionally represented as a controlled placeholder. In future integration, it should call an authenticated, user-scoped backend service that returns verified results.

The LLM must not receive unrestricted database access.

## 8. Basic Error Handling
The POC defines handling for:
- Invalid request body
- Empty message
- Unsupported or unknown intent
- Missing knowledge
- AI provider failure
- AI timeout
- Invalid model response
- Internal processing failure

Internal exception details are logged server-side but are not returned to users.

## 9. Prompt Validation
Before sending a prompt to the AI model, the POC verifies that:
- The user input is present.
- The prompt contains the required system behavior.
- Only controlled context is attached.
- The prompt does not request unsupported financial facts.
- The context size remains within the configured prototype limit.

The system prompt instructs the model to avoid fabricated information and to clearly state when verified information is unavailable.

## 10. Response Validation
Generated output is checked before returning it to the user.

Validation checks include:
- Non-empty response
- Reasonable response length
- No obvious internal error leakage
- No unsupported financial value pattern when verified data is absent
- Safe fallback when validation fails

The POC uses lightweight rule-based validation. A future implementation can add structured output schemas and stronger safety policies.

## 11. Error and Fallback Strategy
Fallback responses are part of the expected workflow, not an exceptional failure.

Examples:
- Unknown product information → “I could not find verified information for that request.”
- Financial data unavailable → “I cannot provide that balance without verified account data.”
- AI service unavailable → “The AI assistant is temporarily unavailable. Please try again.”
- Invalid input → “Please enter a valid question.”

## 12. Recommended Repository Structure
```
hisabdo-ai-poc/
├── README.md
├── requirements.txt
├── app/
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   ├── orchestrator.py
│   ├── intents.py
│   ├── knowledge.py
│   ├── prompts.py
│   ├── validation.py
│   ├── errors.py
│   └── model_provider.py
└── tests/
    └── test_workflow.py
```

## 13. Testing Requirements
The POC should be tested with:
- General HisabDo questions
- FAQ questions
- Feature guidance
- English queries
- Roman Urdu queries
- Empty or invalid input
- Unknown questions
- Simulated AI provider failure
- Simulated invalid model output
- Financial requests without verified data

## 14. Acceptance Criteria
The initial POC is considered successful when:
1. Valid requests pass through the complete workflow.
2. Basic intents route correctly.
3. FAQ answers use verified prototype knowledge.
4. Unknown information triggers a safe fallback.
5. Invalid input is rejected safely.
6. Model failures do not expose internal errors.
7. Prompt validation occurs before model invocation.
8. Response validation occurs before user delivery.
9. The architecture remains modular for future RAG and financial API integration.

## 15. Future Extension
The POC can evolve into the full HisabDo AI Copilot through:
- Embeddings and vector search
- FAISS/Qdrant integration
- Advanced multilingual processing
- Authenticated user context
- Verified financial APIs
- Conversation context
- Recommendations and insights
- Voice interaction
- Offline/local AI optimization

## Conclusion
This initial POC provides a controlled foundation for HisabDo AI development. It validates the complete basic request lifecycle while keeping the prototype lightweight, modular, and low-risk. The design follows the core principle:

**AI understands and explains. Verified systems provide facts and calculations.**
