# System Design

## Overview

The CNRP SRE Platform is designed as a cloud-native microservice deployment that demonstrates modern DevOps and Site Reliability Engineering (SRE) practices.

The platform consists of a FastAPI-based Trading API running on Kubernetes with automated CI/CD, Infrastructure as Code, and a complete observability stack.

---

# High-Level Design

```
                   Client
                     │
                     ▼
             Kubernetes Service
                     │
                     ▼
             FastAPI Trading API
        ┌────────────┼─────────────┐
        │            │             │
        ▼            ▼             ▼
   Orders API   Trades API    Health API
        │            │             │
        └────────────┼─────────────┘
                     │
             Business Logic
                     │
         ┌───────────┼────────────┐
         │           │            │
         ▼           ▼            ▼
   Prometheus     Logging      Tracing
     Metrics       (Loki)      (Jaeger)
                     │
                     ▼
                 Grafana

```

---

# Application Components

## FastAPI

The Trading API exposes REST endpoints that simulate a lightweight trading platform.

Current APIs include:

- Health endpoint
- Orders endpoint
- Trades endpoint
- Metrics endpoint

The application is stateless and designed for horizontal scaling.

---

## Business Logic

The Trading API simulates order processing.

Operations include:

- Create order
- Retrieve orders
- Create trade
- Retrieve trades

The application also exposes metrics for:

- Request count
- Request latency
- Order metrics
- Error metrics

---

## Logging

Application logs are generated in structured JSON format.

Logs are collected by Loki and can be viewed in Grafana.

Benefits:

- Centralized logging
- Searchable logs
- Production-style troubleshooting

---

## Metrics

Prometheus collects application metrics.

Examples include:

- HTTP requests
- API latency
- Process CPU usage
- Memory usage
- Custom trading metrics

These metrics are visualized in Grafana dashboards.

---

## Distributed Tracing

Jaeger captures request traces.

Tracing enables:

- Request flow visualization
- Latency analysis
- Performance troubleshooting

---

# Deployment Design

The application is containerized using Docker.

Deployment workflow:

```
Source Code
      │
Docker Build
      │
Docker Image
      │
Amazon ECR
      │
Helm Chart
      │
Amazon EKS
```

---

# Kubernetes Design

The application is deployed using:

- Deployment
- Service
- Horizontal Pod Autoscaler

Deployment strategy:

- Rolling updates
- Multiple replicas
- Self-healing pods

---

# Helm Design

Helm is used to package Kubernetes manifests.

Configuration is externalized through:

- values.yaml
- values-dev.yaml
- values-prod.yaml

This enables environment-specific deployments without modifying templates.

---

# Infrastructure Design

Infrastructure is provisioned using Terraform.

Terraform modules include:

- VPC
- IAM
- EKS
- ECR
- RDS

Each module is reusable and independently maintainable.

---

# CI/CD Design

GitHub Actions automates the build pipeline.

Pipeline stages:

1. Checkout source
2. Install dependencies
3. Run unit tests
4. Run lint checks
5. Build Docker image
6. Push image to Amazon ECR
7. Validate Terraform

Infrastructure provisioning remains a manual approval step.

---

# Observability Design

The platform follows the three pillars of observability.

## Metrics

Prometheus

Collects:

- Infrastructure metrics
- Application metrics
- Business metrics

---

## Logs

Loki

Stores structured application logs for centralized troubleshooting.

---

## Traces

Jaeger

Captures distributed request traces for latency analysis.

---

# Database Design

Amazon RDS PostgreSQL is provisioned using Terraform.

The current implementation focuses on infrastructure provisioning.

Future enhancements may include:

- SQLAlchemy integration
- Persistent order storage
- Trade history
- Portfolio management

---

# Scalability

The system is horizontally scalable.

Scaling mechanisms:

- Kubernetes Deployment
- Horizontal Pod Autoscaler
- Stateless application
- LoadBalancer Service

---

# Reliability

Reliability is achieved through:

- Kubernetes self-healing
- Health probes
- Infrastructure as Code
- Automated CI validation
- Monitoring and alerting

---

# Security

Security considerations include:

- AWS Security Groups
- Private subnets
- IAM roles
- Kubernetes namespaces
- Infrastructure managed through Terraform

---

# Design Decisions

| Decision | Reason |
|----------|--------|
| FastAPI | Lightweight, high-performance API framework |
| Docker | Consistent deployment across environments |
| Kubernetes | Container orchestration and scalability |
| Helm | Reusable Kubernetes deployments |
| Terraform | Infrastructure as Code |
| GitHub Actions | Automated CI pipeline |
| Prometheus | Metrics collection |
| Grafana | Visualization |
| Loki | Centralized logging |
| Jaeger | Distributed tracing |
| Amazon EKS | Managed Kubernetes service |
| Amazon ECR | Container image registry |
| Amazon RDS | Managed PostgreSQL database |

---

# Future Enhancements

The following improvements are planned for future iterations:

- Persistent PostgreSQL integration
- GitOps using ArgoCD
- Chaos Engineering experiments
- Advanced Grafana dashboards
- Alertmanager notification routing
- Multi-environment deployments
- Automated infrastructure approvals

---

# Conclusion

The CNRP SRE Platform demonstrates the complete lifecycle of a cloud-native application, including infrastructure provisioning, containerization, Kubernetes deployment, CI/CD automation, monitoring, logging, and operational troubleshooting.

The project follows modern DevOps and SRE principles while remaining modular, reproducible, and suitable for production-inspired environments.
