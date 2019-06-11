#!/bin/bash

BASE_COMPOSE='./docker/docker-compose.yml'
DEV_COMPOSE='./docker/docker-compose.dev.yml'
PROD_COMPOSE='./docker/docker-compose.prod.yml'

if [ $# -eq 0 ]; then
  echo 'Specify the environment you want to run!';
  return 1;
elif [ $# -eq 1 ]; then
  if [[ $1 -eq "dev" ]]; then
    docker-compose -f $BASE_COMPOSE -f $DEV_COMPOSE up
  elif [[ $1 -eq "prod" ]]; then
    docker-compose -f $BASE_COMPOSE -f $PROD_COMPOSE up
  fi
elif [ $# -eq 2 ]; then
    if [[ $1 -eq "dev" && $2 -eq "build" ]]; then
    docker-compose -f $BASE_COMPOSE -f $DEV_COMPOSE up --build
  elif [[ $1 -eq "prod" && $2 -eq "build" ]]; then
    docker-compose -f $BASE_COMPOSE -f $PROD_COMPOSE up --build
  fi
fi
