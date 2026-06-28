# Architecture Overview

## Purpose

This project demonstrates a cloud-native SRE platform for a Trading API. It includes application development, observability, containerization, Kubernetes deployment, AWS infrastructure, CI/CD, and troubleshooting practices.

## High-Level Architecture

```text
User / Client
     |
     v
FastAPI Trading API
     |
     |-- /health   -> Health check
     |-- /orders   -> Sample business endpoint
     |-- /metrics  -> Prometheus metrics
     |
     v
Docker Container
     |
     v
Docker Compose / Kubernetes
     |
     +--------------------+
     | Observability      |
     |                    |
     | Prometheus Metrics |
     | Grafana Dashboard  |
     | Loki Logs          |
     | Jaeger Traces      |
     +--------------------+
```

## Components

### FastAPI Trading API

The application exposes REST endpoints used to simulate a trading service.

Key endpoints:

```text
/health
/orders
/metrics
```

### Docker

The app is containerized using Docker so that it can run consistently across local and cloud environments.

### Observability

The platform includes:

```text
Prometheus -> metrics
Grafana    -> dashboards
Loki       -> logs
Jaeger     -> traces
```

### Kubernetes

Kubernetes manifests define deployment, service, ingress, and autoscaling behavior.

### Terraform

Terraform defines AWS infrastructure such as VPC, subnets, IAM roles, EKS, and networking.

## Reliability Goals

```text
Health checks
Metrics collection
Structured logging
Distributed tracing
Autoscaling
Troubleshooting scenarios
Incident documentation
```

## Current Status

```text
FastAPI        : Implemented
Docker         : Implemented
Prometheus     : Implemented
Grafana        : Implemented
Loki           : Implemented
Jaeger         : Implemented
Kubernetes     : Configured
Terraform AWS  : Configured
EKS Deployment : Planned
CI/CD          : Basic CI implemented
```
