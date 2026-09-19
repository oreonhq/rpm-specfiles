#!/bin/sh

# Wrapper script for starting The Ur-Quan Masters

# base settings
myShareDir=/usr/share/uqm
myHomeDir=~/.uqm

. $myShareDir/uqm-functions.sh

echo ""
echo "starting uqm ..."

# creates a local working directory in user-home
createLocalDir

# Source system wide settings
if [ -e /etc/uqm.conf ] ; then
  . /etc/uqm.conf
fi

# Source per-user settings
if [ -e "$HOME/.uqm/uqm.conf" ] ; then
  . "$HOME/.uqm/uqm.conf"
fi

exec /usr/games/uqm $UQM_OPTS "$@"
