Building the MinGW Python environment
=====================================

Build order:

- mingw-python3

- mingw-python-setuptools

- mingw-python-wheel

- mingw-python-flit-core
- mingw-python-pep517 (bootstrap)
- mingw-python-pyparsing (bootstrap)
- mingw-python-packaging (bootstrap)
- mingw-python-installer (boostrap)
- mingw-python-pyproject-hooks (bootstrap)
- mingw-python-build

- mingw-python-pep517
- mingw-python-pyparsing
- mingw-python-packaging
- mingw-python-installer
- mingw-python-pyproject-hooks


A test to check whether the interpreter kinda works:

    python3.exe -Im ensurepip --upgrade --default-pip
