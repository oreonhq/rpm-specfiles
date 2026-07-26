#!/bin/bash

set -e

if [ -f /usr/share/rott/DARKWAR.WAD ]; then
       cd /usr/share/rott
       exec rott-registered.bin "$@"
fi

if [ ! -f ~/.rott/registered/*.WAD -a ! -f ~/.rott/registered/*.wad ]; then
	zenity --info --text='In order to play the registered version of Rise of the Triad (ROTT), An Apogee Game, the original registered ROTT datafiles are needed.

If you posess the registered version, copy all the datafiles of this version to [home folder]/.rott/registered and start ROTT Registered again.'
	exit 1
fi

cd ~/.rott/registered
exec rott-registered.bin "$@"
