# ocaml-dune

[Dune](https://dune.build) is a build system designed for
[OCaml](https://ocaml.org/)/[Reason](https://reasonml.github.io/) projects
only.  It focuses on providing the user with a consistent experience and takes
care of most of the low-level details of OCaml compilation.  All you have to
do is provide a description of your project and Dune will do the rest.

The scheme it implements is inspired from the one used inside
[Jane Street](https://opensource.janestreet.com/) and adapted to the open
source world.  It has matured over a long time and is used daily by hundred of
developers, which means that it is highly tested and productive.
