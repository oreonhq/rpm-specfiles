#!/usr/bin/env ksh
# from bugzilla https://bugzilla.redhat.com/show_bug.cgi?id=890961

echo "Before processing a subshell"

NUMFILES=$(ls | wc -l)

echo "After processing a subshell"
