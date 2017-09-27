#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A intranet_sm.taskapp beat -l INFO
