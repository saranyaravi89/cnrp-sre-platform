output "subnet_ids" {
  value = [
    aws_subnet.public_subnet_1.id,
    aws_subnet.private_subnet_1.id,
    aws_subnet.public_subnet_2.id,
    aws_subnet.private_subnet_2.id
  ]
}

output "eks_cluster_sg_id" {
  value = aws_security_group.eks_cluster_sg.id
}