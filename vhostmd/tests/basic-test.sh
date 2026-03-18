#!/bin/bash -
set -e
set -x

# Setting up vhostmd is basically impossible, so:
LANG=C vm-dump-metrics |& grep "Unable to read metrics disk"
