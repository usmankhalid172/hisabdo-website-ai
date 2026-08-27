# RAG Pipeline

## Document ingestion
Documents → cleaning → chunking → embeddings → FAISS index + metadata.

## Runtime query
User query → embedding → FAISS top-K retrieval → similarity filtering → grounded prompt → Ollama → response.

## Important rule
The embedding model used for indexing must match the model used for querying. If it changes, rebuild the vector index.
