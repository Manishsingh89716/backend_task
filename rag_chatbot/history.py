# rag_chatbot history data

class ChatHistory:
    def __init__(self):
        self.history = {}

    def add_message(self, chat_id: str, user_message: str, response: str):
        if chat_id not in self.history:
            self.history[chat_id] = []
        self.history[chat_id].append({"user": user_message, "response": response})

    def get_history(self, chat_id: str):
        return self.history.get(chat_id, [])
