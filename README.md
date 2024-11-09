Document RAG System
This project is a Retrieval-Augmented Generation (RAG) system for document processing and chatbot interaction. 
It processes documents, stores them for efficient retrieval using embeddings, and allows users to interact with 
a chatbot that retrieves and responds with relevant information from the documents.

Table of Contents
Project Structure
Features
Prerequisites
Installation
Usage
API Endpoints
Testing the Application
Project Structure


document_rag_system/
├── document_processing/
│   ├── __init__.py
│   ├── embeddings.py          # Creates and stores embeddings
│   ├── storage.py             # Stores embeddings in FAISS
│   ├── routes.py              # API routes for document processing
│
├── rag_chatbot/
│   ├── __init__.py
│   ├── chat_service.py        # Manages chat sessions and response streaming
│   ├── routes.py              # API routes for chatbot interactions
│   ├── history.py             # Stores and retrieves chat history
│
├── main.py                    # Main entry point for the FastAPI app
├── requirements.txt           # Project dependencies
└── utils/
    ├── async_utils.py         # Helper functions for asynchronous tasks
    └── logger.py              # Custom logger setup

    
Features
Document Processing: Process and store document embeddings for quick retrieval.
Chatbot Interaction: Chatbot that provides information based on document content.
FAISS Integration: Utilizes FAISS for efficient embedding storage and retrieval.


Prerequisites
Python 3.8 or higher
FAISS for handling embeddings
FastAPI and Uvicorn for the server


Installation
Clone the repository:
git clone https://github.com/Manishsingh89716/backend_task
cd Task_Backend

Install Dependencies: Make sure you have FAISS installed, then install the dependencies listed in requirements.txt:
pip install -r requirements.txt
Setting Up FAISS (Optional, if not installed via pip): If you encounter issues with hnswlib, consider using faiss as an alternative, which is configured in this code.

Usage
Start the FastAPI Application:
uvicorn main:app --reload
By default, the app will run on http://localhost:8000.

Access the API Documentation: Open your browser and navigate to:
http://localhost:8000/docs
This will open the Swagger UI where you can test the endpoints.

API Endpoints
1. Document Processing
Endpoint: POST /api/documents/process
Description: Processes a document and stores its embedding.
Parameters:
file_path (query): Path to the document file (e.g., Task_Backend/sql.pdf).

2. Start Chat
Endpoint: POST /api/chat/start
Description: Starts a chat session for querying a document.
Parameters:
asset_id (string): The ID of the processed document asset.

3. Send Message
Endpoint: POST /api/chat/message
Description: Sends a message to the chatbot for response.
Parameters:
chat_thread_id (string): The ID of the active chat session.
user_message (string): The user's message.

4. Retrieve Chat History
Endpoint: GET /api/chat/history
Description: Retrieves the history of messages in a chat session.
Parameters:
chat_thread_id (string): The ID of the chat session.

Testing the Application
Process a Document:

Navigate to the /api/documents/process endpoint in Swagger UI.
Enter the file_path of your document (e.g., Task_Backend/sql.pdf) and click Execute.
You should receive an asset_id for the document, which can be used for chatbot interaction.
Start a Chat Session:

Use the /api/chat/start endpoint.
Provide the asset_id obtained from the document processing step and click Execute.
You will receive a chat_thread_id for the session.
Send a Message:

Use the /api/chat/message endpoint.
Enter the chat_thread_id and a user_message (e.g., "What is SQL?"), then click Execute.
The response will contain an answer based on the document content.
Retrieve Chat History:

Use the /api/chat/history endpoint.
Provide the chat_thread_id to view the chat history for that session.
Example Usage
To process a file located at Task_Backend/sql.pdf:

curl -X 'POST' \
  'http://localhost:8000/api/documents/process?file_path=Task_Backend/sql.pdf' \
  -H 'accept: application/json'
Expected response:

{
  "asset_id": "asset_sql"
}
Starting a chat session:

curl -X 'POST' \
  'http://localhost:8000/api/chat/start' \
  -H 'accept: application/json' \
  -d '{"asset_id": "asset_sql"}'
Expected response:

{
  "chat_thread_id": "thread_123"
}
Sending a message:

curl -X 'POST' \
  'http://localhost:8000/api/chat/message' \
  -H 'accept: application/json' \
  -d '{"chat_thread_id": "thread_123", "user_message": "What is SQL?"}'
Expected response:

{
  "response": "SQL stands for Structured Query Language, used for managing and querying data in relational databases."
}

Troubleshooting
FAISS Installation Issues: If FAISS is not working, try installing via pip install faiss-cpu.
File Path Errors: Ensure the file path provided in file_path is correct and accessible from the project root.

License
This project is licensed under the MIT License.
