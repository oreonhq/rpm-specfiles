#!/bin/sh -x
on_err(){
  echo "Error"
}
 
trap 'on_err' ERR

# gets stuck -- no journal entries
#sudo journalctl -n 1 --no-pager
sudo systemctl --no-pager status dbus
sudo netstat -g
sudo nslookup www.google.com
sudo sysctl net.ipv4.udp_mem
