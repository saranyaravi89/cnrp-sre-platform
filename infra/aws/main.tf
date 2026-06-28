module "vpc" {
  source = "./vpc"
}

module "iam" {
  source = "./iam"
}

module "eks" {
  source = "./eks"

  cluster_role_arn = module.iam.eks_cluster_role_arn
  node_role_arn    = module.iam.eks_node_role_arn
  subnet_ids       = module.vpc.subnet_ids
  cluster_sg_id    = module.vpc.eks_cluster_sg_id
}