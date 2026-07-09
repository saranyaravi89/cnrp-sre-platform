# Troubleshooting Guide

This document captures common issues encountered during development and deployment of the CNRP SRE Platform, along with their resolutions.

---

# Table of Contents

- Terraform
- Docker
- Kubernetes
- Grafana
- GitHub Actions
- AWS
- Helm
- Python

---

# Terraform

## ECR Repository Not Empty

### Error

```text
RepositoryNotEmptyException
```

### Cause

Terraform cannot delete an Amazon ECR repository while it still contains Docker images.

### Resolution

Delete all images before destroying infrastructure.

```bash
aws ecr batch-delete-image \
  --repository-name cnrp-trading-api \
  --image-ids imageTag=latest
```

---

## VPC DependencyViolation

### Error

```text
The VPC has dependencies and cannot be deleted.
```

### Cause

AWS resources such as Load Balancers, Elastic Network Interfaces (ENIs), or Security Groups still exist.

### Resolution

Verify and remove dependent resources before running:

```bash
terraform destroy
```

---

# Docker

## Container Health Check Failing

### Symptoms

Container repeatedly restarts.

### Resolution

Verify:

- Health endpoint returns HTTP 200.
- Dockerfile includes a HEALTHCHECK instruction.
- Container port matches docker-compose configuration.

---

# Kubernetes

## LoadBalancer Not Deleting

### Symptoms

Terraform cannot destroy VPC.

### Cause

AWS LoadBalancer created by Kubernetes still exists.

### Resolution

Delete the Kubernetes Service:

```bash
kubectl delete service trading-api-service
```

Wait for AWS to remove the Load Balancer before retrying:

```bash
terraform destroy
```

---

## ImagePullBackOff

### Cause

Docker image not found in Amazon ECR.

### Resolution

Verify:

- Docker image pushed successfully.
- Helm image tag matches the image in ECR.
- Kubernetes has permission to pull images.

---

# Grafana

## Dashboard Not Provisioned

### Symptoms

Dashboard does not appear after starting Grafana.

### Cause

- Incorrect provisioning path.
- Dashboard JSON format incompatible with provisioning.

### Resolution

Verify:

```
observability/grafana/provisioning/dashboards/dashboards.yml
```

Ensure dashboards are mounted correctly:

```
/var/lib/grafana/dashboards
```

---

## Prometheus Panels Show "No Data"

### Cause

Application metrics not being exposed or Prometheus scraping incorrectly.

### Resolution

Verify:

```
http://localhost:8000/metrics
```

Check:

```
http://localhost:9090/targets
```

Ensure target status is **UP**.

---

# GitHub Actions

## Tests Cannot Import Application

### Error

```text
ModuleNotFoundError: No module named 'app'
```

### Resolution

Set the Python path before running tests.

```bash
export PYTHONPATH=services/trading_api
pytest
```

---

## Terraform Formatting Failure

### Error

```text
terraform fmt -check
```

### Resolution

Run:

```bash
terraform fmt -recursive
```

Commit formatting changes.

---

# AWS

## Security Group Cannot Be Deleted

### Cause

Security Group is attached to an AWS resource.

### Resolution

Check:

- Elastic Network Interfaces
- Load Balancers
- EC2 instances

Delete dependent resources before deleting the Security Group.

---

## Internet Gateway Cannot Be Detached

### Cause

Public IPs or Load Balancers still attached.

### Resolution

Delete LoadBalancer Services and wait for AWS cleanup before retrying.

---

# Helm

## Helm Lint Cannot Find Chart.yaml

### Cause

Command executed from the wrong directory.

### Resolution

Run from the repository root:

```bash
helm lint charts/trading-api
```

---

# Python

## Pytest Collection Errors

### Error

```text
ModuleNotFoundError
```

### Resolution

Run tests from the project root or configure `PYTHONPATH` appropriately.

---

## Flake8 Errors

### Common Issues

- Missing blank lines (`E302`)
- Missing newline at end of file (`W292`)

### Resolution

Format files or configure Flake8 rules as needed.

---

# Best Practices

- Never commit AWS credentials.
- Store secrets using GitHub Secrets, Kubernetes Secrets, or AWS Secrets Manager.
- Use immutable Docker image tags instead of `latest`.
- Keep Terraform state secure.
- Version-control `.terraform.lock.hcl`.
- Ignore `.venv/`, `.terraform/`, and `__pycache__/`.
- Validate infrastructure before deployment.

---

# Useful Commands

## Terraform

```bash
terraform fmt -recursive
terraform validate
terraform plan
terraform apply
terraform destroy
```

## Kubernetes

```bash
kubectl get pods
kubectl get svc
kubectl get deployments
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

## Helm

```bash
helm lint charts/trading-api
helm template trading-api charts/trading-api
```

## Docker

```bash
docker compose up --build
docker ps
docker logs <container-name>
```

## Testing

```bash
pytest
flake8 services/trading_api/app services/trading_api/tests --max-line-length=120
```

---

# References

- Terraform Documentation
- Kubernetes Documentation
- Helm Documentation
- AWS EKS Documentation
- Prometheus Documentation
- Grafana Documentation
- FastAPI Documentation
