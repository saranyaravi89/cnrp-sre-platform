resource "aws_vpc" "cnrp_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name = "cnrp-vpc"
  }
}

resource "aws_internet_gateway" "cnrp_igw" {
  vpc_id = aws_vpc.cnrp_vpc.id

  tags = {
    Name = "cnrp-igw"
  }
}