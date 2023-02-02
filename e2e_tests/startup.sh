
# print command before executing
set -o xtrace
SOURCE_DIR=$PWD

cd $SOURCE_DIR
pwd
ls
docker login -u sandeshb8 -p dckr_pat__3CqYNrraAqPWzTRRDxUUB9mZVQ docker.io
docker build -t e2e_test -f $SOURCE_DIR/e2e_tests/Dockerfile .
docker push e2e_test
docker run --rm --entrypoint=/bin/bash --name test -v $SOURCE_DIR/e2e_tests:/stms/qa --network host e2e_test:latest -c ls

#echo "Executing Pytest"
#docker run --rm --entrypoint pytest --name test -v $SOURCE_DIR:/stms/qa \
#           --network host e2e_test:latest /stms/qa/e2e_tests/sample

# DO NOT ADD CODE AFTER docker run COMMAND AS OUTPUT OF THIS COMMAND RETURNS EXIT CODE BASED ON WHICH JOB STATUS IS UPDATED.
