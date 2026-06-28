resource "aws_eks_node_group" "cnrp_node_group" {
  cluster_name    = aws_eks_cluster.cnrp_cluster.name
  node_group_name = "cnrp-node-group"
  node_role_arn   = var.node_role_arn

  subnet_ids = var.subnet_ids

  scaling_config {
    desired_size = 2
    max_size     = 3
    min_size     = 1
  }

  instance_types = ["t3.medium"]

  tags = {
    Name = "cnrp-node-group"
  }
}