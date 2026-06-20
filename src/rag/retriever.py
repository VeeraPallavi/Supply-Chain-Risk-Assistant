import faiss
import pickle
import numpy as np

from src.rag.embeddings import EmbeddingGenerator

class Retriever:
    def __init__(self):
        self.index = faiss.read_index("vector_db/faiss.index")
        with open("vector_db/documents.pkl","rb") as f:
            self.documents = pickle.load(f)

        self.embedder = None

    def retrieve(self, query, top_k=5):
        if self.embedder is None:
            self.embedder = EmbeddingGenerator()

        query_embedding = self.embedder.generate([query])
        query_embedding = np.array(query_embedding).astype("float32")
        distances, indices = self.index.search(query_embedding,top_k)
        results = []
        for idx in indices[0]:
            doc = self.documents[idx]
            if doc not in results:
                results.append(doc)
        return results