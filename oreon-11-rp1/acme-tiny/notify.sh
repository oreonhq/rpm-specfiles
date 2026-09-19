#!/usr/bin/sh

acmedir="/var/lib/acme"
#acmedir="test"
notify="${acmedir}/.notify"
verbose="n"
mkdir -p "$notify"

scancerts() {
  if test -e "${notify}/notify"; then
    find "${acmedir}/certs" -name '*.crt' -newer "${notify}/notify" -print0 
  else
    find "${acmedir}/certs" -name '*.crt' -print0
  fi | xargs -0 /usr/libexec/acme-tiny/notify -v 
  touch "${notify}/notify"
}

for cert in "$@"; do
  case "$cert" in
  -v|--verbose) verbose="y"; continue;;
  -s|--scan) scancerts; continue;;
  -*) echo "Invalid option $cert"; exit 2;;
  esac
  name="${cert##*/}"
  script="/etc/acme-tiny/notify.d/${name%.crt}.sh"

  # kick apache if cert is mentioned
  if test "$cert" -nt "${notify}/httpd"; then
    if grep "$cert" /etc/httpd/conf.d/*.conf >/dev/null 2>&1; then
      apachectl graceful && touch "${notify}/httpd" && \
        [ "$verbose" = "y" ] && echo "Httpd reloaded"
    fi
  fi

  # kick sendmail if cert is mentioned
  if test "$cert" -nt "${notify}/sendmail"; then
    if grep "/etc/pki/tls/certs/$name" /etc/mail/*.cf >/dev/null 2>&1; then
      cp "$cert" /etc/pki/tls/certs && systemctl restart sendmail \
	&& touch "${notify}/sendmail" && \
        [ "$verbose" = "y" ] && echo "Sendmail reloaded"
    fi
  fi

  # kick dovecot if cert is mentioned
  if test "$cert" -nt "${notify}/dovecot"; then
    if grep "/etc/pki/dovecot/certs/$name" /etc/dovecot/conf.d/10-ssl.conf >/dev/null 2>&1; then
      cp "$cert" /etc/pki/dovecot/certs && systemctl restart dovecot \
	&& touch "${notify}/dovecot" && \
        [ "$verbose" = "y" ] && echo "Dovecot reloaded"
    fi
  fi

  # run any dropin extension
  if test -x "$script"; then
    [ "$verbose" = "y" ] && echo "Running $script $cert"
    ACMEDIR="$acmedir" NOTIFY="$notify" VERBOSE="$verbose" "$script" "$cert"
  fi
done
