import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b"OK" in response.data

def test_post_data(client):
    res = client.post('/data', json={'foo': 'bar'})
    assert res.status_code == 201
    assert res.is_json
    assert res.get_json()['received']['foo'] == 'bar'