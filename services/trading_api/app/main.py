from fastapi import FastAPI, Request
from app.api.health import router as health_router
from app.api.orders import router as orders_router
from app.observability.metrics import router as metrics_router, REQUEST_COUNT
from app.core.logging import get_logger
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from app.core.tracing import setup_tracing

logger = get_logger()

app = FastAPI()

setup_tracing()
FastAPIInstrumentor.instrument_app(app)

logger.info("Trading API started")

@app.middleware("http")
async def count_requests(request: Request, call_next):
    logger.info(f"{request.method} {request.url.path}")
    REQUEST_COUNT.inc()
    response = await call_next(request)
    return response

app.include_router(health_router)
app.include_router(orders_router)
app.include_router(metrics_router)