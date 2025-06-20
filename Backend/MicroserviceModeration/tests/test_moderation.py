from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_moderate_accept():
    resp = client.post('/moderate', json={'content': 'hello friend'})
    assert resp.status_code == 200
    data = resp.json()
    assert data['accepted'] is True


def test_moderate_reject():
    resp = client.post('/moderate', json={'content': 'I will kill you'})
    assert resp.status_code == 200
    data = resp.json()
    assert data['accepted'] is False
    assert data['reason']
