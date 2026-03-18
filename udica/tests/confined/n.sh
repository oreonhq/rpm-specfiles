#!/bin/sh -x
on_err(){
  echo "Error"
}
 
trap 'on_err' ERR

ip address
ifconfig -s
traceroute 127.0.0.1
# this may block the test if there is no trafic !!!
sudo tcpdump -i any -c 1
netstat -g
nslookup www.google.com
ping -c 1 127.0.0.1
