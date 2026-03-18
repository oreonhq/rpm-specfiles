#!/bin/bash -
set -e
set -x

# Run nbdkit and check that nbdinfo can connect back to it.
nbdkit -U - memory 1G --run 'nbdinfo "$uri"'
