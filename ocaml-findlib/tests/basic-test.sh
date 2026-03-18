#!/bin/bash -
set -e
set -x

# There's not really any reason to test this as chain builds
# use findlib extensively.  Just check the binary functions.
ocamlfind query findlib
