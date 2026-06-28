resource "aws_subnet" "public_subnet_1" {
  vpc_id                  = aws_vpc.cnrp_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "ap-southeast-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "cnrp-public-subnet-1"
  }
}

resource "aws_subnet" "private_subnet_1" {
  vpc_id            = aws_vpc.cnrp_vpc.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "ap-southeast-1a"

  tags = {
    Name = "cnrp-private-subnet-1"
  }
}

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.cnrp_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.cnrp_igw.id
  }

  tags = {
    Name = "cnrp-public-rt"
  }
}

resource "aws_route_table_association" "public_assoc_1" {
  subnet_id      = aws_subnet.public_subnet_1.id
  route_table_id = aws_route_table.public_rt.id
}