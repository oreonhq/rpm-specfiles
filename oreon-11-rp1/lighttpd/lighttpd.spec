%global source0_hash none

%define webroot /var/www/lighttpd

# We have an bunch of --with/--without options to pass, make it easy with bcond
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

%if 0%{?rhel} >= 9
%bcond_with    dbi
%else
%bcond_without dbi
%endif
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

# We can't have bcond names with hyphens
%bcond_without webdavprops
%bcond_without webdavlocks

# The /var/run/lighttpd directory uses tmpfiles.d when mounted using tmpfs
%if 0%{?fedora} || 0%{?rhel} >= 8
%bcond_without tmpfiles
%else
%bcond_with    tmpfiles
%endif

Summary: Lightning fast webserver with light system requirements
Name: lighttpd
Version: 1.4.84
Release: 2%{?dist}
License: BSD-3-Clause
URL: http://www.lighttpd.net/
Source0: http://download.lighttpd.net/lighttpd/releases-1.4.x/lighttpd-%{version}.tar.xz
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
BuildRequires: systemd
# preserve installation of modules historically bundled with lighttpd package
Requires(post): %{name}-mod_deflate
Requires(post): %{name}-mod_webdav
%{?with_lua:Requires(post): %{name}-mod_magnet}
%{?with_openssl:Requires(post): %{name}-mod_openssl}
Provides: webserver
BuildRequires: autoconf, automake, libtool, m4, pkg-config, /usr/bin/awk
BuildRequires: libxcrypt-devel
%{?with_pcre:BuildRequires: pcre-devel}
%{?with_pcre2:BuildRequires: pcre2-devel}
%{?with_nettle:BuildRequires: nettle-devel}
%{?with_unwind:BuildRequires: libunwind-devel}

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

# Install our own logrotate entry
install -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/logrotate.d/lighttpd

# Install our own php.d ini file
install -D -p -m 0644 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/php.d/lighttpd.ini

# Install upstream systemd service
install -D -p -m 0644 doc/systemd/lighttpd.service \
    %{buildroot}%{_unitdir}/lighttpd.service

# Install our own default web page and images
mkdir -p %{buildroot}%{webroot}
install -p -m 0644 %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} \
    %{buildroot}%{webroot}/

# Symlink for the powered-by-$DISTRO image (install empty image on EL5)
%if %{with systemlogos}
ln -s %{_datadir}/pixmaps/poweredby.png \
%else
install -p -m 0644 %{SOURCE14} \
%endif
    %{buildroot}%{webroot}/poweredby.png

# Example configuration to be included as %%doc
rm -rf config
cp -a doc/config config
find config -name 'Makefile*' | xargs rm -f
# Remove +x from scripts to be included as %%doc to avoid auto requirement
chmod -x doc/scripts/*.sh

# Install (*patched above*) sample config files
mkdir -p %{buildroot}%{_sysconfdir}/lighttpd
cp -a config/*.conf config/*.d %{buildroot}%{_sysconfdir}/lighttpd/
mkdir -p %{buildroot}/usr/lib/modules-load.d
echo tls > %{buildroot}/usr/lib/modules-load.d/lighttpd-mod_gnutls.conf
echo tls > %{buildroot}/usr/lib/modules-load.d/lighttpd-mod_openssl.conf

# Install empty log directory to include
mkdir -p %{buildroot}%{_var}/log/lighttpd

# Install empty run directory to include (for the example fastcgi socket)
mkdir -p %{buildroot}%{_var}/run/lighttpd
%if %{with tmpfiles}
# Setup tmpfiles.d config for the above
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
echo 'D /run/lighttpd 0750 lighttpd lighttpd -' > \
    %{buildroot}/usr/lib/tmpfiles.d/lighttpd.conf
%endif

mkdir -p %{buildroot}%{_var}/lib/lighttpd/

install -m0644 -D lighttpd.sysusers.conf %{buildroot}%{_sysusersdir}/lighttpd.conf


%post
%systemd_post lighttpd.service

%preun
%systemd_preun lighttpd.service

%postun
%systemd_postun_with_restart lighttpd.service

%files
%license COPYING
%doc AUTHORS README
%doc config/ doc/scripts/cert-staple.sh doc/scripts/rrdtool-graph.sh
%config(noreplace) %{_sysconfdir}/lighttpd/*.conf
%config(noreplace) %{_sysconfdir}/lighttpd/conf.d/*.conf
%exclude %{_sysconfdir}/lighttpd/conf.d/deflate.conf
%exclude %{_sysconfdir}/lighttpd/conf.d/fastcgi.conf
%exclude %{_sysconfdir}/lighttpd/conf.d/magnet.conf
%exclude %{_sysconfdir}/lighttpd/conf.d/webdav.conf
%exclude %{_sysconfdir}/lighttpd/conf.d/tls.conf.defaultconf
%config %{_sysconfdir}/lighttpd/conf.d/mod.template
%config %{_sysconfdir}/lighttpd/vhosts.d/vhosts.template
%config(noreplace) %{_sysconfdir}/logrotate.d/lighttpd
%{_unitdir}/lighttpd.service
%if %{with tmpfiles}
%config(noreplace) /usr/lib/tmpfiles.d/lighttpd.conf
%endif
%{_sbindir}/lighttpd
%{_sbindir}/lighttpd-angel
%{_libdir}/lighttpd/
%exclude %{_libdir}/lighttpd/mod_authn_dbi.so
%exclude %{_libdir}/lighttpd/mod_authn_gssapi.so
%exclude %{_libdir}/lighttpd/mod_authn_ldap.so
%exclude %{_libdir}/lighttpd/mod_authn_pam.so
%exclude %{_libdir}/lighttpd/mod_authn_sasl.so
%exclude %{_libdir}/lighttpd/mod_deflate.so
%exclude %{_libdir}/lighttpd/mod_gnutls.so
%exclude %{_libdir}/lighttpd/mod_magnet.so
%exclude %{_libdir}/lighttpd/mod_maxminddb.so
%exclude %{_libdir}/lighttpd/mod_mbedtls.so
%exclude %{_libdir}/lighttpd/mod_openssl.so
%exclude %{_libdir}/lighttpd/mod_nss.so
%exclude %{_libdir}/lighttpd/mod_vhostdb_dbi.so
%exclude %{_libdir}/lighttpd/mod_vhostdb_ldap.so
%exclude %{_libdir}/lighttpd/mod_vhostdb_mysql.so
%exclude %{_libdir}/lighttpd/mod_vhostdb_pgsql.so
%{_mandir}/man8/lighttpd*8*
%{webroot}/*.ico
%{webroot}/*.png
# This is not really configuration, but prevent loss of local changes
%config %{webroot}/index.html

%files fastcgi
%doc doc/outdated/fastcgi*.txt
%config(noreplace) %{_sysconfdir}/php.d/lighttpd.ini
%config(noreplace) %{_sysconfdir}/lighttpd/conf.d/fastcgi.conf

%if %{with dbi}
%files mod_authn_dbi
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_authn_dbi.so
%endif

%if %{with krb5}
%files mod_authn_gssapi
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_authn_gssapi.so
%endif

%if %{with ldap}
%files mod_authn_ldap
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_authn_ldap.so
%endif

%if %{with pam}
%files mod_authn_pam
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_authn_pam.so
%endif

%if %{with sasl}
%files mod_authn_sasl
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_authn_sasl.so
%endif

%files mod_deflate
%doc doc/outdated/compress.txt
%config(noreplace) %{_sysconfdir}/lighttpd/conf.d/deflate.conf
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_deflate.so

%if %{with gnutls}
%files mod_gnutls
%config(noreplace) /usr/lib/modules-load.d/lighttpd-mod_gnutls.conf
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_gnutls.so
%endif

%if %{with lua}
%files mod_magnet
%doc doc/outdated/magnet.txt
%config(noreplace) %{_sysconfdir}/lighttpd/conf.d/magnet.conf
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_magnet.so
%endif

%if %{with maxminddb}
%files mod_maxminddb
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_maxminddb.so
%endif

%if %{with mbedtls}
%files mod_mbedtls
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_mbedtls.so
%endif

%if %{with nss}
%files mod_nss
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_nss.so
%endif

%if %{with openssl}
%files mod_openssl
%config(noreplace) /usr/lib/modules-load.d/lighttpd-mod_openssl.conf
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_openssl.so
%endif

%if %{with dbi}
%files mod_vhostdb_dbi
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_vhostdb_dbi.so
%endif

%if %{with ldap}
%files mod_vhostdb_ldap
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_vhostdb_ldap.so
%endif

%if %{with mysql}
%files mod_vhostdb_mysql
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_vhostdb_mysql.so
%endif

%if %{with pgsql}
%files mod_vhostdb_pgsql
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_vhostdb_pgsql.so
%endif

%files mod_webdav
%doc doc/outdated/webdav.txt
%config(noreplace) %{_sysconfdir}/lighttpd/conf.d/webdav.conf
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_webdav.so

%files filesystem
%dir %{_sysconfdir}/lighttpd/
%dir %{_sysconfdir}/lighttpd/conf.d/
%dir %{_sysconfdir}/lighttpd/vhosts.d/
%dir %{_var}/run/lighttpd/
%dir %{_var}/lib/lighttpd/
%if %{with tmpfiles}
%ghost %attr(0750, lighttpd, lighttpd) %{_var}/run/lighttpd/
%else
%attr(0750, lighttpd, lighttpd) %{_var}/run/lighttpd/
%endif
%attr(0750, lighttpd, lighttpd) %{_var}/lib/lighttpd/
%attr(0750, lighttpd, lighttpd) %{_var}/log/lighttpd/
%attr(0700, lighttpd, lighttpd) %dir %{webroot}/
%{_sysusersdir}/lighttpd.conf

%changelog
%autochangelog

