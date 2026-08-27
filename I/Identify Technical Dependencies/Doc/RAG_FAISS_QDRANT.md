# RAG / FAISS / Qdrant Implementation Plan

## Initial
Sentence Transformers → FAISS → Ollama.

## Indexing
1. Load knowledge documents.
2. Clean text.
3. Split into chunks.
4. Generate embeddings.
5. Add embeddings to FAISS.
6. Save index and metadata mapping.

## Query
1. Receive user query.
2. Generate query embedding using the same model.
3. Retrieve top-K vectors.
4. Apply similarity threshold.
5. Build grounded prompt.
6. Send context + query to Ollama.
7. Return answer and optional sources.

## Qdrant migration
Keep a vector-store interface so FAISS can be replaced by Qdrant without changing frontend contracts. Re-index the knowledge base and validate retrieval quality before switching production configuration.
