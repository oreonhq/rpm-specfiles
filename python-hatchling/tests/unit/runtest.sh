#!/bin/bash -eux

# Get the version of our installed component
VERSION=$(rpm -q --queryformat="%{VERSION}" python3-hatchling)

# The hatch's source code contains the tests for hatchling in tests/backend
git clone --depth 1 --branch hatchling-v$VERSION https://github.com/pypa/hatch/
cd hatch

# Delete the hatchling sources from the repository - we want to test the RPM package
rm -r backend/

# Work around tests wanting a proper Hatch installation
echo '__version__ = "(bogus)"' > src/hatch/_version.py

# test_extra_met and test_unknown_extra try to pip install requests[security]==2.25.1
# which is too old to be compiled for Python 3.13 - skip them
k="not test_extra_met and not test_unknown_extra"

PYTHONPATH="$PWD/src" python3 -m pytest tests/backend -k "${k}" -v
