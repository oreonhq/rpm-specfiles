#!/usr/bin/bash
# Prepare the host environment for running the snapm tests.
# This includes installing missing dependencies and tools.

set -euxo pipefail

# Move to the checked out git repo with the test plans
# this should be the root of the dist-git repo
cd "${TMT_TREE}"

sudo dnf builddep -y snapm.spec
