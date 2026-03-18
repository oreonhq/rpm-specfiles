#!/bin/bash -
set -e
set -x

# Compile trivial curses program.
echo 'open Curses;; ignore (initscr ()); endwin ()' > cursestest.ml
ocamlfind ocamlopt -package curses cursestest.ml -linkpkg -o cursestest
# We can't run this because there is no controlling terminal in
# the test environment.
#./cursestest
