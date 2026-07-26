#!/bin/bash

if [ `glxinfo | grep "direct rendering: " | head -n 1 | cut -d " " -f 3` != Yes ]; then
  exec nogravity-software "$@"
else
  exec nogravity-opengl "$@"
fi
