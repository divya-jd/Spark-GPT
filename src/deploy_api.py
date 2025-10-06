from fastapi import FastAPI, Query
from src.rag_pipeline import generate_answer
import uvicorn

app = FastAPI(title="SparkGPT – RAG API", version="1.0")

@app.get("/query")
def query_llm(q: str = Query(..., description="Enter your question")):
    response = generate_answer(q)
    return {"query": q, "response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
