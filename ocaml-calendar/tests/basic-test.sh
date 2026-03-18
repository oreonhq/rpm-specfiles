#!/bin/bash -
set -e
set -x

# Compile trivial calendar program.
echo 'CalendarLib.Calendar.Period.make 0 0 0 1 0 0' > caltest.ml
ocamlfind ocamlopt -package calendar caltest.ml -linkpkg -o caltest
./caltest
