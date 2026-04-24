from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.orders import router as orders_router
from app.observability.metrics import router as metrics_router
from app.core.logging import get_logger

app = FastAPI()
logger = get_logger()

app.include_router(health_router)
app.include_router(orders_router)
app.include_router(metrics_router)

logger.info("Service started")