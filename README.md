# SparkGPT — Distributed RAG Engine on Databricks

**SparkGPT** is an AI-powered, cloud-scale **Retrieval-Augmented Generation (RAG)** framework that blends the best of **Apache Spark™, LangChain, and FAISS** to turn large document collections into an intelligent, searchable knowledge base.

Built for **massive parallelism and low-latency reasoning**, SparkGPT ingests, embeds, and answers complex enterprise queries using **LLMs (GPT-4 / Claude)** ; all orchestrated over Databricks.

## What It Does
> Distributed Ingestion: Spark processes millions of documents into chunked Delta tables.

> Intelligent Embeddings: SentenceTransformers convert text into high-dimensional vectors for semantic understanding.

> Efficient Retrieval: FAISS ANN index ensures lightning-fast lookups across massive datasets.

> RAG + LangChain: Combines retrieval with LLM reasoning for grounded, factual responses.

> Scalable Serving: FastAPI or Streamlit endpoints deliver conversational AI at production scale.

> Evaluation Suite: Built-in latency, F1, and retrieval precision metrics for continuous improvement.

## Tech Stack
Databricks · Apache Spark™ · LangChain · DSPy · FAISS · SentenceTransformers · OpenAI · FastAPI · Delta Lake

## Quickstart

pip install -r requirements.txt

python src/spark_ingest.py

python src/embedding_generator.py
python src/vector_store.py build

uvicorn src.deploy_api:app --reload


### 💬 Example Query

Input:
“Summarize the refund policy in the 2024 contract.”

Response:

{
  "answer": "Customers can cancel within 30 days for a prorated refund...",
  "sources": ["contract_2024.pdf#p3", "refund_policy.md#L12"],
  "latency_ms": 421
}

# 🌟 Why SparkGPT?
Because RAG shouldn’t be slow or fragile. SparkGPT fuses **distributed data processing, semantic retrieval, and LLM reasoning** into one cohesive system — making enterprise-scale AI knowledge retrieval fast, explainable, and production-ready.

**Author**

Velankani Joise Divya G C
@2025
