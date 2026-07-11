# Cloud Native SRE Platform

![CI](https://github.com/saranyaravi89/cnrp-sre-platform/actions/workflows/ci.yml/badge.svg)

# CNRP SRE Platform

A cloud-native Site Reliability Engineering (SRE) platform demonstrating Infrastructure as Code, Kubernetes, CI/CD, observability, and cloud deployment using AWS.

---

# Project Overview

This project simulates a production-ready Trading API deployed on Amazon EKS using Terraform and monitored with a modern observability stack.

The objective was to build an end-to-end platform similar to what an SRE or DevOps engineer would maintain in production.

---

# Architecture

<img width="1536" height="1024" alt="High Level Architecture" src="https://github.com/user-attachments/assets/c694e032-9231-4fe0-9307-05cbfd6701ac" />

For detailed architecture, see:

- docs/architecture.md
- docs/aws_architecture.md
- docs/system_design.md
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
git clone https://github.com/saranyaravi89/cnrp-sre-platform.git
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
helm upgrade --install trading-api charts/trading-api \
  -f charts/trading-api/values-prod.yaml
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

- Amazon EKS
<img width="3195" height="1577" alt="AWS EKS Cluster" src="https://github.com/user-attachments/assets/afbf8ca4-761d-4da0-a771-2b15cd9cdc1a" />

- Amazon RDS
  <img width="1281" height="1215" alt="RDS_Instance" src="https://github.com/user-attachments/assets/f0f44c4a-7d08-46bf-be80-d57c2c5aa1fd" />

- Amazon ECR
  <img width="3187" height="1562" alt="ECR Repository" src="https://github.com/user-attachments/assets/9089c51e-8343-4bd8-aa54-fd2aa689ff8c" />

- Kubernetes Pods
  <img width="1945" height="360" alt="Kubernetes Pods" src="https://github.com/user-attachments/assets/9da278bc-72ea-4193-af5c-43f33ac560b5" />

- Kubernetes Services
  <img width="1957" height="360" alt="kubernetes-services" src="https://github.com/user-attachments/assets/5eef573e-0ed2-4b9d-b2b3-bf4105aef050" />

- Grafana Dashboard
  <img width="2947" height="1185" alt="API-Overview-Grafana-Dashboard" src="https://github.com/user-attachments/assets/fe94c748-a0d4-4fc1-84c2-d32572aff423" />
  <img width="2945" height="750" alt="Application-Performance-Grafana-Dashboard" src="https://github.com/user-attachments/assets/6b124a52-ebda-4be2-9154-6bd52bc03f41" />

- Prometheus Targets
  <img width="3180" height="1590" alt="prometheus-targets" src="https://github.com/user-attachments/assets/91fee418-22fc-4fa9-af84-c940a0d0982d" />

- GitHub Actions CI
  <img width="3190" height="1587" alt="GitHub_Actions" src="https://github.com/user-attachments/assets/8904eb64-95c5-4069-8fcd-05717ce3695a" />

- GitHub Actions Deploy
  <img width="3185" height="1292" alt="Github Actions Deploy Workflow" src="https://github.com/user-attachments/assets/527c362a-e38f-4d2a-ab74-fb16ededbdfc" />

- Jaeger Tracing
  <img width="1281" height="1215" alt="Jaeger_tracing" src="https://github.com/user-attachments/assets/a5bab7ae-fb3a-4dd9-9026-6488737fdc94" />

- LoadBalancer Health Response
  <img width="2627" height="302" alt="LoadBalancerHealthResponse" src="https://github.com/user-attachments/assets/81eb2224-ac7a-4e3a-ae67-204735c156dd" />



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

