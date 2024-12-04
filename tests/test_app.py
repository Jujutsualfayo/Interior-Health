import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_users(client):
    # Test the GET /users endpoint
    response = client.get('/users')
    assert response.status_code == 200
    data = response.get_json()
    
    # Ensure we get at least one user
    assert isinstance(data, list)
    assert len(data) > 0
    assert "name" in data[0]
    assert "email" in data[0]

def test_get_user(client):
    # Test retrieving an existing user
    response = client.get('/users/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1
    assert data["name"] == "Alice"

def test_get_nonexistent_user(client):
    # Test retrieving a non-existent user
    response = client.get('/users/999')  # User ID 999 doesn't exist
    assert response.status_code == 404
    data = response.get_json()
    
    # Ensure the error message is returned
    assert "error" in data
    assert data["error"] == "User not found"
