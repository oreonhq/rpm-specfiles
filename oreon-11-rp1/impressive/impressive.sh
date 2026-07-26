#!/bin/bash

. /usr/share/opengl-games-utils/opengl-game-functions.sh

APP=impressive

checkDriOK $APP

exec @PYTHON_SITELIB@/$APP.py "$@"
