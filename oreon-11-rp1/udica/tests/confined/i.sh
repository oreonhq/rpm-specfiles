#!/bin/sh -x
on_err(){
  echo "Error"
}
 
trap 'on_err' ERR


seinfo
getsebool httpd_can_connect_ftp
sesearch -A -s httpd_t -t http_port_t -c tcp_socket
