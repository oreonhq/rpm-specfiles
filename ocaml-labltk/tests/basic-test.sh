#!/bin/bash -
set -e
set -x

# Compile trivial tk program.
echo 'ignore (Tk.opentk ())' > tktest.ml
ocamlfind ocamlopt -package labltk tktest.ml -linkpkg -o tktest
# Unfortunately we can't run this as we won't have an X server available.
#./tktest
