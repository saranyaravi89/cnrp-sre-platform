# Operations Runbook

This document provides operational procedures for deploying, monitoring, troubleshooting, and recovering the CNRP SRE Platform.

---

# Table of Contents

- Local Development
- AWS Deployment
- Kubernetes Operations
- Observability
- Database
- Incident Response
- Disaster Recovery
- Useful Commands

---

# Local Development

## Start the Platform

```bash
docker compose up --build
```

Verify services:

| Service | URL |
|---------|-----|
| Trading API | http://localhost:8000 |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |
| Jaeger | http://localhost:16686 |

---

## Stop the Platform

```bash
docker compose down
```

---

# AWS Deployment

## Provision Infrastructure

```bash
cd infra/aws

terraform init
terraform plan
terraform apply
```

---

## Configure kubectl

```bash
aws eks update-kubeconfig \
  --region ap-southeast-1 \
  --name cnrp-cluster
```

Verify:

```bash
kubectl get nodes
```

---

## Deploy Application

```bash
helm upgrade --install trading-api charts/trading-api \
-f charts/trading-api/values-prod.yaml
```

Verify deployment:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

---

# Kubernetes Operations

## Check Pod Status

```bash
kubectl get pods
```

---

## Describe a Pod

```bash
kubectl describe pod <pod-name>
```

---

## View Logs

```bash
kubectl logs <pod-name>
```

---

## Restart Deployment

```bash
kubectl rollout restart deployment trading-api
```

---

## Verify Rollout

```bash
kubectl rollout status deployment trading-api
```

---

# Observability

## Verify Prometheus Targets

Open:

```
http://localhost:9090/targets
```

Ensure all targets show **UP**.

---

## Verify Grafana

Open:

```
http://localhost:3000
```

Check dashboards:

- API Overview
- Application Performance

---

## Verify Loki Logs

Open Grafana

Explore → Loki

Search logs:

```
{job="trading-api"}
```

---

## Verify Jaeger

Open:

```
http://localhost:16686
```

Search for:

```
trading-api
```

---

# Database

## Verify PostgreSQL Connectivity

If deployed:

```bash
psql \
-h <rds-endpoint> \
-U postgres \
-d trading
```

---

# Incident Response

## API Unavailable

### Symptoms

- HTTP 5xx
- Load Balancer unhealthy

### Actions

```bash
kubectl get pods
kubectl logs <pod-name>
kubectl describe pod <pod-name>
```

If required:

```bash
kubectl rollout restart deployment trading-api
```

---

## High CPU Usage

Check:

```bash
kubectl top pods
```

Verify:

- HPA status
- Resource requests
- Resource limits

---

## Pod CrashLoopBackOff

Describe pod:

```bash
kubectl describe pod <pod-name>
```

Check logs:

```bash
kubectl logs <pod-name>
```

---

## ImagePullBackOff

Verify:

- Image exists in ECR
- Helm image tag
- IAM permissions

---

## Grafana Dashboard Missing

Verify provisioning:

```
observability/grafana/provisioning/
```

Restart Grafana:

```bash
docker compose restart grafana
```

---

## Prometheus Shows No Data

Verify metrics endpoint:

```
http://localhost:8000/metrics
```

Verify target status:

```
http://localhost:9090/targets
```

---

# Disaster Recovery

## Recreate Infrastructure

```bash
terraform apply
```

---

## Redeploy Application

```bash
helm upgrade --install trading-api charts/trading-api
```

---

## Restore Dashboards

Grafana automatically provisions dashboards from:

```
observability/grafana/dashboards/
```

---

# Infrastructure Cleanup

Destroy infrastructure:

```bash
terraform destroy
```

If dependencies remain:

- Delete Kubernetes LoadBalancer Service
- Delete remaining ECR images
- Retry destroy

---

# Useful Commands

## Docker

```bash
docker compose up --build
docker compose down
docker ps
docker logs <container>
```

---

## Kubernetes

```bash
kubectl get pods
kubectl get svc
kubectl get deployments
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl rollout restart deployment trading-api
kubectl rollout status deployment trading-api
```

---

## Helm

```bash
helm lint charts/trading-api
helm template trading-api charts/trading-api
helm upgrade --install trading-api charts/trading-api
```

---

## Terraform

```bash
terraform fmt -recursive
terraform validate
terraform plan
terraform apply
terraform destroy
```

---

## Testing

```bash
pytest

flake8 services/trading_api/app services/trading_api/tests \
--max-line-length=120
```

---

# Operational Best Practices

- Validate Terraform before applying changes.
- Run unit tests before pushing code.
- Monitor Prometheus targets after deployment.
- Verify Grafana dashboards after provisioning.
- Use immutable Docker image tags.
- Store secrets in GitHub Secrets or Kubernetes Secrets.
- Review logs and traces before restarting workloads.
