# SparkGPT — Distributed RAG on Databricks

A production-ready Retrieval-Augmented Generation (RAG) system that scales with **Apache Spark™ on Databricks**, uses SentenceTransformers for embeddings, FAISS/Delta for retrieval, and serves answers via FastAPI (optional Streamlit UI). Includes offline evals/telemetry for quality and latency.

## Features
- Distributed document ingestion via **Spark**
- Vector embeddings using **SentenceTransformers**
- Scalable **RAG pipeline** with LangChain & FAISS
- Deployment via **FastAPI / Streamlit**
- Evaluation & Monitoring with latency and F1 metrics

## Tech Stack
`Databricks` · `Apache Spark™` · `LangChain` · `DSPy` · `FAISS` · `Azure ML` · `Delta Lake` · `OpenAI`

## Usage


pip install -r requirements.txt

python src/spark_ingest.py

python src/embedding_generator.py
python src/vector_store.py build

uvicorn src.deploy_api:app --reload


## Prerequisites

Python ≥ 3.9

Databricks workspace + cluster (DBR 13 +)

OpenAI / Azure OpenAI API key

FAISS & SentenceTransformers installed (pip install -r requirements.txt)

Optional but recommended:

Unity Catalog for dataset organization

Databricks Jobs for scheduled ingestion & embedding updates

## 🧩 Installation

# Clone
git clone https://github.com/divya-jd/SparkGPT.git
cd SparkGPT

# Virtual env
python3 -m venv venv
source venv/bin/activate

# Dependencies
pip install -r requirements.txt

## Running the Pipeline
Step 1: Ingest Documents → Delta
python src/spark_ingest.py --config conf/config.yaml


