from fastapi.testclient import TestClient
from app.main import app

def test_saldo():
    with TestClient(app) as client:
        response = client.get("/api/v1/nnieto/alcancia/saldo")
        assert response.status_code == 200
        assert response.json() == 700
