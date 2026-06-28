# AWS Architecture

## Purpose

This document explains the AWS architecture designed for the Cloud Native SRE Platform.

## AWS Architecture Diagram

```text
AWS Region: ap-southeast-1
|
+--------------------------------------------------+
| VPC: cnrp-vpc                                    |
| CIDR: 10.0.0.0/16                                |
|                                                  |
|  +----------------------+    +----------------+  |
|  | Public Subnet         |    | Private Subnet |  |
|  | 10.0.1.0/24           |    | 10.0.2.0/24    |  |
|  |                      |    |                |  |
|  | Internet Gateway     |    | EKS Nodes      |  |
|  | NAT Gateway          |--->| Trading API    |  |
|  +----------------------+    +----------------+  |
|                                                  |
|  +--------------------------------------------+  |
|  | EKS Cluster                                |  |
|  | - Managed Node Group                       |  |
|  | - Kubernetes Workloads                     |  |
|  | - HPA                                      |  |
|  +--------------------------------------------+  |
|                                                  |
|  +--------------------------------------------+  |
|  | IAM Roles                                  |  |
|  | - EKS Cluster Role                         |  |
|  | - EKS Node Role                            |  |
|  +--------------------------------------------+  |
+--------------------------------------------------+
```

## AWS Services Used

### VPC

A custom VPC is created to isolate project resources.

```text
CIDR: 10.0.0.0/16
```

### Public Subnet

Used for internet-facing resources such as NAT Gateway or Load Balancer.

```text
10.0.1.0/24
```

### Private Subnet

Used for EKS worker nodes and internal workloads.

```text
10.0.2.0/24
```

### Internet Gateway

Allows public subnet resources to access the internet.

### NAT Gateway

Allows private subnet resources to access the internet without exposing them publicly.

### Route Tables

Public route table sends internet traffic through Internet Gateway.

Private route table sends outbound traffic through NAT Gateway.

### EKS

Amazon EKS is used to run Kubernetes workloads.

### IAM

IAM roles are created for:

```text
EKS control plane
EKS worker nodes
ECR access
CNI networking
```

## Terraform Modules

```text
infra/aws/
├── main.tf
├── provider.tf
├── backend.tf
├── vpc/
├── iam/
└── eks/
```

## Cost Awareness

Main AWS cost drivers:

```text
EKS control plane
NAT Gateway
EC2 worker nodes
Load Balancer
```

Infrastructure should be destroyed when not in use.

```bash
terraform destroy
```

## Deployment Flow

```text
Terraform
   |
   v
Create AWS VPC + IAM + EKS
   |
   v
Build Docker Image
   |
   v
Push Image to ECR
   |
   v
Deploy App to EKS
   |
   v
Expose Service via Load Balancer
```
