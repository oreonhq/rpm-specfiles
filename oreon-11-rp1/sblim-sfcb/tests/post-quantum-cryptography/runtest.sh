#!/bin/sh -eux

function check_key_and_cert()
{
  echo -e "\n===== key info"
  ssh-keygen -l -f /etc/sfcb/file.pem || :
  file /etc/sfcb/file.pem
  echo -e "\n\n\n"

  echo -e "\n===== cert info"
  openssl x509 -in /etc/sfcb/server.pem --text --noout
  echo -e "\n\n\n"
}

function test_key_exchange()
{
  echo -e "\n===== check that it uses TLS 1.3 and the X25519MLKEM768 key exchange by default if the peer supports it"
  openssl s_client -connect localhost:5989 -CAfile /etc/sfcb/client.pem </dev/null | tee key-exchange.out
  echo -e "\n\n\n"
  grep "Negotiated TLS1.3 group: X25519MLKEM768" key-exchange.out
  echo -e "\n\n\n"
}

function test_cert_support()
{
  echo -e "\n===== check that TLS certificate using ML-DSA works"
  openssl s_client -connect localhost:5989 -CAfile /etc/sfcb/client.pem </dev/null | tee cert-mldsa.out
  echo -e "\n\n\n"
  grep "Peer signature type: mldsa65" cert-mldsa.out
  echo -e "\n\n\n"
  # simulate lack of ML-DSA support
  echo "\n===== check support for a classic certificate chain if peer doesn't support ML-DSA certificate"
  openssl s_client -connect localhost:5989 -CAfile /etc/sfcb/client-fallback.pem -sigalgs 'rsa_pss_pss_sha256:rsa_pss_rsae_sha256' </dev/null | \
    tee cert-classic.out
  echo -e "\n\n\n"
  grep "Peer signature type: rsa_pss_rsae_sha256" cert-classic.out
  echo -e "\n\n\n"
}

systemctl start sblim-sfcb
check_key_and_cert
test_key_exchange
systemctl stop sblim-sfcb

# keep RSA certificate and key
cp /etc/sfcb/server.pem /etc/sfcb/server-fallback.pem
cp /etc/sfcb/client.pem /etc/sfcb/client-fallback.pem
cp /etc/sfcb/file.pem /etc/sfcb/file-fallback.pem
# remove previously generated certificates/keys
rm -rf /etc/sfcb/{client,clist,file,server}.pem

# update genOpenPegasusSSLCerts to generate a new key using ML-DSA-65
# and issue a self-signed certificate for localhost using this key
patch /usr/share/sfcb/genSslCert.sh << 'EOF'
--- genSslCert.sh.orig	2025-05-21 09:29:57.615675163 +0200
+++ genSslCert.sh	2025-05-21 09:31:02.967076796 +0200
@@ -38,7 +38,7 @@
 emailAddress=root@$HOSTNAME
 EOF
 
-openssl req -x509 -days 365 -newkey rsa:2048 \
+openssl req -x509 -days 365 -newkey mldsa65 \
    -nodes -config $DIR/ssl.cnf   \
    -keyout $DIR/key.pem -out $DIR/cert.pem
 
EOF

/usr/share/sfcb/genSslCert.sh /etc/sfcb

# update config file
echo "sslKeyFallbackFilePath: /etc/sfcb/file-fallback.pem" >> /etc/sfcb/sfcb.cfg
echo "sslCertificateFallbackFilePath: /etc/sfcb/server-fallback.pem" >> /etc/sfcb/sfcb.cfg

systemctl start sblim-sfcb
check_key_and_cert
test_cert_support
