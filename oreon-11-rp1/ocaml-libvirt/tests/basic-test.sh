#!/bin/bash -
set -e
set -x

# Compile trivial libvirt program.
echo 'print_endline Libvirt_version.version' > virttest.ml
ocamlfind ocamlopt -package libvirt virttest.ml -linkpkg -o virttest
./virttest
