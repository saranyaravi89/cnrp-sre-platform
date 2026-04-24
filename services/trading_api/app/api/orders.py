from fastapi import APIRouter

router = APIRouter()

@router.get("/orders")
def get_orders():
    return [{"id": 1, "status": "filled"}]