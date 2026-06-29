resource "aws_ecr_repository" "trading_api" {
  name                 = "cnrp-trading-api"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Name = "cnrp-trading-api"
  }
}