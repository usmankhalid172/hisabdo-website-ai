from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_pipeline import RAGPipeline
import os

app = FastAPI(
    title="HisabDo FAQ Assistant API",
    description="RAG-based FAQ Assistant for HisabDo",
    version="1.0.0"
)


# Request model
class FAQRequest(BaseModel):
    question: str
kb_dir = os.path.join(
    os.path.dirname(__file__),
    "knowledge-base"
)
pipeline = RAGPipeline(kb_dir)
print("Building RAG index...")
stats = pipeline.build_index()
print("Index built:", stats)


@app.get("/")
def home():
    return {
        "success": True,
        "message": "HisabDo FAQ Assistant API is running"
    }


@app.post("/api/faq")
def ask_faq(request: FAQRequest):

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question is required."
        )

    try:
        result = pipeline.generate_answer(
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