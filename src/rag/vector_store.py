import faiss
import numpy as np
import pickle

class VectorStore:

    def __init__(self):
        self.index = None
        self.documents = None

    def build_index(self,embeddings,documents):

        embeddings = np.array(embeddings).astype("float32")
        dimension = embeddings.shape[1]
        self.index = faiss.IndexHNSWFlat(dimension,32)
        self.index.add(embeddings)
        self.documents = documents

    def save(self):
        faiss.write_index(self.index,"vector_db/faiss.index")

        with open("vector_db/documents.pkl","wb") as f:
            pickle.dump(self.documents,f)