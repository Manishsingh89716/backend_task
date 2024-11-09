from fastapi import FastAPI
from document_processing import routes as document_routes
from rag_chatbot import routes as chatbot_routes

app = FastAPI()

app.include_router(document_routes.router)
app.include_router(chatbot_routes.router)
