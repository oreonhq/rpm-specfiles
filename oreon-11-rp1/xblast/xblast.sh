#!/bin/bash

XBLAST=`which xblast-sdl 2> /dev/null`

if [ -z "$XBLAST" ]; then
    XBLAST=`which xblast-x11 2> /dev/null`
fi

if [ -z "$XBLAST" ]; then
    echo "error could find neither xblast-sdl nor xblast-x11"
    exit 1
fi

exec $XBLAST "$@"
