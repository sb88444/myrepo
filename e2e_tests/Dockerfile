FROM ubuntu:20.04

EXPOSE 443 22 27017 161/udp 9001 9002 9003 9005 9006 9007 80

RUN apt-get update -y && \
    apt-get install -y tcpdump net-tools vim iputils-ping curl

RUN apt-get install tzdata \
    && apt-get install software-properties-common -y \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get install -y python3.9 python3-pip python3.9-dev \
    && ln -s -f /usr/bin/python3.9 /usr/bin/python3 \
    && ln -s -f /usr/bin/python3.9  /usr/bin/python \
    && ln -s -f /usr/bin/pip3 /usr/bin/pip


RUN mkdir /tmp/locust
RUN mkdir /stms
RUN mkdir -p /stms/qa
RUN mkdir /stms/qa/spot_test_logs
COPY . /stms/qa
WORKDIR /stms/qa
RUN echo $(ls -1 /stms)


# # Copy the package requirements
COPY e2e_tests/requirements.txt /tmp/


# Install the package requirements
RUN pip3 install -U pip
RUN pip3 install -r /tmp/requirements.txt

ENV LOG_DIR_PATH /stms/qa/spot_test_logs
ENV PYTHONPATH /stms/qa/e2e_test

ENTRYPOINT ["/bin/bash","-c","./startup.sh"]


