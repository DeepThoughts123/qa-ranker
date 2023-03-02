#!/bin/bash

set -o pipefail -o errexit

#
# Installing common linux dependencies
# TODO: Move it to base docker image

apt-get update
apt-get install -y \
    build-essential \
    wget \
    vim \
    htop \
    procps \
    curl \
    sysstat \
    libuv1-dev \
    zlib1g-dev \
    libssl-dev \
    cmake \
    unzip
