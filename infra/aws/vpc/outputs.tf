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

output "vpc_id" {
  value = aws_vpc.cnrp_vpc.id
}

output "private_subnet_ids" {
  value = [
    aws_subnet.private_subnet_1.id,
    aws_subnet.private_subnet_2.id
  ]
}

output "app_sg_id" {
  value = aws_security_group.app_sg.id
}