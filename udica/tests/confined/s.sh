#!/bin/sh -x
on_err(){
  echo "Error"
}
 
trap 'on_err' ERR

sudo id -Z
sudo passwd -S root
