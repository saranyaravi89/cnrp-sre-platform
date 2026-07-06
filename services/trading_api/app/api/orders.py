from fastapi import APIRouter
from random import choice, randint
from app.observability.metrics import ORDER_CREATED, ORDER_CANCELLED, ORDER_FAILED, ACTIVE_ORDERS

router = APIRouter()

active_orders = 0


@router.get("/orders")
def get_orders():
    return {
        "orders": [
            {"id": 1, "symbol": "AAPL", "side": "BUY", "status": "OPEN"},
            {"id": 2, "symbol": "MSFT", "side": "SELL", "status": "FILLED"}
        ]
    }


@router.post("/orders")
def create_order():
    global active_orders

    symbol = choice(["AAPL", "MSFT", "TSLA", "NVDA"])
    side = choice(["BUY", "SELL"])
    quantity = randint(1, 100)

    if randint(1, 10) == 1:
        ORDER_FAILED.inc()
        return {
            "status": "failed",
            "reason": "simulated order validation failure"
        }

    active_orders += 1
    ACTIVE_ORDERS.set(active_orders)
    ORDER_CREATED.inc()

    return {
        "status": "created",
        "symbol": symbol,
        "side": side,
        "quantity": quantity
    }


@router.post("/orders/cancel")
def cancel_order():
    global active_orders

    if active_orders > 0:
        active_orders -= 1

    ACTIVE_ORDERS.set(active_orders)
    ORDER_CANCELLED.inc()

    return {
        "status": "cancelled",
        "active_orders": active_orders
    }
