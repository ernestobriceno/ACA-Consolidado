from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_moderate_accept():
    response = client.post('/moderate', json={'content': 'hello world'})
    assert response.status_code == 200
    data = response.json()
    assert 'results' in data or 'accepted' in data
