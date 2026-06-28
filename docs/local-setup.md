# Local Setup

## Start stack
docker-compose up --build -d

## Stop stack
docker-compose down

## Test API
curl http://localhost:8000/health
curl http://localhost:8000/orders
curl http://localhost:8000/metrics