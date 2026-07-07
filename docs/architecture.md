# System Architecture

## Overview

The CNRP SRE Platform demonstrates a cloud-native application deployed using modern DevOps and Site Reliability Engineering (SRE) practices.

The platform provisions AWS infrastructure using Terraform, deploys a FastAPI-based Trading API to Amazon EKS, and provides complete observability through Prometheus, Grafana, Loki, Jaeger, and Blackbox Exporter.

---

# High-Level Architecture

```
                          Developer
                              │
                        Git Push
                              │
                     GitHub Repository
                              │
                    GitHub Actions CI/CD
                              │
                 Build • Test • Docker Build
                              │
                      Push Image to ECR
                              │
                      Amazon Elastic
                    Container Registry
                              │
                              ▼
                    Amazon EKS Cluster
                              │
                    Helm Deployment Chart
                              │
                     Trading API (FastAPI)
                              │
        ┌──────────────┬──────────────┬──────────────┐
        │              │              │              │
   Prometheus       Loki          Jaeger      Blackbox Exporter
        │              │              │              │
        └──────────────┴──────────────┴──────────────┘
                              │
                           Grafana
                              │
                      Dashboards & Metrics


Infrastructure Provisioning

Terraform
    │
    ▼
AWS
├── VPC
├── Public Subnets
├── Private Subnets
├── Internet Gateway
├── Route Tables
├── Security Groups
├── Amazon EKS
├── Amazon ECR
└── Amazon RDS PostgreSQL
```

---

# Components

## Trading API

The Trading API is a FastAPI application that simulates order and trade processing.

Endpoints include:

- Health endpoint
- Orders endpoint
- Trades endpoint
- Prometheus metrics endpoint

The application also provides:

- Structured JSON logging
- OpenTelemetry instrumentation
- Prometheus metrics

---

## Infrastructure

Infrastructure is provisioned using Terraform.

Resources include:

- Custom VPC
- Public and Private Subnets
- Internet Gateway
- Route Tables
- Security Groups
- Amazon EKS Cluster
- Amazon ECR Repository
- Amazon RDS PostgreSQL

Infrastructure follows Infrastructure as Code (IaC) principles and can be provisioned or destroyed using Terraform.

---

## Kubernetes

The application is deployed to Amazon EKS using Helm.

Resources include:

- Deployment
- Service
- Horizontal Pod Autoscaler (HPA)

Helm enables environment-specific configuration through configurable values files.

---

## CI/CD

GitHub Actions automates the software delivery process.

Pipeline stages include:

- Source checkout
- Dependency installation
- Unit testing
- Linting
- Docker image build
- Push image to Amazon ECR
- Terraform validation

Infrastructure deployment remains a manual approval step to avoid accidental provisioning.

---

## Observability

The platform includes a complete observability stack.

### Prometheus

Responsible for collecting application and infrastructure metrics.

Examples:

- Request count
- Request latency
- Order metrics
- CPU usage
- Memory usage

---

### Grafana

Grafana visualizes metrics collected by Prometheus.

Current dashboards include:

- API Overview
- Application Performance

---

### Loki

Centralized log aggregation.

Application logs are collected and searchable from Grafana.

---

### Jaeger

Distributed tracing for API requests.

Used to visualize request flow and latency.

---

### Blackbox Exporter

Performs external health checks against application endpoints.

Used to verify endpoint availability independently of application metrics.

---

# Security

The platform follows AWS security best practices.

- Private networking where appropriate
- Security Groups restrict access
- Kubernetes workloads are isolated within the cluster
- Infrastructure managed through Terraform

---

# Scalability

The application supports horizontal scaling using:

- Kubernetes Deployments
- Horizontal Pod Autoscaler
- LoadBalancer Service
- Stateless application design

---

# Repository Layout

```
cnrp-sre-platform
│
├── services/
│   └── trading_api/
│
├── infra/
│   └── aws/
│
├── charts/
│   └── trading-api/
│
├── observability/
│   ├── grafana/
│   ├── prometheus/
│   ├── loki/
│   ├── jaeger/
│   └── blackbox/
│
├── docs/
│
├── chaos/
│
└── scripts/
```

---

# Deployment Flow

1. Developer pushes code to GitHub.
2. GitHub Actions runs tests and validation.
3. Docker image is built.
4. Image is pushed to Amazon ECR.
5. Terraform provisions AWS infrastructure (manual).
6. Helm deploys the application to Amazon EKS.
7. Prometheus collects metrics.
8. Loki collects logs.
9. Jaeger collects traces.
10. Grafana visualizes operational data.

---

# Design Decisions

The following technologies were selected:

| Technology | Purpose |
|------------|---------|
| FastAPI | Lightweight REST API |
| Docker | Containerization |
| Kubernetes | Container orchestration |
| Helm | Kubernetes package management |
| Terraform | Infrastructure as Code |
| AWS EKS | Managed Kubernetes |
| Amazon ECR | Container registry |
| Amazon RDS | Managed PostgreSQL |
| Prometheus | Metrics collection |
| Grafana | Dashboards |
| Loki | Centralized logging |
| Jaeger | Distributed tracing |
| GitHub Actions | Continuous Integration |
