#!/usr/bin/env bash
# Simple deploy script example (pulls latest image and restarts compose)
set -e
REMOTE_COMPOSE_PATH=${1:-/srv/swiftter}
IMAGE=${2:-ghcr.io/yourorg/swiftter:latest}

echo "Stopping and pulling new image..."
ssh -o StrictHostKeyChecking=no $SSH_DEPLOY_HOST "docker pull ${IMAGE} && cd ${REMOTE_COMPOSE_PATH} && docker-compose pull && docker-compose up -d --remove-orphans"
echo "Deploy triggered"
