# document_processing routes

from fastapi import APIRouter, HTTPException
from .embeddings import EmbeddingService
from .storage import FAISSStorage

router = APIRouter()
embedding_service = EmbeddingService()
storage_service = FAISSStorage()

@router.post("/api/documents/process")
async def process_document(file_path: str):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except Exception as e:
        raise HTTPException(status_code=400, detail="Could not read file.")

    embedding = embedding_service.create_embedding(content)
    asset_id = storage_service.add_document(asset_id=file_path, embedding=embedding)

    return {"asset_id": asset_id}
