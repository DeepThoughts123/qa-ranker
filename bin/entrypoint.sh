#!/bin/bash

set -o pipefail -o errexit

#
# Default entrypoint for MLCLI-powered apps.
#
ISC_CONF=/conf/service_configurations.env

set -a
if [ -f "$ISC_CONF" ]; then
  source $ISC_CONF
fi
set +ax

exec qa_ranker_cli $@
