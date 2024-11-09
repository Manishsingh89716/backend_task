# document_processing

from sentence_transformers import SentenceTransformer

class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def create_embedding(self, text: str):
        return self.model.encode(text).tolist()