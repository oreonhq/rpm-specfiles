#!/bin/sh
#Wrapper script for lpsk31 to ensure that user configuration is present
xpsk31bin="/usr/bin/xpsk31.bin"
if  [ ! -f ~/xpsk31/xpsk31rc ]
then
echo "Creating user configuration in ~/xpsk31"
mkdir -p ~/xpsk31
install -m 0644 /usr/share/xpsk31/* ~/xpsk31/
$xpsk31bin $@
else 
$xpsk31bin $@
fi
