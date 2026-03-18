#!/bin/sh -eux

function check_key_and_cert()
{
  echo -e "\n===== key info"
  ssh-keygen -l -f /etc/pki/Pegasus/file.pem || :
  file /etc/pki/Pegasus/file.pem
  echo -e "\n\n\n"

  echo -e "\n===== cert info"
  openssl x509 -in /etc/pki/Pegasus/ca.crt --text --noout
  echo -e "\n\n\n"
}

function test_key_exchange()
{
  echo -e "\n===== check that it uses TLS 1.3 and the X25519MLKEM768 key exchange by default if the peer supports it"
  openssl s_client -connect localhost:5989 -CAfile /etc/pki/Pegasus/client.pem </dev/null | tee key-exchange.out
  echo -e "\n\n\n"
  grep "Negotiated TLS1.3 group: X25519MLKEM768" key-exchange.out
  echo -e "\n\n\n"
}

function test_cert_support()
{
  echo -e "\n===== check that TLS certificate using ML-DSA works"
  openssl s_client -connect localhost:5989 -CAfile /etc/pki/Pegasus/client.pem </dev/null | tee cert-mldsa.out
  echo -e "\n\n\n"
  grep "Peer signature type: mldsa65" cert-mldsa.out
  echo -e "\n\n\n"
  # simulate lack of ML-DSA support
  echo "\n===== check support for a classic certificate chain if peer doesn't support ML-DSA certificate"
  openssl s_client -connect localhost:5989 -CAfile /etc/pki/Pegasus/client-fallback.pem -sigalgs 'rsa_pss_pss_sha256:rsa_pss_rsae_sha256' </dev/null | \
    tee cert-classic.out
  echo -e "\n\n\n"
  grep "Peer signature type: rsa_pss_rsae_sha256" cert-classic.out
  echo -e "\n\n\n"
}

systemctl start tog-pegasus
check_key_and_cert
test_key_exchange

systemctl stop tog-pegasus

# keep RSA certificate and key
cp /etc/pki/Pegasus/client.pem /etc/pki/Pegasus/client-fallback.pem
cp /etc/pki/Pegasus/server.pem /etc/pki/Pegasus/server-fallback.pem
cp /etc/pki/Pegasus/file.pem /etc/pki/Pegasus/file-fallback.pem
# remove other generated files
rm -rf /etc/Pegasus/ssl-* /etc/pki/Pegasus/ca* /etc/pki/Pegasus/{client,file,server}.pem
ls /etc/Pegasus /etc/pki/Pegasus

# update genOpenPegasusSSLCerts to generate a new key using ML-DSA-65
# and issue a self-signed certificate for localhost using this key
patch /usr/share/Pegasus/scripts/genOpenPegasusSSLCerts << 'EOF'
--- genOpenPegasusSSLCerts      2025-05-20 08:50:42.979482659 +0200
+++ genOpenPegasusSSLCerts.updated_2    2025-05-20 09:03:28.235354864 +0200
@@ -81,7 +81,7 @@
     # Create private key for the CA certificate
     TMPKEY=`mktemp --tmpdir=$PEGASUS_PEM_DIR XXXXXXXXXXXX`

-    /usr/bin/openssl genrsa -out $TMPKEY $KEYSIZE
+    /usr/bin/openssl genpkey -algorithm ML-DSA-65 -out $TMPKEY

     # Restore the umask for the other files
     umask $OLDUMASK
@@ -98,7 +98,7 @@
                          -out $PEGASUS_PEM_DIR/ca.crt \

     # Create private key for the service certificate
-    /usr/bin/openssl genrsa -out $PEGASUS_PEM_DIR/$PEGASUS_SSL_KEY_FILE $KEYSIZE
+    /usr/bin/openssl genpkey -algorithm ML-DSA-65 -out $PEGASUS_PEM_DIR/$PEGASUS_SSL_KEY_FILE

     # Create a signing request for the service certificate
     /usr/bin/openssl req -new \
EOF

systemctl start tog-pegasus
check_key_and_cert
test_cert_support
