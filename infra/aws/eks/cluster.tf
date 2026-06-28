resource "aws_eks_cluster" "cnrp_cluster" {
  name     = "cnrp-cluster"
  role_arn = aws_iam_role.eks_cluster_role.arn
  version  = "1.29"

  vpc_config {
    subnet_ids = [
      aws_subnet.public_subnet_1.id,
      aws_subnet.private_subnet_1.id
    ]

    security_group_ids = [
      aws_security_group.eks_cluster_sg.id
    ]
  }

  depends_on = [
    aws_iam_role_policy_attachment.eks_cluster_policy
  ]

  tags = {
    Name = "cnrp-cluster"
  }
}