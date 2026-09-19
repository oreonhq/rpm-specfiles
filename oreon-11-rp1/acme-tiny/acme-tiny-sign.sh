#!/bin/bash

if test "$(id -u)" -eq 0; then
  echo "Do not run as root!"
  exit 2
fi

. /etc/sysconfig/acme-tiny
DAYS="${1:-$DAYS}"
test -n "$DAYS" || DAYS="7"
if [[ "$DAYS" =~ ^[0-9]+$ ]]; then
  echo "Days before expiration: $DAYS"
  secs=$(( $DAYS * 24 * 60 * 60 ))
else
  echo "Invalid number of days: $DAYS"
  exit 1
fi

cd /var/lib/acme

if ! test -s private/account.key; then
  touch private/account.key
  chmod 0600 private/account.key
  openssl genrsa 4096 >private/account.key
fi

rc="0"
for csr in csr/*.csr; do
  test -s "$csr" || continue
  test -r "$csr" || continue
  crt="${csr%%.csr}"
  tmp="certs/${crt##csr/}.tmp"
  crt="certs/${crt##csr/}.crt"
  if test -s "$crt" && openssl x509 -in "$crt" -noout -checkend "$secs"; then
    continue
  fi
  if test -w "$crt" || test ! -e "$crt"; then
    echo acme_tiny --account-key private/account.key --csr "$csr" \
	--acme-dir /var/www/challenges/ --out "$crt"
  else
    echo "Can't write to $crt" 
    rc="1"
    continue
  fi

  if /usr/sbin/acme_tiny --account-key private/account.key --csr "$csr" \
	--acme-dir /var/www/challenges/ > "$tmp"; then
	mv "$tmp" "$crt" || exit 1
  else
	test -e "$tmp" && test ! -s "$tmp" && rm "$tmp"
  fi
  # append intermediate certs
  #cat *.pem >>"$crt"
done
exit "$rc"
