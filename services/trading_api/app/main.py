from fastapi import FastAPI, Request
from app.api.health import router as health_router
from app.api.orders import router as orders_router
from app.api.trades import router as trades_router
from app.observability.metrics import router as metrics_router, REQUEST_COUNT, REQUEST_LATENCY
from app.core.logging import get_logger

logger = get_logger()

app = FastAPI()

logger.info("Trading API started")

@app.middleware("http")
async def count_requests(request: Request, call_next):
    logger.info(f"{request.method} {request.url.path}")
    REQUEST_COUNT.inc()

    with REQUEST_LATENCY.time():
        response = await call_next(request)

    return response

app.include_router(health_router)
app.include_router(orders_router)
app.include_router(trades_router)
app.include_router(metrics_router)