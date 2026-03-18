#!/bin/bash

set -xe
set -o pipefail

/usr/share/booth/tests/test/runtests.py --allow-root-user
