from fastapi.testclient import TestClient
import sys
import os

# Adiciona o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app

client = TestClient(app)

def test_soma():
    response = client.post("/soma", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"resultado": 15}

def test_subtracao():
    response = client.post("/subtracao", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"resultado": 5}

def test_multiplicacao():
    response = client.post("/multiplicacao", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"resultado": 50}

def test_divisao():
    response = client.post("/divisao", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"resultado": 2.0}

def test_divisao_por_zero():
    response = client.post("/divisao", json={"a": 10, "b": 0})
    assert response.status_code == 400
    assert response.json()["detail"] == "Divisão por zero"

def test_exponenciacao():
    response = client.post("/exponenciacao", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"resultado": 8}