from fastapi.testclient import TestClient
import pytest
from src.main import app  # Ajuste o caminho conforme a organização do seu projeto

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_extrair_entidades(client):
    endpoint = "/extrair-entidades/"  # O TestClient sabe que o host é localhost e a porta padrão é 8000
    json_data = {
        "texto": "João da Silva mora em São Paulo - SP, na Avenida das Araucárias, Centro.",
        "labels": ["PER", "LOC"]
    }
    response = client.post(endpoint, json=json_data)
    data = response.json()

    assert response.status_code == 200
    assert "PER" in data
    assert "LOC" in data
    assert "João da Silva" in data["PER"]
    assert "São Paulo" in data["LOC"]
