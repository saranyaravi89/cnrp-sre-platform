# Cloud Native SRE Platform

![CI](https://github.com/saranyaravi89/cnrp-sre-platform/actions/workflows/ci.yml/badge.svg)

## Overview

Cloud Native SRE Platform demonstrating production-ready Site Reliability Engineering practices using FastAPI, Docker, Kubernetes, AWS, Prometheus, Grafana, Loki, Jaeger, Terraform and GitHub Actions.

---

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

## Roadmap

* [x] FastAPI
* [x] Docker
* [x] Prometheus
* [x] Grafana
* [ ] Loki
* [ ] Jaeger
* [x] Kubernetes Manifests
* [ ] AWS EKS
* [ ] Terraform
* [ ] GitHub Actions
* [ ] Chaos Engineering
* [ ] AI Incident Analyzer

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

## Author

Saranya Sakthivel
AWS Certified Solutions Architect Associate
13+ Years Production Support → Site Reliability Engineering
