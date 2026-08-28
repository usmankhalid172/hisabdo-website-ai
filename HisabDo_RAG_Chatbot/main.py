from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_pipeline import RAGPipeline
import os

app = FastAPI(
    title="HisabDo RAG Chatbot",
    description="Retrieval Augmented Generation Chatbot",
    version="1.0.0"
)


class QueryRequest(BaseModel):
    query: str
    top_k: int = 3


class FAQRequest(BaseModel):
    question: str


# Initialize RAG Pipeline
knowledge_base_dir = os.path.join(
    os.path.dirname(__file__),
    "knowledge-base"
)

rag_pipeline = RAGPipeline(knowledge_base_dir)
index_built = False


@app.get("/")
def read_root():
    return {
        "message": "HisabDo RAG Chatbot API",
        "docs": "/docs",
        "index_ready": index_built
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/build-index")
def build_index():
    global index_built

    try:
        stats = rag_pipeline.build_index()
        index_built = True

        return {
            "status": "success",
            **stats
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/retrieve")
def retrieve(request: QueryRequest):

    if not index_built:
        raise HTTPException(
            status_code=400,
            detail="Index not built. Call /build-index first"
        )

    chunks = rag_pipeline.retrieve(
        request.query,
        top_k=request.top_k
    )

    return {
        "query": request.query,
        "chunks": chunks
    }


@app.post("/chat")
def chat(request: QueryRequest):

    if not index_built:
        raise HTTPException(
            status_code=400,
            detail="Index not built. Call /build-index first"
        )

    result = rag_pipeline.generate_answer(
        request.query,
        top_k=request.top_k
    )

    return result


@app.post("/api/faq")
def ask_faq(request: FAQRequest):

    question = request.question.strip()
    print("Received FAQ question:", question)

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question is required."
        )

    if not index_built:
        raise HTTPException(
            status_code=400,
            detail="Index not built. Call /build-index first"
        )

    try:
        result = rag_pipeline.generate_answer(
            question,
            top_k=3
        )

        return {
            "success": True,
            "question": question,
            "answer": result["answer"],
            "generated_by_llm": result["generated_by_llm"],
            "retrieved_chunks": result["retrieved_chunks"]
        }

    except Exception as e:

        print("FAQ API Error:", str(e))

        raise HTTPException(
            status_code=500,
            detail="Unable to process the question."
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )