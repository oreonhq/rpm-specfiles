#!/bin/sh -x
on_err(){
  echo "Error"
}
 
trap 'on_err' ERR

id -Z
date
ls ~
ps
man -f selinux
systemctl --no-pager --user status dbus | grep "D-Bus User Message Bus"
journalctl -user
# cannot rotate the orgiginal password as user
#echo -e "$1\n9$1\n9$1" | passwd
#echo -e "9$1\n$1\n$1" | passwd
