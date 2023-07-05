from coffee.main import app
import coffee.main
from fastapi.testclient import TestClient


client = TestClient(app)

def test_read_main():
    """test"""
    response = client.get("/")
    assert response.status_code == 200
