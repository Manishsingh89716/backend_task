# rag_chatbot service

from fastapi import HTTPException
from document_processing.embeddings import EmbeddingService
from document_processing.storage import FAISSStorage

class ChatService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.storage_service = FAISSStorage()
        self.chat_threads = {}

    def start_chat(self, asset_id: str):
        chat_id = f"chat_{len(self.chat_threads) + 1}"
        self.chat_threads[chat_id] = {"asset_id": asset_id, "history": []}
        return chat_id

    def process_message(self, chat_id: str, user_message: str):
        if chat_id not in self.chat_threads:
            raise HTTPException(status_code=404, detail="Chat thread not found")

        embedding = self.embedding_service.create_embedding(user_message)
        asset_ids = self.storage_service.query(embedding)

        response = f"Related documents found: {', '.join(asset_ids)}"
        self.chat_threads[chat_id]["history"].append({"user": user_message, "response": response})
        return response
