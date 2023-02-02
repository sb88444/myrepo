#!/bin/bash

# print command before executing
set -o xtrace
SOURCE_DIR=$PWD

docker build -t e2e_test -f BE-Dockerfile .

echo "Executing Pytest"
docker run --rm --entrypoint pytest --name test -v $SOURCE_DIR:/stms/qa \
           --network host e2e_test:latest /stms/qa/

# DO NOT ADD CODE AFTER docker run COMMAND AS OUTPUT OF THIS COMMAND RETURNS EXIT CODE BASED ON WHICH JOB STATUS IS UPDATED.