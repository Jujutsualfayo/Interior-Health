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

