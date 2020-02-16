#!/usr/bin/bash

PROG_OPTS="dp"

RUN_DEV=0
RUN_PROD=0

while getopts ${PROG_OPTS} c
do
  case ${c} in
    d) RUN_DEV=1 ;;
    p) RUN_PROD=1 ;;
  esac
done


function run-server {
  if [[ $RUN_DEV -eq "1" ]] ; then
    python manage.py runserver 0.0.0.0:8000
  elif [[ $RUN_PROD -eq "1" ]] ; then
    python manage.py runserver 0.0.0.0:8000
  fi
}


run-server
