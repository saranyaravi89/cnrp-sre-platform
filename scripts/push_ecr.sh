#!/bin/bash
set -e

AWS_REGION="ap-southeast-1"
AWS_ACCOUNT_ID="985411011517"
ECR_REPO="cnrp-trading-api"
IMAGE_TAG="latest"

aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

docker build -t $ECR_REPO ./services/trading_api

docker tag $ECR_REPO:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG

docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG