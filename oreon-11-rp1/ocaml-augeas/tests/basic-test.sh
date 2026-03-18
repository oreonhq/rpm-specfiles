#!/bin/bash -
set -e
set -x

# Compile trivial augeas program.
echo 'Augeas.create "/" None [AugNoLoad]' > augtest.ml
ocamlfind ocamlopt -package augeas augtest.ml -linkpkg -o augtest
./augtest
