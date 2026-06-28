resource "aws_security_group" "eks_cluster_sg" {
  name        = "cnrp-eks-cluster-sg"
  description = "Security group for EKS cluster"
  vpc_id      = aws_vpc.cnrp_vpc.id

  ingress {
    description = "Allow HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "cnrp-eks-cluster-sg"
  }
}

resource "aws_security_group" "app_sg" {
  name        = "cnrp-app-sg"
  description = "Security group for application load balancer"
  vpc_id      = aws_vpc.cnrp_vpc.id

  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "cnrp-app-sg"
  }
}