from fastapi import APIRouter
from random import choice, randint
from app.observability.metrics import TRADE_EXECUTED

router = APIRouter()


@router.get("/trades")
def get_trades():
    return {
        "trades": [
            {"id": 1, "symbol": "AAPL", "price": 190.5, "quantity": 10},
            {"id": 2, "symbol": "NVDA", "price": 880.2, "quantity": 5}
        ]
    }


@router.post("/trades/execute")
def execute_trade():
    symbol = choice(["AAPL", "MSFT", "TSLA", "NVDA"])
    quantity = randint(1, 50)

    TRADE_EXECUTED.inc()

    return {
        "status": "executed",
        "symbol": symbol,
        "quantity": quantity
    }
