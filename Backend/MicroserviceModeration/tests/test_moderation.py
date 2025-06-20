from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_moderate_accept():
    response = client.post('/moderate', json={"content": "hello world"})
    assert response.status_code == 200
    data = response.json()
    assert data["accepted"] is True


def test_moderate_reject():
    response = client.post('/moderate', json={"content": "you are stupid"})
    assert response.status_code == 200
    data = response.json()
    assert data["accepted"] is False
    assert data["reason"]
