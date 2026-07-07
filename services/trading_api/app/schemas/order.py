from pydantic import BaseModel


class OrderRequest(BaseModel):
    symbol: str
    side: str
    quantity: int
