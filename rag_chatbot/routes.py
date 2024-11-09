# rag_chatbot routes

from fastapi import APIRouter, HTTPException
from .chat_service import ChatService

router = APIRouter()
chat_service = ChatService()

@router.post("/api/chat/start")
async def start_chat(asset_id: str):
    return {"chat_id": chat_service.start_chat(asset_id)}

@router.post("/api/chat/message")
async def chat_message(chat_id: str, message: str):
    response = chat_service.process_message(chat_id, message)
    return {"response": response}
