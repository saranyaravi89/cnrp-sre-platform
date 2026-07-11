from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_orders():
    response = client.get("/orders")
    assert response.status_code == 200
    assert "orders" in response.json()


def test_create_order():
    response = client.post("/orders")
    assert response.status_code == 200
    assert response.json()["status"] in ["created", "failed"]


def test_cancel_order():
    response = client.post("/orders/cancel")
    assert response.status_code == 200
    assert response.json()["status"] == "cancelled"


def test_get_trades():
    response = client.get("/trades")
    assert response.status_code == 200
    assert "trades" in response.json()


def test_execute_trade():
    response = client.post("/trades/execute")
    assert response.status_code == 200
    assert response.json()["status"] == "executed"


def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert b"app_requests_total" in response.content
