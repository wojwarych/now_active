#!/usr/bin/env bash

PROG_OPTS='bCdptXx'


BASE_COMPOSE='./docker/docker-compose.yml'
DEV_COMPOSE='./docker/docker-compose.dev.yml'
PROD_COMPOSE='./docker/docker-compose.prod.yml'
PREPARE_DB='./docker/docker-compose.prepare.yml'
RUN_DEV=0
RUN_PROD=0
BUILD_SERVICE=""
TESTS=0
KILL_CONTAINERS=0
CREATE_DB=0


while getopts ${PROG_OPTS} c
do
  case ${c} in
    b) BUILD_SERVICE="--build" ;;
    C) CREATE_DB=2 ;;
    d) RUN_DEV=1 ;;
    p) RUN_PROD=1 ;;
    t) TESTS=1 ;;
    x) KILL_CONTAINERS=1 ;;
    X) KILL_CONTAINERS=2 ;;
  esac
done


function run-tests {
  if [ ${TESTS} -eq "1" ] ; then
    docker-compose -f $DEV_COMPOSE run --rm backend pytest
  fi
}


function run-image {
  if [ ${RUN_DEV} -eq "1" ] ; then
    if [ ${CREATE_DB} -eq "2" ] ; then
      docker-compose -f ${BASE_COMPOSE} -f ${DEV_COMPOSE} -f ${PREPARE_DB} up
    else
      docker-compose -f ${BASE_COMPOSE} -f ${DEV_COMPOSE} up
    fi
  elif [ ${RUN_PROD} -eq "1" ] ; then
    docker-compose -f ${BASE_COMPOSE} -f ${PROD_COMPOSE} up ${BUILD_SERVICE}
  fi
}

function kill-containers {
  if [ ${KILL_CONTAINERS} -eq "1" ] ; then
    docker-compose -f ${BASE_COMPOSE} -f ${DEV_COMPOSE} stop
  elif [ ${KILL_CONTAINERS} -eq "2" ] ; then
    docker-compose -f ${BASE_COMPOSE} -f ${DEV_COMPOSE} down --remove-orphans
  fi
}

run-image
run-tests
kill-containers
