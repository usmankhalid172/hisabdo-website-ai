# HisabDo Architecture

```text
                 ┌─────────────────┐
                 │   React / Vite  │
                 └────────┬────────┘
                          │
                   HTTP/JSON API
                          │
                 ┌────────▼────────┐
                 │ Node / Express  │
                 │ integration     │
                 └────────┬────────┘
                          │
                 ┌────────▼────────┐
                 │ FastAPI AI API  │
                 └───┬────┬────┬───┘
                     │    │    │
          ┌──────────┘    │    └─────────────┐
          ▼               ▼                  ▼
      MongoDB           FAISS             Ollama
   application data   RAG retrieval       local LLM
                          ▲
                          │
                Sentence Transformers
                     embeddings

Future:
FastAPI → Qdrant instead of/local to FAISS when scale requires it.
```
