#!/bin/bash

set -e

# game assets installed with game-data-packager
if [ -f /usr/share/rott/REMOTE1.RTS ]; then
  cd /usr/share/rott
  exec /usr/bin/rott-shareware.bin "$@"
fi

mkdir -p $HOME/.rott
cd $HOME/.rott

if [ ! -f REMOTE1.RTS ]; then
  set +e
  /usr/share/autodl/AutoDL.py /usr/share/rott/rott.autodlrc
  STATUS=$?
  set -e
  # status 2 means download was ok, but the user choice not to start the game
  if [ "$STATUS" = "0" -o  "$STATUS" = "2" ]; then
    unzip -u 1rott13.zip ROTTSW13.SHR
    unzip -u ROTTSW13.SHR VENDOR.DOC 'HUNTBGIN.*' REMOTE1.RTS 'DEMO*.DMO'
    rm 1rott13.zip ROTTSW13.SHR
  fi
  if [ "$STATUS" != "0" ]; then
    exit $STATUS
  fi
fi

exec /usr/bin/rott-shareware.bin "$@"
