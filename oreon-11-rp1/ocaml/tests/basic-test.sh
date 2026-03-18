#!/bin/bash -
set -e
set -x

# Compile a trivial program and run it.
echo 'print_endline "hello, world"' > hello.ml
ocamlc.opt hello.ml -o hello
./hello
ocamlopt.opt hello.ml -o hello
./hello
