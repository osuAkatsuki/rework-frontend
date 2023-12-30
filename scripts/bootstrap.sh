#!/usr/bin/env bash
set -eo pipefail

cd /srv/root

if [ -z "$APP_ENV" ]; then
  echo "Please set APP_ENV"
  exit 1
fi

if [ -z "$APP_COMPONENT" ]; then
  echo "Please set APP_COMPONENT"
  exit 1
fi

if [[ $PULL_SECRETS_FROM_VAULT -eq 1 ]]; then
  # TODO: revert to $APP_ENV
  akatsuki vault get rework-frontend production-k8s -o .env
  source .env
fi

# run the service
if [ $APP_COMPONENT == "api" ]; then
  exec /scripts/run-api.sh
else
  echo "Unknown APP_COMPONENT: $APP_COMPONENT"
  exit 1
fi
