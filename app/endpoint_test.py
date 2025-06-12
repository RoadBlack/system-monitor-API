from fastapi import FastAPI
from fastapi.testclient import TestClient
import datetime
from main import app

client = TestClient(app)

def test_read_health():

    response = client.get("/health")
    assert response.status_code == 200 
    assert response.json() == {"msg": "OK"}

def test_read_stats():
    response = client.get("/stats")
    assert response.status_code == 200
    assert type(response.json()['cpu']) == int
    assert type(response.json()['ram']) == float
    assert type(response.json()['disk']) == float

