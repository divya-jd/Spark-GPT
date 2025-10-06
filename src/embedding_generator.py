import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()
model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(texts, save_path="data/embeddings/vector_index.faiss"):
    vectors = model.encode(texts)
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(np.array(vectors).astype("float32"))
    faiss.write_index(index, save_path)
    print(f"✅ Saved {len(texts)} embeddings to {save_path}")
    return index

if __name__ == "__main__":
    sample_texts = ["Databricks integrates Spark and AI seamlessly.", 
                    "RAG pipelines improve enterprise retrieval accuracy."]
    create_embeddings(sample_texts)
