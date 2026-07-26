#!/bin/bash

set -e

. /usr/share/opengl-games-utils/opengl-game-functions.sh

checkDriOK "Urban Terror"

# urbanterror < 4.1.1 lived in ~/.q3a/q3ut4, with ~/.q3ut4/q3ut4 being a
# symlink to it. For urbanterror 4.1.1 we directly use ~/.q3ut4/q3ut4
if [ -L $HOME/.q3ut4/q3ut4 ]; then
	rm $HOME/.q3ut4/q3ut4
fi

# Clean up old urbanterror if any, note we do this undepent of the symlink
# existing as even older autodownloader installs ran directly from ~/.q3a/q3ut4
rm -fr $HOME/.q3a/q3ut4

if [ ! -f ~/.q3ut4/q3ut4/zUrT42_0001.pk3 ]; then
  set +e
  /usr/share/autodl/AutoDL.py /usr/share/quake3/urbanterror.autodlrc
  STATUS=$?
  set -e
  # status 2 means download was ok, but the user choice not to start the game
  if [ "$STATUS" = "0" -o "$STATUS" = "2" ]; then
    pushd ~/.q3ut4 > /dev/null
    unzip -qq -o -u UrbanTerror42_full023.zip
    # remove any old versions (if present) otherwise the mv fails
    rm -fr q3ut4
    mv UrbanTerror42/q3ut4 .
    rm -r UrbanTerror42 UrbanTerror42_full023.zip
    popd > /dev/null
  fi
  if [ "$STATUS" != "0" ]; then
    exit $STATUS
  fi
fi

# We run from ~/.q3ut4, using ~/.q3a is a bad idea as that will
# cause com_standalone to not get set if regular quake3 is also present
CVARS="+set com_basegame q3ut4"
CVARS="$CVARS +set com_homepath .q3ut4"
CVARS="$CVARS +set fs_basepath /usr/share/q3ut4"
# Urban Terror's default master server is different
CVARS="$CVARS +set sv_master1 master.urbanterror.info:27900"
# update.quake3arena.com is pretty irrelevant if you're playing ut
CVARS="$CVARS +set cl_motd 0"
# ut qvm files use unaligned stores and loads
CVARS="$CVARS +set qvm_unaligned 1"
# And last some Urban Terror specific settings
CVARS="$CVARS +set com_hunkMegs 512 +set cl_allowdownload 1"

exec quake3 $CVARS "$@"
