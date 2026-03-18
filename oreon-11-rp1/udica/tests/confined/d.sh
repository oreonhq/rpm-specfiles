#!/bin/sh -x
on_err(){
  echo "Error"
}
 
trap 'on_err' ERR

sesearch -A -s httpd_t -t http_port_t -c tcp_socket
sudo semanage user -l
sudo semanage fcontext -lC
sudo semodule -B
sudo sepolicy network -p 44322
