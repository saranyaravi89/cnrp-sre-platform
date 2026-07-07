# Cloud Native SRE Platform

![CI](https://github.com/saranyaravi89/cnrp-sre-platform/actions/workflows/ci.yml/badge.svg)

# Overview

A cloud-native Site Reliability Engineering (SRE) platform demonstrating Infrastructure as Code, Kubernetes, CI/CD, observability, and cloud deployment using AWS.

---

# Project Overview

This project simulates a production-ready Trading API deployed on Amazon EKS using Terraform and monitored with a modern observability stack.

The objective was to build an end-to-end platform similar to what an SRE or DevOps engineer would maintain in production.

---

# Architecture

```
Developer
    │
Git Push
    │
GitHub Actions
    │
Docker Build
    │
Amazon ECR
    │
Amazon EKS
    │
Trading API (FastAPI)
    │
 ┌──────────────┬─────────────┬────────────┐
 │              │             │            │
Prometheus    Grafana       Loki       Jaeger
 │
Terraform
 │
AWS
├── VPC
├── Public & Private Subnets
├── Internet Gateway
├── Route Tables
├── Security Groups
├── Amazon EKS
├── Amazon ECR
└── Amazon RDS (PostgreSQL)
```

---

# Features

## Infrastructure

- Terraform Infrastructure as Code
- Custom AWS VPC
- Public & Private Subnets
- Route Tables
- Internet Gateway
- Security Groups
- Amazon EKS Cluster
- Amazon ECR Repository
- Amazon RDS PostgreSQL
- Infrastructure validation using Terraform

---

## Application

- FastAPI Trading API
- Health endpoint
- Orders API
- Trades API
- Structured JSON logging
- Prometheus metrics
- OpenTelemetry tracing

---

## CI/CD

- GitHub Actions
- Python testing (pytest)
- Flake8 linting
- Docker image build
- Amazon ECR push
- Terraform validation

---

## Kubernetes

- Deployments
- Services
- Horizontal Pod Autoscaler
- Helm Charts
- Rolling Updates

---

## Observability

- Prometheus
- Grafana
- Loki
- Jaeger
- Blackbox Exporter

Current dashboards include:

- API Overview
- Application Performance

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | FastAPI |
| Container | Docker |
| Orchestration | Kubernetes |
| Package Manager | Helm |
| Infrastructure | Terraform |
| Cloud | AWS |
| Container Registry | Amazon ECR |
| Kubernetes | Amazon EKS |
| Database | PostgreSQL (Amazon RDS) |
| Monitoring | Prometheus |
| Visualization | Grafana |
| Logging | Loki |
| Tracing | Jaeger |
| CI/CD | GitHub Actions |

---

# Repository Structure

```
cnrp-sre-platform/
│
├── .github/
│   └── workflows/
│
├── charts/
│   └── trading-api/
│
├── docs/
│
├── infra/
│   └── aws/
│
├── observability/
│   ├── grafana/
│   ├── prometheus/
│   ├── loki/
│   ├── jaeger/
│   └── blackbox/
│
├── services/
│   └── trading_api/
│
├── chaos/
│
├── scripts/
│
└── README.md
```

---

# Local Setup

Clone repository

```bash
git clone https://github.com/<your-username>/cnrp-sre-platform.git
```

Install dependencies

```bash
pip install -r services/trading_api/requirements.txt
```

Start platform

```bash
docker-compose up --build
```

Trading API

```
http://localhost:8000
```

Prometheus

```
http://localhost:9090
```

Grafana

```
http://localhost:3000
```

Jaeger

```
http://localhost:16686
```

---

# AWS Deployment

Infrastructure

```bash
cd infra/aws

terraform init
terraform plan
terraform apply
```

Configure kubectl

```bash
aws eks update-kubeconfig --region ap-southeast-1 --name cnrp-cluster
```

Deploy application

```bash
helm upgrade --install trading-api charts/trading-api
```

Destroy infrastructure

```bash
terraform destroy
```

---

# Testing

Run unit tests

```bash
pytest
```

Run linting

```bash
flake8
```

Validate Terraform

```bash
terraform validate
```

Validate Helm

```bash
helm lint charts/trading-api
```

---

# Screenshots

Include screenshots for:

- AWS VPC
- Amazon EKS
- Amazon RDS
- Amazon ECR
- Kubernetes Pods
- Kubernetes Services
- Grafana Dashboard
- Prometheus Targets
- GitHub Actions CI
- GitHub Actions Deploy

---

# Challenges Solved

During this project the following production issues were identified and resolved:

- Terraform dependency violations
- Kubernetes LoadBalancer cleanup
- ECR repository cleanup
- Grafana dashboard provisioning
- GitHub Actions PYTHONPATH configuration
- Structured logging in CI
- Terraform formatting validation
- AWS networking and security group cleanup

---

# Future Improvements

- Chaos Engineering experiments
- ArgoCD GitOps deployment
- Alertmanager notification routing
- Advanced Grafana dashboards
- Kubernetes Network Policies
- Automated infrastructure deployment approvals

---

# Key Learning Outcomes

- Infrastructure as Code with Terraform
- Kubernetes application deployment
- CI/CD using GitHub Actions
- Production observability
- AWS networking
- Helm packaging
- Cloud-native application deployment
- SRE operational troubleshooting

---
