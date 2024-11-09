import faiss
import numpy as np
import os
import pickle

class FAISSStorage:
    def __init__(self, embedding_dim=384, index_file='faiss_index'):
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(self.embedding_dim)
        self.id_map = {}
        self.index_file = index_file

        if os.path.exists(f'{self.index_file}.index'):
            self.load_index()

    def load_index(self):
        self.index = faiss.read_index(f'{self.index_file}.index')
        with open(f'{self.index_file}_id_map.pkl', 'rb') as f:
            self.id_map = pickle.load(f)

    def save_index(self):
        faiss.write_index(self.index, f'{self.index_file}.index')
        with open(f'{self.index_file}_id_map.pkl', 'wb') as f:
            pickle.dump(self.id_map, f)

    def add_document(self, asset_id: str, embedding: list):
        vector = np.array(embedding).reshape(1, -1).astype('float32')
        self.index.add(vector)
        self.id_map[self.index.ntotal - 1] = asset_id
        self.save_index()
        return asset_id

    def query(self, embedding: list, top_k=5):
        vector = np.array(embedding).reshape(1, -1).astype('float32')
        distances, indices = self.index.search(vector, top_k)
        results = [self.id_map[idx] for idx in indices[0] if idx in self.id_map]
        return results
