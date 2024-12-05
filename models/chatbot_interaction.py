from sqlalchemy import Column, Integer, String, Text, DateTime
from .database import db
from datetime import datetime


class ChatbotInteraction(db.Model):
    """Model for storing chatbot interaction logs."""
    __tablename__ = 'chatbot_interactions'

    id = Column(Integer, primary_key=True)  # Primary key
    query = Column(Text, nullable=False)  # User query
    response = Column(Text, nullable=False)  # Chatbot response
    timestamp = Column(DateTime, default=datetime.utcnow)  # Time of interaction

    def __init__(self, query, response, timestamp=None):
        """
        Constructor to initialize a ChatbotInteraction instance.
        :param query: The user query or input.
        :param response: The chatbot's response.
        :param timestamp: (Optional) Timestamp of the interaction.
        """
        self.query = query
        self.response = response
        self.timestamp = timestamp or datetime.utcnow()

    def __repr__(self):
        """String representation of the ChatbotInteraction instance."""
        return f"<ChatbotInteraction {self.id}: Query='{self.query}', Response='{self.response}', Timestamp={self.timestamp}>"

    def as_dict(self):
        """
        Serialize the chatbot interaction object into a dictionary.
        Useful for APIs or JSON responses.
        """
        return {
            "id": self.id,
            "query": self.query,
            "response": self.response,
            "timestamp": self.timestamp.isoformat(),
        }
