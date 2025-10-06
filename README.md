<<<<<<< HEAD
# Spark-GPT
=======
# SparkGPT: Distributed RAG on Databricks

A production-ready **Retrieval-Augmented Generation (RAG)** system built with **Apache Spark™, LangChain, FAISS, and Databricks Runtime**.

## Features
- Distributed document ingestion via **Spark**
- Vector embeddings using **SentenceTransformers**
- Scalable **RAG pipeline** with LangChain & FAISS
- Deployment via **FastAPI / Streamlit**
- Evaluation & Monitoring with latency and F1 metrics

## Tech Stack
`Databricks` · `Apache Spark™` · `LangChain` · `DSPy` · `FAISS` · `Azure ML` · `Delta Lake` · `OpenAI`

## Usage
```bash
pip install -r requirements.txt
python src/spark_ingest.py
python src/embedding_generator.py
python src/deploy_api.py
>>>>>>> 09d9e78 (Initial commit - SparkGPT project)
