%global source0_hash de894f6219ec90831e96f1f612ccc7a007060288c4427c393281f61d92c77617
%define VERSION %{version}
%define bind_name bind
%define bind_version 32:9.18.50
%if 0%{?fedora} >= 31 || 0%{?rhel} > 8 || 0%{?oreon} >= 11
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
    %global openssl_pkcs11_version 1.0
    %global openssl_pkcs11_name pkcs11-provider
    %global softhsm_version 2.6.1
%else
    %global openssl_pkcs11_version 0.4.10-6
    %global openssl_pkcs11_name openssl-pkcs11
    %global softhsm_version 2.5.0-4
%endif
%else
    %global with_bind_pkcs11 1
%endif
Name:           bind-dyndb-ldap
Version:        12.0
Release:        1%{?dist}
Summary:        LDAP back-end plug-in for BIND
License:        GPL-2.0-or-later
URL:            https://releases.pagure.org/bind-dyndb-ldap
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.bz2
Conflicts: bind9-next
%if %{with bind_pkcs11}
Requires(pre): bind-pkcs11 >= %{bind_version}
Requires: bind-pkcs11 >= %{bind_version}
Requires: bind-pkcs11-utils >= %{bind_version}
%else
Requires: softhsm >= %{softhsm_version}
Requires: %{openssl_pkcs11_name} >= %{openssl_pkcs11_version}
Requires(pre): %{bind_name} >= %{bind_version}
Requires: %{bind_name} >= %{bind_version}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bind-devel
BuildRequires:  bind-lite-devel
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  openldap-devel
# /oreon:deps
%description
This package provides an LDAP back-end plug-in for BIND. It features
support for dynamic updates and internal caching, to lift the load
off of your LDAP server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n bind-dyndb-ldap-%{VERSION} -p1

%build

autoreconf -fiv
export BIND9_CFLAGS='-I /usr/include/bind9 -DHAVE_TLS -DHAVE_THREAD_LOCAL'
%configure
%make_build
%install
%make_install
mkdir -m 770 -p %{buildroot}/%{_localstatedir}/named/dyndb-ldap
rm %{buildroot}%{_libdir}/bind/ldap.la
rm -r %{buildroot}%{_datadir}/doc/%{name}
%oreon_autofiles main

%post

[ -f /etc/named.conf ] || exit 0
PLATFORM=$(uname -m)
if [ $PLATFORM == "x86_64" ] ; then
    LIBPATH=/usr/lib64
else
    LIBPATH=/usr/lib
fi
while read -r PATTERN
do
    SEDSCRIPT+="$PATTERN"
done <<EOF
/^\s*dynamic-db/,/};/ {
  s/\(\s*\)arg\s\+\(["']\)\([a-zA-Z_]\+\s\)/\1\3\2/g;
  s/^dynamic-db/dyndb/;
  s@\(dyndb "[^"]\+"\)@\1 "$LIBPATH/bind/ldap.so"@;
  s@\(dyndb '[^']\+'\)@\1 '$LIBPATH/bind/ldap.so'@;
  /\s*library[^;]\+;/d;
  /\s*cache_ttl[^;]\+;/d;
  /\s*psearch[^;]\+;/d;
  /\s*serial_autoincrement[^;]\+;/d;
  /\s*zone_refresh[^;]\+;/d;
}
EOF
sed -i.bak -e "$SEDSCRIPT" /etc/named.conf
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 11.11-12
- Prepare for Oreon 11 (RP1)
