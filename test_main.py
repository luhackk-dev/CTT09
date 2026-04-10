from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API Online"}

def test_soma():
    response = client.get("/somar/10/20")
    assert response.status_code == 200
    assert response.json() == {"resultado": 30}
