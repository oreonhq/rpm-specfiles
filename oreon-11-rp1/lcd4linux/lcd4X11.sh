#!/bin/sh

if [ ! -f $HOME/.lcd4X11.conf ]; then
    cp /etc/lcd4X11.conf $HOME/.lcd4X11.conf
    chmod 600 $HOME/.lcd4X11.conf
fi

exec lcd4linux -F -f $HOME/.lcd4X11.conf
