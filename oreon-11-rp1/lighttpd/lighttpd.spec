%global source0_hash 18de51b393bac4a6827879e1a7ff377c169e414bae92cd245091d80fc2601d13
%global source11_hash c14443059f7f4f6a1999e9147d7ce3f15058768dd16679ec248d4562ce4d51dc
%global source12_hash 2080e74437fe44333974c5268bccbfec96abaf19266cbbc96e896652d7a38183
%global source13_hash 6cbac241e026381d710f9110d209ef6198f448ddb241b95556d4f700a2e177d1
%define webroot /var/www/lighttpd
%define confswitch() %{expand:%%{?with_%{1}:--with-%{1}}%%{!?with_%{1}:--without-%{1}}}
%bcond_without attr
%bcond_with    pcre
%bcond_without pcre2
%bcond_without nettle
%bcond_with    unwind
%bcond_without lua
%bcond_without brotli
%bcond_with    bzip2
%bcond_without zlib
%bcond_without zstd
%bcond_without maxminddb
%bcond_without dbi
%bcond_without ldap
%bcond_without mysql
%bcond_without pgsql
%bcond_without krb5
%bcond_without pam
%bcond_without sasl
%bcond_without gnutls
%bcond_without mbedtls
%bcond_without nss
%bcond_without openssl
%bcond_without webdavprops
%bcond_without webdavlocks
%bcond_with    tmpfiles
Summary:        Lightning fast webserver with light system requirements
Name: lighttpd
Version: 1.4.85
Release:        1%{?dist}
License: BSD-3-Clause
URL: http://www.lighttpd.net/
Source0:        http://download.lighttpd.net/lighttpd/releases-1.4.x/lighttpd-%{version}.tar.xz
Source1: lighttpd.logrotate
Source2: php.d-lighttpd.ini
Source10: index.html
Source11: http://www.lighttpd.net/favicon.ico
Source12: http://www.lighttpd.net/light_button.png
Source13: http://www.lighttpd.net/light_logo.png
Source14: lighttpd-empty.png
Patch0: lighttpd-1.4.79-defaultconf.patch
Requires: system-logos
Requires: %{name}-filesystem
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires(post): %{name}-mod_deflate
Requires(post): %{name}-mod_webdav
%{?with_lua:Requires(post): %{name}-mod_magnet}
%{?with_openssl:Requires(post): %{name}-mod_openssl}
Provides: webserver
%{?with_pcre:BuildRequires: pcre-devel}
%{?with_pcre2:BuildRequires: pcre2-devel}
%{?with_nettle:BuildRequires: nettle-devel}
%{?with_unwind:BuildRequires: libunwind-devel}
# oreon:deps
BuildRequires:  /usr/bin/awk
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  brotli-devel
BuildRequires:  bzip2-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gnutls-devel
BuildRequires:  krb5-devel
BuildRequires:  libdbi-devel
BuildRequires:  libmaxminddb-devel
BuildRequires:  libpq-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzstd-devel
BuildRequires:  lua-devel
BuildRequires:  m4
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  mbedtls-devel
BuildRequires:  nettle-devel
BuildRequires:  nss-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkg-config
BuildRequires:  sqlite-devel
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
%description
lighttpd (pronounced /lighty/) is a secure, fast, compliant, and very flexible
web server that has been optimized for high-performance environments. lighttpd
uses memory and CPU efficiently and has lower resource use than other popular
web servers. Its advanced feature-set (FastCGI, CGI, Auth, Output-Compression,
URL-Rewriting and much more) make lighttpd the perfect web server for all
systems, small and large.

%package fastcgi
Summary: FastCGI module and spawning helper for lighttpd and PHP configuration
Requires: %{name} = %{version}-%{release}
%description fastcgi
This package contains the spawn-fcgi helper for lighttpd's automatic spawning
of local FastCGI programs. Included is also a PHP .ini file to change a few
defaults needed for correct FastCGI behavior.

%if %{with dbi}
%package mod_authn_dbi
Summary: Authentication module for lighttpd that uses DBI
Requires: %{name} = %{version}-%{release}
%{?with_dbi:BuildRequires: libdbi-devel}
%{?with_dbi:Suggests: libdbi-dbd-mysql}
%{?with_dbi:Suggests: libdbi-dbd-pgsql}
%{?with_dbi:Suggests: libdbi-dbd-sqlite}
%description mod_authn_dbi
Authentication module for lighttpd that uses DBI
%endif

%if %{with krb5}
%package mod_authn_gssapi
Summary: Authentication module for lighttpd that uses GSSAPI
Requires: %{name} = %{version}-%{release}
%{?with_krb5:BuildRequires: krb5-devel}
%description mod_authn_gssapi
Authentication module for lighttpd that uses GSSAPI
%endif

%if %{with ldap}
%package mod_authn_ldap
Summary: Authentication module for lighttpd that uses LDAP
Requires: %{name} = %{version}-%{release}
%{?with_ldap:BuildRequires: openldap-devel}
%description mod_authn_ldap
Authentication module for lighttpd that uses LDAP
%endif

%if %{with pam}
%package mod_authn_pam
Summary: Authentication module for lighttpd that uses PAM
Requires: %{name} = %{version}-%{release}
%{?with_pam:BuildRequires: pam-devel}
%description mod_authn_pam
Authentication module for lighttpd that uses PAM.
%endif

%if %{with sasl}
%package mod_authn_sasl
Summary: Authentication module for lighttpd that uses SASL
Requires: %{name} = %{version}-%{release}
%{?with_sasl:BuildRequires: cyrus-sasl-devel}
%description mod_authn_sasl
Authentication module for lighttpd that uses SASL.
%endif

%package mod_deflate
Summary: Compression module for lighttpd
Requires: %{name} = %{version}-%{release}
%{?with_zlib:BuildRequires: zlib-devel}
%{?with_zstd:BuildRequires: libzstd-devel}
%{?with_bzip2:BuildRequires: bzip2-devel}
%{?with_brotli:BuildRequires: brotli-devel}
%description mod_deflate
Compression module for lighttpd.

%if %{with gnutls}
%package mod_gnutls
Summary: TLS module for lighttpd that uses GnuTLS
Requires: %{name} = %{version}-%{release}
%{?with_gnutls:BuildRequires: gnutls-devel}
%description mod_gnutls
TLS module for lighttpd that uses GnuTLS.
%endif

%if %{with lua}
%package mod_magnet
Summary: Lua module for lighttpd
Requires: %{name} = %{version}-%{release}
%{?with_lua:BuildRequires: lua-devel}
%description mod_magnet
Lua module for lighttpd.
%endif

%if %{with maxminddb}
%package mod_maxminddb
Summary: GeoIP2 module for lighttpd to use for location lookups
Requires: %{name} = %{version}-%{release}
%{?with_maxminddb:BuildRequires: libmaxminddb-devel}
%{?with_maxminddb:Recommends: GeoIP-GeoLite-data}
%{?with_maxminddb:Recommends: GeoIP-GeoLite-data-extra}
%{?with_maxminddb:Suggests: geoipupdate}
%{?with_maxminddb:Suggests: geoipupdate-cron}
%description mod_maxminddb
GeoIP2 module for lighttpd to use for location lookups.
%endif

%if %{with mbedtls}
%package mod_mbedtls
Summary: TLS module for lighttpd that uses mbedTLS
Requires: %{name} = %{version}-%{release}
%{?with_mbedtls:BuildRequires: mbedtls-devel}
%description mod_mbedtls
TLS module for lighttpd that uses mbedTLS.
%endif

%if %{with nss}
%package mod_nss
Summary: TLS module for lighttpd that uses NSS
Requires: %{name} = %{version}-%{release}
%{?with_nss:BuildRequires: nss-devel}
%description mod_nss
TLS module for lighttpd that uses NSS.
%endif

%if %{with openssl}
%package mod_openssl
Summary: TLS module for lighttpd that uses OpenSSL
Requires: %{name} = %{version}-%{release}
%{?with_openssl:BuildRequires: openssl-devel}
%description mod_openssl
TLS module for lighttpd that uses OpenSSL.
%endif

%if %{with dbi}
%package mod_vhostdb_dbi
Summary: Virtual host module for lighttpd that uses DBI
Requires: %{name} = %{version}-%{release}
%{?with_dbi:BuildRequires: libdbi-devel}
%{?with_dbi:Suggests: libdbi-dbd-mysql}
%{?with_dbi:Suggests: libdbi-dbd-pgsql}
%{?with_dbi:Suggests: libdbi-dbd-sqlite}
%description mod_vhostdb_dbi
Virtual host module for lighttpd that uses DBI.
%endif

%if %{with ldap}
%package mod_vhostdb_ldap
Summary: Virtual host module for lighttpd that uses LDAP
Requires: %{name} = %{version}-%{release}
%{?with_ldap:BuildRequires: openldap-devel}
%description mod_vhostdb_ldap
Virtual host module for lighttpd that uses LDAP.
%endif

%if %{with mysql}
%package mod_vhostdb_mysql
Summary: Virtual host module for lighttpd that uses MySQL
Requires: %{name} = %{version}-%{release}
%{?with_mysql:BuildRequires: mariadb-connector-c-devel}
%description mod_vhostdb_mysql
Virtual host module for lighttpd that uses MySQL.
%endif

%if %{with pgsql}
%package mod_vhostdb_pgsql
Summary: Virtual host module for lighttpd that uses PostgreSQL
Requires: %{name} = %{version}-%{release}
%{?with_pgsql:BuildRequires: libpq-devel}
%description mod_vhostdb_pgsql
Virtual host module for lighttpd that uses PostgreSQL.
%endif

%package mod_webdav
Summary: WebDAV module for lighttpd
Requires: %{name} = %{version}-%{release}
%{?with_webdavprops:BuildRequires: libxml2-devel}
%{?with_webdavprops:BuildRequires: sqlite-devel}
%{?with_webdavlocks:BuildRequires: libxml2-devel}
%{?with_webdavlocks:BuildRequires: sqlite-devel}
%description mod_webdav
WebDAV module for lighttpd.

%package filesystem
Summary: The basic directory layout for lighttpd
BuildArch: noarch
%description filesystem
The lighttpd-filesystem package contains the basic directory layout
for the lighttpd server including the correct permissions
for the directories.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source11_hash}" = "none" || { f="%{SOURCE11}"; test -f "$f" || { echo "oreon: missing Source11 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source11_hash}" || { echo "oreon: Source11 hash mismatch" >&2; exit 1; }; }
test "%{source12_hash}" = "none" || { f="%{SOURCE12}"; test -f "$f" || { echo "oreon: missing Source12 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source12_hash}" || { echo "oreon: Source12 hash mismatch" >&2; exit 1; }; }
test "%{source13_hash}" = "none" || { f="%{SOURCE13}"; test -f "$f" || { echo "oreon: missing Source13 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source13_hash}" || { echo "oreon: Source13 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P 0 -p0 -b .defaultconf

# Create a sysusers.d config file
cat >lighttpd.sysusers.conf <<EOF
u lighttpd - 'lighttpd web server' %{webroot} -
EOF

%build

autoreconf -if
%configure \
    --libdir='%{_libdir}/lighttpd' \
    %{confswitch pcre} \
    %{confswitch pcre2} \
    %{confswitch nettle} \
    %{confswitch attr} \
    %{confswitch mysql} \
    %{confswitch pgsql} \
    %{confswitch dbi} \
    %{confswitch krb5} \
    %{confswitch ldap} \
    %{confswitch pam} \
    %{confswitch sasl} \
    %{confswitch gnutls} \
    %{confswitch mbedtls} \
    %{confswitch nss} \
    %{confswitch openssl} \
    %{?with_webdavprops:--with-webdav-props} \
    %{?with_webdavlocks:--with-webdav-locks} \
    %{?with_lua:--with-lua=lua} \
    %{confswitch zlib} \
    %{confswitch zstd} \
    %{confswitch bzip2} \
    %{confswitch brotli} \
    %{confswitch maxminddb} \
    %{confswitch unwind}
%make_build
%install
%make_install
install -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/logrotate.d/lighttpd
install -D -p -m 0644 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/php.d/lighttpd.ini
install -D -p -m 0644 doc/systemd/lighttpd.service \
    %{buildroot}%{_unitdir}/lighttpd.service
mkdir -p %{buildroot}%{webroot}
install -p -m 0644 %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} \
    %{buildroot}%{webroot}/
%if %{with systemlogos}
ln -s %{_datadir}/pixmaps/poweredby.png \
%else
install -p -m 0644 %{SOURCE14} \
%endif
    %{buildroot}%{webroot}/poweredby.png
rm -rf config
cp -a doc/config config
find config -name 'Makefile*' | xargs rm -f
chmod -x doc/scripts/*.sh
mkdir -p %{buildroot}%{_sysconfdir}/lighttpd
cp -a config/*.conf config/*.d %{buildroot}%{_sysconfdir}/lighttpd/
mkdir -p %{buildroot}/usr/lib/modules-load.d
echo tls > %{buildroot}/usr/lib/modules-load.d/lighttpd-mod_gnutls.conf
echo tls > %{buildroot}/usr/lib/modules-load.d/lighttpd-mod_openssl.conf
mkdir -p %{buildroot}%{_var}/log/lighttpd
mkdir -p %{buildroot}%{_var}/run/lighttpd
%if %{with tmpfiles}
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
echo 'D /run/lighttpd 0750 lighttpd lighttpd -' > \
    %{buildroot}/usr/lib/tmpfiles.d/lighttpd.conf
%endif
mkdir -p %{buildroot}%{_var}/lib/lighttpd/
install -m0644 -D lighttpd.sysusers.conf %{buildroot}%{_sysusersdir}/lighttpd.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post lighttpd.service
%preun

%systemd_preun lighttpd.service
%postun

%systemd_postun_with_restart lighttpd.service
%files -f %{oreon_filedir}/main.list
%files -n lighttpd-fastcgi -f %{oreon_filedir}/lighttpd-fastcgi.list
%files -n lighttpd-mod_authn_dbi -f %{oreon_filedir}/lighttpd-mod_authn_dbi.list
%files -n lighttpd-mod_authn_gssapi -f %{oreon_filedir}/lighttpd-mod_authn_gssapi.list
%files -n lighttpd-mod_authn_ldap -f %{oreon_filedir}/lighttpd-mod_authn_ldap.list
%files -n lighttpd-mod_authn_pam -f %{oreon_filedir}/lighttpd-mod_authn_pam.list
%files -n lighttpd-mod_authn_sasl -f %{oreon_filedir}/lighttpd-mod_authn_sasl.list
%files -n lighttpd-mod_deflate -f %{oreon_filedir}/lighttpd-mod_deflate.list
%files -n lighttpd-mod_gnutls -f %{oreon_filedir}/lighttpd-mod_gnutls.list
%files -n lighttpd-mod_magnet -f %{oreon_filedir}/lighttpd-mod_magnet.list
%files -n lighttpd-mod_maxminddb -f %{oreon_filedir}/lighttpd-mod_maxminddb.list
%files -n lighttpd-mod_mbedtls -f %{oreon_filedir}/lighttpd-mod_mbedtls.list
%files -n lighttpd-mod_nss -f %{oreon_filedir}/lighttpd-mod_nss.list
%files -n lighttpd-mod_openssl -f %{oreon_filedir}/lighttpd-mod_openssl.list
%files -n lighttpd-mod_vhostdb_dbi -f %{oreon_filedir}/lighttpd-mod_vhostdb_dbi.list
%files -n lighttpd-mod_vhostdb_ldap -f %{oreon_filedir}/lighttpd-mod_vhostdb_ldap.list
%files -n lighttpd-mod_vhostdb_mysql -f %{oreon_filedir}/lighttpd-mod_vhostdb_mysql.list
%files -n lighttpd-mod_vhostdb_pgsql -f %{oreon_filedir}/lighttpd-mod_vhostdb_pgsql.list
%files -n lighttpd-mod_webdav -f %{oreon_filedir}/lighttpd-mod_webdav.list
%files -n lighttpd-filesystem -f %{oreon_filedir}/lighttpd-filesystem.list

%changelog

%autochangelog
