#!/bin/bash

# print command before executing
set -o xtrace
SOURCE_DIR=$PWD

echo "Executing Pytest"
docker run --rm --entrypoint pytest --name ${username} -v $SOURCE_DIR:/stms/qa \
           --network host e2e_pytest:latest /stms/qa/

# DO NOT ADD CODE AFTER docker run COMMAND AS OUTPUT OF THIS COMMAND RETURNS EXIT CODE BASED ON WHICH JOB STATUS IS UPDATED.
