#!/bin/sh -ux

# remove previously generated SSL files
rm -rf /etc/openwsman/{servercert,serverkey}*.pem /etc/openwsman/ca.crt

# remove SSL fallback to relly really just on sscg
cp /etc/openwsman/owsmangencert.sh /etc/openwsman/test-script.sh
sed -i 's/^selfsign_sscg ||.*/selfsign_sscg/' /etc/openwsman/test-script.sh

# generate new SSL files using sscg
/etc/openwsman/test-script.sh

# check that SSL files were generated
[ -f /etc/openwsman/servercert.pem ] && [ -f /etc/openwsman/serverkey.pem ] || { echo "Error: SSL files missing"; exit 1; }

# try to start the service
systemctl start openwsmand
