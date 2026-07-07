from pydantic import BaseModel


class TradeResponse(BaseModel):
    id: int
    symbol: str
    price: float
    quantity: int
