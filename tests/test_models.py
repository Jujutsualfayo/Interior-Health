import pytest
from app import db
from app.models import ChatbotInteraction

@pytest.fixture
def test_db():
    """Fixture to set up and tear down the test database."""
    # Create a temporary database for testing
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()

def test_chatbot_model(test_db):
    """Test the ChatbotInteraction model."""
    chatbot_interaction = ChatbotInteraction(query="How are you?", response="I'm good, thanks!")
    db.session.add(chatbot_interaction)
    db.session.commit()
    
    # Fix: Use db.session.query instead of ChatbotInteraction.query
    queried_interaction = db.session.query(ChatbotInteraction).filter(ChatbotInteraction.query == "How are you?").first()

    assert queried_interaction is not None
    assert queried_interaction.query == "How are you?"
    assert queried_interaction.response == "I'm good, thanks!"
