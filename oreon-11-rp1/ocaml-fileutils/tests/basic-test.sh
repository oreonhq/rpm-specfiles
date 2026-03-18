#!/bin/bash -
set -e
set -x

# Compile trivial fileutils program.
echo 'assert (FilePath.compare "/" "/" = 0)' > filetest.ml
ocamlfind ocamlopt -package fileutils filetest.ml -linkpkg -o filetest
./filetest
