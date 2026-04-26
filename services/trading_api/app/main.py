from fastapi import FastAPI, Request
from app.api.health import router as health_router
from app.api.orders import router as orders_router
from app.observability.metrics import router as metrics_router, REQUEST_COUNT

app = FastAPI()

@app.middleware("http")
async def count_requests(request: Request, call_next):
    REQUEST_COUNT.inc()
    response = await call_next(request)
    return response

app.include_router(health_router)
app.include_router(orders_router)
app.include_router(metrics_router)