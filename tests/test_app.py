import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "name" in data[0]

def test_interact_chatbot(client):
    # Test chatbot interaction
    response = client.post('/chatbot', json={"message": "Hello"})
    assert response.status_code == 200
    data = response.get_json()
    assert "response" in data
    assert data["response"] == "Hello! How can I assist you today?"

    response = client.post('/chatbot', json={"message": "I need help"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["response"] == "I can assist with booking teleconsultations or finding health information."

    response = client.post('/chatbot', json={"message": "Random message"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["response"] == "I'm sorry, I didn't understand that. Could you rephrase?"

def test_book_teleconsultation(client):
    # Test valid teleconsultation booking
    response = client.post('/teleconsultation', json={"user_id": 1, "time_slot": "2024-12-05T10:00"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Teleconsultation booked successfully"
    assert data["teleconsultation"]["user_id"] == 1
    assert data["teleconsultation"]["time_slot"] == "2024-12-05T10:00"

    # Test invalid teleconsultation booking (missing fields)
    response = client.post('/teleconsultation', json={"user_id": 1})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Missing user_id or time_slot"
