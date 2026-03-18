#!/bin/bash -
set -e
set -x

# Compile trivial gettext program.
cat <<EOF > gettexttest.ml
module Gettext = Gettext.Program (
  struct
    let textdomain = "test"
    let codeset = None
    let dir = None
    let dependencies = []
  end
) (GettextStub.Native) ;;
open Gettext ;;
print_endline (s_ "Hello world")
EOF
ocamlfind ocamlopt -package gettext,gettext-stub gettexttest.ml -linkpkg -o gettexttest
./gettexttest
