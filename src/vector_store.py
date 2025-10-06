import faiss
import numpy as np

class VectorSearch:
    def __init__(self, index_path="data/embeddings/vector_index.faiss"):
        self.index = faiss.read_index(index_path)

    def search(self, query_vec, top_k=3):
        distances, indices = self.index.search(np.array([query_vec]).astype("float32"), top_k)
        return indices, distances
