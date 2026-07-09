# AWS Infrastructure Architecture

## Overview

The CNRP SRE Platform is deployed on Amazon Web Services (AWS) using Terraform as Infrastructure as Code (IaC).

The infrastructure provides a secure, scalable, and production-inspired environment for running a cloud-native Trading API on Amazon Elastic Kubernetes Service (EKS).

---

# Architecture

<img width="1536" height="1024" alt="WhatsApp Image 2026-07-09 at 11 23 16 PM" src="https://github.com/user-attachments/assets/1a32b28b-0ae9-4b94-adf3-d132d4d55566" />


---

# Infrastructure Components

## Amazon VPC

A custom Virtual Private Cloud (VPC) provides network isolation for all infrastructure resources.

Responsibilities:

- Network segmentation
- Routing
- Security boundaries

---

## Public Subnets

Public subnets host internet-facing resources such as:

- Internet Gateway
- Kubernetes LoadBalancer Service

Public resources receive external traffic.

---

## Private Subnets

Private subnets host application workloads.

Resources include:

- Amazon EKS worker nodes
- Trading API containers
- Amazon RDS PostgreSQL

Application workloads are isolated from direct internet access.

---

## Internet Gateway

Provides outbound internet connectivity for public resources.

Used by:

- Kubernetes LoadBalancer
- Public AWS endpoints

---

## Security Groups

Security Groups control inbound and outbound traffic.

Configured for:

- EKS Cluster
- Worker Nodes
- RDS PostgreSQL
- Load Balancer

Only required ports are exposed.

---

## Amazon Elastic Kubernetes Service (EKS)

Amazon EKS hosts the Trading API.

Kubernetes resources include:

- Deployment
- Service
- Horizontal Pod Autoscaler

The cluster provides:

- High availability
- Container orchestration
- Rolling updates
- Auto healing

---

## Amazon Elastic Container Registry (ECR)

Docker images are stored in Amazon ECR.

GitHub Actions builds the application image and pushes it to ECR before deployment.

---

## Amazon RDS PostgreSQL

Amazon RDS provides managed PostgreSQL.

Purpose:

- Persistent relational storage
- Managed backups
- Automated maintenance
- High reliability

(Current implementation provisions the database infrastructure. Application integration can be extended in future iterations.)

---

# Deployment Flow

```
Developer
      │
GitHub Push
      │
GitHub Actions
      │
Docker Build
      │
Amazon ECR
      │
Helm Deployment
      │
Amazon EKS
      │
Trading API
```

---

# Terraform Modules

Infrastructure is organized into reusable Terraform modules.

Current modules include:

```
infra/aws/

├── ecr/
├── eks/
├── rds/
├── vpc/
├── iam/
└── main.tf
```

Each module is responsible for provisioning a specific AWS service.

---

# Security Design

Security considerations include:

- Custom VPC
- Private application subnets
- Security Groups
- IAM Roles for EKS
- Infrastructure managed through Terraform
- No hard-coded AWS credentials

---

# Scalability

The infrastructure supports horizontal scaling through:

- Kubernetes Deployments
- Horizontal Pod Autoscaler
- Amazon EKS
- LoadBalancer Service

Application containers remain stateless, enabling additional replicas without application changes.

---

# Cost Optimization

The project uses lightweight AWS resources where possible:

- t3.micro instances
- Small PostgreSQL instance
- Infrastructure destroyed after validation
- Terraform used to avoid configuration drift

---

# Infrastructure Validation

Infrastructure was validated by provisioning and verifying:

- Amazon VPC
- Public and Private Subnets
- Internet Gateway
- Security Groups
- Amazon EKS Cluster
- Amazon ECR Repository
- Amazon RDS PostgreSQL
- Kubernetes LoadBalancer
- Terraform Apply
- Terraform Destroy

---

# Lessons Learned

During implementation, several real-world operational challenges were encountered and resolved:

- AWS subnet dependency violations during Terraform destroy
- Kubernetes LoadBalancer cleanup
- ECR repository deletion constraints
- Terraform state management
- AWS networking dependencies
- Security group cleanup
- Kubernetes deployment validation

These troubleshooting activities provided practical experience with AWS infrastructure lifecycle management.
