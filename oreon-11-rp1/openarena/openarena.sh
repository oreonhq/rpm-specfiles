#!/bin/bash

. /usr/share/opengl-games-utils/opengl-game-functions.sh

# we're a standalone game
CVARS="+set com_basegame baseoa"
CVARS="$CVARS +set com_homepath .openarena"
CVARS="$CVARS +set fs_basepath /usr/share/openarena"
# OA uses a different protocol number to reflect incompatible game content
CVARS="$CVARS +set com_protocol 71"
CVARS="$CVARS +set com_legacyprotocol 71"
# OA's default master server is different
CVARS="$CVARS +set sv_master1 dpmaster.deathmask.net"
# update.quake3arena.com is pretty irrelevant if you're playing OA
CVARS="$CVARS +set cl_motd 0"
# And last some openarena specific settings
CVARS="$CVARS +set com_hunkMegs 128"

if [[ "$0" =~ "ded" ]]; then
    CVARS="+set dedicated 1 $CVARS"
else
    checkDriOK openarena
fi

if [ ! -d ~/.openarena ]; then
  mkdir -p ~/.openarena
fi

rsync -a /usr/share/openarena/* ~/.openarena/

exec /usr/bin/quake3 $CVARS "$@"
