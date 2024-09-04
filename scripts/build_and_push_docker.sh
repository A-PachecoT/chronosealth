#!/bin/bash
set -e

echo "Building Docker image..."
docker build -t myapp:latest .

echo "Logging in to Docker Hub..."
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

echo "Pushing Docker image..."
docker push myapp:latest