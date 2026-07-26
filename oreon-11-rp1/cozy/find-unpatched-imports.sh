#!/bin/bash

grep \
	--line-number \
	--include '*.py' \
	--fixed-strings \
	-e 'from cozy.ext import inject' \
	-e 'import cozy.ext.inject' \
	-d recurse "$1"

# Quoting grep's man page:
# > Normally the exit status is 0 if a line is selected,
# > 1 if no lines were selected,
# > and 2 if an error occurred.
if [[ "$?" -ne 1 ]]; then
	exit 1
fi
