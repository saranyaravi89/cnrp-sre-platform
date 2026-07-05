from fastapi import APIRouter, Response
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST

router = APIRouter()

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total API requests",
    ["method", "path", "status"]
)

ORDER_CREATED = Counter(
    "trading_orders_created_total",
    "Total orders created"
)

ORDER_CANCELLED = Counter(
    "trading_orders_cancelled_total",
    "Total orders cancelled"
)

TRADE_EXECUTED = Counter(
    "trading_trades_executed_total",
    "Total trades executed"
)

ORDER_FAILED = Counter(
    "trading_orders_failed_total",
    "Total failed orders"
)

REQUEST_LATENCY = Histogram(
    "trading_request_latency_seconds",
    "Request latency in seconds"
)

ACTIVE_ORDERS = Gauge(
    "trading_active_orders",
    "Current active orders"
)

@router.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)