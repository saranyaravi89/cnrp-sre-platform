resource "aws_eks_cluster" "cnrp_cluster" {
  name     = "cnrp-cluster"
  role_arn = var.cluster_role_arn
  version  = "1.32"

  vpc_config {
    subnet_ids = var.subnet_ids

    security_group_ids = [var.cluster_sg_id]
  }


  tags = {
    Name = "cnrp-cluster"
  }
}