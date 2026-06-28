# Cloud Native SRE Platform

![CI](https://github.com/saranyaravi89/cnrp-sre-platform/actions/workflows/ci.yml/badge.svg)

## Overview

Cloud Native SRE Platform is a production-inspired Site Reliability Engineering project demonstrating observability, Kubernetes, AWS infrastructure, Infrastructure as Code, CI/CD, and incident troubleshooting using modern cloud-native technologies.

---
## SRE Concepts Demonstrated

- Health Checks
- Metrics
- Structured Logging
- Distributed Tracing
- Infrastructure as Code
- Kubernetes Deployments
- Auto Scaling
- Incident Documentation
- Runbooks
- CI/CD


## Architecture

```
Users
   │
   ▼
FastAPI Trading API
   │
   ├── Prometheus Metrics
   ├── JSON Logs
   └── OpenTelemetry Traces
        │
        ▼
Grafana
 ├── Prometheus
 ├── Loki
 └── Jaeger

Docker
   │
Kubernetes (EKS)

Terraform
   │
AWS Infrastructure

GitHub Actions
   │
CI/CD Pipeline
```

---

## Technologies

* Python
* FastAPI
* Docker
* Kubernetes
* AWS
* Terraform
* Prometheus
* Grafana
* Loki
* Jaeger
* GitHub Actions

---

## Features

* REST API
* Health Checks
* Dockerized Application
* Prometheus Metrics
* Structured JSON Logging
* Distributed Tracing
* Kubernetes Deployment
* Horizontal Pod Autoscaler
* GitHub Actions CI
* Terraform Infrastructure
* Incident Runbooks
* Kubernetes Troubleshooting Lab

---

## Repository Structure

```
services/
infra/
observability/
chaos/
cicd/
docs/
scripts/
```

---

## Current Status

✅ FastAPI service structure  
✅ Initial API setup  
✅ Docker setup in progress  
✅ Observability design in progress  
✅ Terraform/EKS structure created  
🚧 Kubernetes deployment in progress  
🚧 GitHub Actions CI/CD in progress  
🚧 Prometheus/Grafana/Loki/Jaeger integration in progress  
🚧 Incident runbooks and troubleshooting labs planned  

---

## Screenshots

* API
* Grafana Dashboard
* Prometheus
* Loki Logs
* Jaeger Traces
* GitHub Actions
* AWS EKS

---

## Future Enhancements

* AI-assisted RCA
* Automated Incident Response
* Slack Notifications
* GitOps
* ArgoCD
* Multi-region Deployment

---
## What I Learned
* Building cloud-native applications
* Kubernetes troubleshooting
* Infrastructure as Code with Terraform
* Observability using Prometheus, Grafana, Loki, and Jaeger
* CI/CD automation
* Incident management and reliability engineering

## Author

Saranya Sakthivel
AWS Certified Solutions Architect Associate
13+ Years Production Support → Site Reliability Engineering
