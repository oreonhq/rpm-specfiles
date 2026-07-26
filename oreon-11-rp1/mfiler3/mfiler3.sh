#!/bin/bash

export PATH="/usr/libexec/mfiler3:$PATH"
exec /usr/libexec/mfiler3/mfiler3 $*
