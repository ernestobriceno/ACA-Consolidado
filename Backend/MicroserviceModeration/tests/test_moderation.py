from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_moderate_accept():
    response = client.post('/moderate', json={'content': 'hello world'})
    assert response.status_code == 200
    data = response.json()
    assert data['accepted'] is True
    assert 'scores' in data

def test_moderate_reject():
    response = client.post('/moderate', json={'content': 'you are stupid and idiotic'})
    assert response.status_code == 200
    data = response.json()
    assert data['accepted'] is False
    assert data['reason'] == 'toxic content'
    assert 'scores' in data
