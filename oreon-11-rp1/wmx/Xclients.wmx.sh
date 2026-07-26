#!/bin/bash
# wmx startup script

if [ -f ${HOME}/.wmx/startup ]; then
  # fire up user's startup apps:
  . ${HOME}/.wmx/startup
else
  # fire default startup apps:
  . /usr/share/wmx/startup
fi

exec wmx
