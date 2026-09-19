#!/bin/bash

set -e

. /usr/share/opengl-games-utils/opengl-game-functions.sh

checkDriOK "World of Padman"

# For wop < 1.5 lived in ~/.q3a/wop, with ~/.wop/wop being a symlink to it
# For wop 1.5 we directly use ~/.wop/wop
if [ -L $HOME/.wop/wop ]; then
	rm $HOME/.wop/wop
fi

# Clean up old wop if any, note we do this undepent of the symlink existing
# as even older autodownloader installs ran directly from ~/.q3a/wop
rm -fr $HOME/.q3a/wop

if [ ! -f $HOME/.wop/wop/wop_001.pk3 ]; then
	set +e
	/usr/share/autodl/AutoDL.py /usr/share/quake3/worldofpadman.autodlrc
	STATUS=$?
	set -e

	# status 2 means download was ok, but the user choice not to start the game
	if [ "$STATUS" = "0" -o "$STATUS" = "2" ]; then
		pushd $HOME/.wop > /dev/null
		unzip -qq -o -u wop-1.5-unified.zip
		rm -r *.dll wop*.* "XTRAS/editing files"
		popd > /dev/null
	fi
	if [ "$STATUS" != "0" ]; then
		exit $STATUS
	fi
fi

# We run from ~/.wop, using ~/.q3a is a bad idea as that will
# cause com_standalone to not get set if regular quake3 is also present
CVARS="+set com_basegame wop"
CVARS="$CVARS +set com_homepath .wop"
CVARS="$CVARS +set fs_basepath /usr/share/wop"
# World of Padman's default master server is different
CVARS="$CVARS +set sv_master1 master.worldofpadman.com:27955"
# WoP 1.5 has bumped the protocol version to allow using 1 master server
# for 1.2 and 1.5
CVARS="$CVARS +set com_protocol 69"
CVARS="$CVARS +set com_legacyprotocol 69"
# update.quake3arena.com is pretty irrelevant if you're playing wop
CVARS="$CVARS +set cl_motd 0"

exec quake3 $CVARS "$@"
