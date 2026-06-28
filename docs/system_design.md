# System Design

## System Goal

The goal of this project is to design a production-inspired SRE platform for a Trading API with observability, automation, cloud infrastructure, and troubleshooting capabilities.

## System Context

```text
Client
  |
  v
Trading API
  |
  +--> Metrics
  +--> Logs
  +--> Traces
  |
  v
Observability Stack
```

## Application Design

The Trading API is built using FastAPI.

```text
services/trading_api/
├── app/
│   ├── main.py
│   ├── api/
│   ├── core/
│   ├── observability/
│   ├── db/
│   └── schemas/
```

## API Endpoints

```text
GET /health
GET /orders
GET /metrics
```

## Observability Design

```text
Application
   |
   +--> Prometheus metrics
   +--> JSON logs
   +--> OpenTelemetry traces
```

## Metrics Flow

```text
FastAPI /metrics
      |
      v
Prometheus
      |
      v
Grafana Dashboard
```

## Logging Flow

```text
FastAPI JSON Logs
      |
      v
Promtail
      |
      v
Loki
      |
      v
Grafana Explore
```

## Tracing Flow

```text
FastAPI Request
      |
      v
OpenTelemetry
      |
      v
Jaeger
      |
      v
Trace Analysis
```

## Kubernetes Design

```text
Deployment
   |
   +--> 2 replicas
   +--> livenessProbe
   +--> readinessProbe
   +--> resource requests
   +--> resource limits
   +--> rolling update strategy
   |
Service
   |
   v
LoadBalancer
```

## Reliability Features

```text
Health checks
Prometheus metrics
Structured logging
Distributed tracing
Horizontal Pod Autoscaler
Kubernetes troubleshooting scenarios
Incident templates
Runbooks
```

## Failure Scenarios

The project includes Kubernetes troubleshooting examples for:

```text
CrashLoopBackOff
ImagePullBackOff
OOMKilled
High latency
Application outage
```

## CI/CD Design

```text
GitHub Push
    |
    v
GitHub Actions
    |
    +--> Checkout code
    +--> Setup Python
    +--> Install dependencies
    +--> Build Docker image
```

Future deployment pipeline:

```text
GitHub Actions
    |
    v
Build Docker Image
    |
    v
Push to ECR
    |
    v
Deploy to EKS
```

## SRE Concepts Demonstrated

```text
SLI/SLO thinking
Health checks
Incident response
Root cause analysis
Observability
Infrastructure as Code
Cloud deployment
Kubernetes operations
CI/CD automation
Troubleshooting
```

## Future Enhancements

```text
AWS ECR deployment
EKS live deployment
ALB ingress
TLS certificate
Prometheus alerts
Chaos engineering
AI incident analyzer
Slack alert integration
Automated RCA generation
```
