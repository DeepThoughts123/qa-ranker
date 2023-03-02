#!/bin/bash

set -o pipefail -o errexit

#
# Basic entrypoint that just executes whatever you tell it to.
#
ISC_CONF=/conf/service_configurations.env

set -a
if [ -f "$ISC_CONF" ]; then
  source $ISC_CONF
fi
set +ax

exec $@
