from fastapi import APIRouter

router = APIRouter()

@router.get("/metrics")
def metrics():
    return {"requests": 1, "errors": 0}