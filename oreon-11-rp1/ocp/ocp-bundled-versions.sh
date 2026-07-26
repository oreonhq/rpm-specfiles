#!/bin/sh
# Try to find the versions of all the bundled source code projects by
# searching for Autoconf AC_INIT macros.

if [ x$1 = x ]; then
    tree="."
else
    tree="$1"
fi

if [ ! -e ${tree}/configure.ac ]; then
    echo "Missing ${tree}/configure.ac."
    echo "Usage: $0 [path-to-root-of-ocp-source-tree]"
    exit 1;
fi

grep -hEr 'AC_INIT\(|lib_major|lib_minor|lib_level' ${tree} | grep -Ev '#|='
