#!/bin/bash

LIBEXECDIR=/usr/libexec
DATADIR=/usr/share/ochusha

if [ -z $HOME ]
then
	echo "The environment \$HOME is not defined."
	exit 1
fi
if [ ! -d $HOME/.ochusha ]
then
	mkdir $HOME/.ochusha || exit 1
fi
if [ ! -f $HOME/.ochusha/ochusha-prefs-gtkrc ]
then
	install -c -p -m 0600 $DATADIR/ochusha-prefs-gtkrc $HOME/.ochusha/
fi

exec $LIBEXECDIR/ochusha $@
