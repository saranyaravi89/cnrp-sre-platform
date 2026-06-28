resource "aws_eks_node_group" "cnrp_node_group" {
  cluster_name    = aws_eks_cluster.cnrp_cluster.name
  node_group_name = "cnrp-node-group"
  node_role_arn   = aws_iam_role.eks_node_role.arn

  subnet_ids = [
    aws_subnet.private_subnet_1.id
  ]

  scaling_config {
    desired_size = 2
    max_size     = 3
    min_size     = 1
  }

  instance_types = ["t3.medium"]

  depends_on = [
    aws_iam_role_policy_attachment.eks_worker_node_policy,
    aws_iam_role_policy_attachment.eks_cni_policy,
    aws_iam_role_policy_attachment.ec2_container_registry_readonly
  ]

  tags = {
    Name = "cnrp-node-group"
  }
}