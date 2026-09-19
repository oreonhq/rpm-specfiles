#!/bin/bash

set -e

# First check if a system-wide doom1.wad is installed and if it is
# use that instead of downloading
if [ -f /usr/share/games/doom/doom1.wad ]; then
  exec /usr/bin/vavoom -iwaddir /usr/share/games/doom -doom "$@"
elif [ -f /usr/share/doom/doom1.wad ]; then
  exec /usr/bin/vavoom -iwaddir /usr/share/doom -doom "$@"
fi

if [ ! -f ~/.vavoom/doom-shareware/doom1.wad ]; then
  set +e
  /usr/share/autodl/AutoDL.py /usr/share/vavoom/doom.autodlrc
  STATUS=$?
  set -e
  # status 2 means download was ok, but the user choice not to start the game
  if [ "$STATUS" = "0" -o  "$STATUS" = "2" ]; then
    cd ~/.vavoom/doom-shareware
    unzip -u doom19s.zip 'DOOMS_19.?'
    cat DOOMS_19.1 DOOMS_19.2 > doom.zip
    unzip -u -L doom.zip doom1.wad
    rm doom19s.zip DOOMS_19.1 DOOMS_19.2 doom.zip
  fi
  if [ "$STATUS" != "0" ]; then
    exit $STATUS
  fi
fi

exec /usr/bin/vavoom -iwaddir ~/.vavoom/doom-shareware -doom "$@"
