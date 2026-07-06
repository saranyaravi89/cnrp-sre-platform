from pydantic import BaseModel


class OrderModel(BaseModel):
    id: int
    symbol: str
    side: str
    quantity: int
    status: str


class TradeModel(BaseModel):
    id: int
    symbol: str
    price: float
    quantity: int