#!/bin/sh -eux

function check_key_and_cert()
{
  echo -e "\n===== key info"
  ssh-keygen -l -f /etc/openwsman/serverkey.pem || :
  file /etc/openwsman/serverkey.pem
  echo -e "\n\n\n"

  echo -e "\n===== cert info"
  openssl x509 -in /etc/openwsman/servercert.pem --text --noout
  echo -e "\n\n\n"
}

function test_key_exchange()
{
  echo -e "\n===== check that it uses TLS 1.3 and the X25519MLKEM768 key exchange by default if the peer supports it"
  openssl s_client  -connect localhost:5986 -CAfile /etc/openwsman/servercert.pem </dev/null | tee key-exchange.out
  echo -e "\n\n\n"
  grep "Negotiated TLS1.3 group: X25519MLKEM768" key-exchange.out
  echo -e "\n\n\n"
}

function test_cert_support()
{
  echo -e "\n===== check that TLS certificate using ML-DSA works"
  openssl s_client  -connect localhost:5986 -CAfile /etc/openwsman/servercert.pem </dev/null | tee cert-mldsa.out
  echo -e "\n\n\n"
  grep "Peer signature type: mldsa65" cert-mldsa.out
  echo -e "\n\n\n"
  # simulate lack of ML-DSA support
  echo "\n===== check support for a classic certificate chain if peer doesn't support ML-DSA certificate"
  openssl s_client  -connect localhost:5986 -CAfile /etc/openwsman/servercert-fallback.pem </dev/null -sigalgs 'rsa_pss_pss_sha256:rsa_pss_rsae_sha256' </dev/null | \
    tee cert-classic.out
  echo -e "\n\n\n"
  grep "Peer signature type: rsa_pss_rsae_sha256" cert-classic.out
  echo -e "\n\n\n"
}

(echo CZ; echo "Czech Republic"; echo Brno; echo "Red Hat"; echo "Core Services"; echo localhost; echo joe@example.com; ) | /etc/openwsman/owsmangencert.sh
systemctl start openwsmand
check_key_and_cert
test_key_exchange
systemctl stop openwsmand

# keep RSA certificate and key
cp /etc/openwsman/servercert.pem /etc/openwsman/servercert-fallback.pem
cp /etc/openwsman/serverkey.pem /etc/openwsman/serverkey-fallback.pem
# remove previously generated certificates/keys
rm -rf /etc/openwsman/{servercert,serverkey}.pem

# update genOpenPegasusSSLCerts to generate a new key using ML-DSA-65
# and issue a self-signed certificate for localhost using this key
patch /etc/openwsman/owsmangencert.sh << 'EOF'
--- owsmangencert.sh.orig	2026-01-08 03:50:31.852413993 -0500
+++ owsmangencert.sh	2026-01-08 03:52:41.883088457 -0500
@@ -65,7 +65,7 @@
     # certificate is created
 
     openssl req -days $DAYS $@ -config $CNFFILE \
-        -new -x509 -nodes -out $CERTFILE \
+        -newkey mldsa65 -x509 -nodes -out $CERTFILE \
         -keyout $KEYFILE
     chmod 600 $KEYFILE
 }
EOF

(echo CZ; echo "Czech Republic"; echo Brno; echo "Red Hat"; echo "Core Services"; echo localhost; echo joe@example.com; ) | /etc/openwsman/owsmangencert.sh

# update config file
patch /etc/openwsman/openwsman.conf << 'EOF'
--- openwsman.conf.orig	2025-06-05 07:50:30.285822838 -0400
+++ openwsman.conf	2025-06-05 07:50:38.609822838 -0400
@@ -33,11 +33,11 @@
 # the openwsman server certificate file, in .pem format
 ssl_cert_file = /etc/openwsman/servercert.pem
 # the openwsman server certificate fallback file, in .pem format
-#ssl_cert_fallback_file = /etc/openwsman/servercert-fallback.pem
+ssl_cert_fallback_file = /etc/openwsman/servercert-fallback.pem
 # the openwsman server private key, in .pem format
 ssl_key_file = /etc/openwsman/serverkey.pem
 # the openwsman server private key fallback, in .pem format
-#ssl_key_fallback_file = /etc/openwsman/serverkey-fallback.pem
+ssl_key_fallback_file = /etc/openwsman/serverkey-fallback.pem
 
 # space-separated list of SSL protocols to *dis*able
 # possible values: SSLv2 SSLv3 TLSv1 TLSv1_1 TLSv1_2
EOF

systemctl start openwsmand
check_key_and_cert
test_cert_support
