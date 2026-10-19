%global source11_hash 85f1aeae37ab76b35972d3ddd64c4338cf36cca0b5ba3b93e39335259796cd86
%global source10_hash c46b8691d41944b220a7aed3b728e18d2da47ab9d25025ae62f21266caef9b49
%global source0_hash c46b8691d41944b220a7aed3b728e18d2da47ab9d25025ae62f21266caef9b49
%global libmemcached_pkg libmemcached-awesome
%global _hardened_build 1
%undefine _strict_symbol_defs_build
%global baserelease 3
%global mod_proxy_version 0.9.5
%global mod_vroot_version 0.9.12
Summary:        Flexible, stable and highly-configurable FTP server
Name:			proftpd
Version:		1.3.9d
Release:        1%{?dist}
License:		GPL-2.0-or-later
URL:			http://www.proftpd.org/
Source0:        ftp://ftp.%{name}.org/distrib/source/%{name}-%{version}.tar.gz
Source1:		proftpd.conf
Source2:		modules.conf
Source3:		mod_tls.conf
Source4:		mod_ban.conf
Source5:		mod_qos.conf
Source6:		anonftp.conf
Source8:		proftpd-welcome.msg
Source9:		proftpd.sysconfig
Source10:		http://github.com/Castaglia/proftpd-mod_vroot/archive/v%{mod_vroot_version}.tar.gz
Source11:		http://github.com/Castaglia/proftpd-mod_proxy/archive/v%{mod_proxy_version}.tar.gz
Patch1:			proftpd-1.3.8-shellbang.patch
Patch2:			mod_proxy-certificate.patch
Patch3:			proftpd-1.3.4rc1-mod_vroot-test.patch
%if 0%{?_with_integrationtests:1}
%endif
Requires:		systemd
Requires:		logrotate
Requires(preun):	coreutils, findutils
%{?systemd_requires}
Provides:		ftpserver
# oreon:deps
BuildRequires:  check-devel
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  libidn2-devel
BuildRequires:  libmemcached-awesome-devel
BuildRequires:  libpq-devel
BuildRequires:  libsodium-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  logrotate
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  ncurses-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl(Crypt::Cracklib)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRequires:  sqlite-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  tar
BuildRequires:  zlib-devel
# /oreon:deps
%description
ProFTPD is an enhanced FTP server with a focus toward simplicity, security,
and ease of configuration. It features a very Apache-like configuration
syntax, and a highly customizable server infrastructure, including support for
multiple 'virtual' FTP servers, anonymous FTP, and permission-based directory
visibility.

This package defaults to the standalone behavior of ProFTPD, but all the
needed scripts to have it run by systemd instead are included.

%package devel
Summary:	ProFTPD - Tools and header files for developers
Requires:	%{name} = %{version}-%{release}
Requires:	gcc, libtool
Requires:	libacl-devel
Requires:	libcap-devel
Requires:	%{libmemcached_pkg}-devel >= 0.41
Requires:	libpq-devel
Requires:	libsodium-devel >= 1.0
Requires:	mariadb-connector-c-devel
Requires:	ncurses-devel
Requires:	openldap-devel
Requires:	openssl-devel
Requires:	pam-devel
Requires:	pcre2-devel >= 10.30
Requires:	pkgconfig
Requires:	sqlite-devel
Requires:	zlib-devel
%description devel
This package is required to build additional modules for ProFTPD.

%package ldap
Summary:	Module to add LDAP support to the ProFTPD FTP server
Requires:	%{name} = %{version}-%{release}
%description ldap
Module to add LDAP support to the ProFTPD FTP server.

%package mysql
Summary:	Module to add MySQL support to the ProFTPD FTP server
Requires:	%{name} = %{version}-%{release}
%description mysql
Module to add MySQL support to the ProFTPD FTP server.

%package postgresql
Summary:	Module to add PostgreSQL support to the ProFTPD FTP server
Requires:	%{name} = %{version}-%{release}
%description postgresql
Module to add PostgreSQL support to the ProFTPD FTP server.

%package proxy
Summary:	Module to add proxying support to the ProFTPD FTP server
Requires:	%{name} = %{version}-%{release}
%description proxy
Module to add proxying support to the ProFTPD FTP server.

%package sqlite
Summary:	Module to add SQLite support to the ProFTPD FTP server
Requires:	%{name} = %{version}-%{release}
%description sqlite
Module to add SQLite support to the ProFTPD FTP server.

%package utils
Summary:	ProFTPD - Additional utilities
Requires:	%{name} = %{version}-%{release}
Requires:	perl-interpreter
BuildRequires:	perl(Crypt::Cracklib)
Requires:	perl(Crypt::Cracklib)
%description utils
This package contains additional utilities for monitoring and configuring the
ProFTPD server:

* ftpasswd: generate passwd(5) files for use with AuthUserFile
* ftpcount: show the current number of connections per server/virtualhost
* ftpmail: monitor transfer log and send email when files uploaded
* ftpquota: manipulate quota tables
* ftptop: show the current status of FTP sessions
* ftpwho: show the current process information for each FTP session

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}%{?prever}

# Extract mod_proxy and mod_vroot source into contrib/
# Directories must be named mod_{proxy,vroot} for configure script to find them
cd contrib
tar xfz %{SOURCE10}
tar xfz %{SOURCE11}
mv proftpd-mod_proxy-%{mod_proxy_version} mod_proxy
mv proftpd-mod_vroot-%{mod_vroot_version} mod_vroot
cd -

# Default config files
sed -e 's|@RUNDIR@|/run|' %{SOURCE1} > proftpd.conf
sed -e 's|@RUNDIR@|/run|' %{SOURCE2} > modules.conf
sed -e 's|@RUNDIR@|/run|' %{SOURCE3} > mod_tls.conf
sed -e 's|@RUNDIR@|/run|' %{SOURCE4} > mod_ban.conf
sed -e 's|@RUNDIR@|/run|' %{SOURCE5} > mod_qos.conf
sed -e 's|@RUNDIR@|/run|' %{SOURCE6} > anonftp.conf

# Avoid documentation name conflicts
mv contrib/README contrib/README.contrib

# Change shellbangs /usr/bin/env perl ⇒ /usr/bin/perl
%patch -P 1

# Use the system-wide CA certificate file rather than the one bundled with mod_proxy
%patch -P 2 -b .proxy-ca-cert

# If we're running the full test suite, include the mod_vroot test
%patch -P 3 -p1 -b .test_vroot

# Tweak logrotate script for systemd compatibility (#802178)
sed -i -e '/killall/s/test.*/systemctl try-reload-or-restart proftpd.service/' \
	contrib/dist/rpm/proftpd.logrotate

# Avoid docfile dependencies
chmod -c -x contrib/xferstats.holger-preiss

# Remove bogus exec permissions from source files
chmod -c -x include/hanson-tpl.h lib/hanson-tpl.c

# Remove any patch backup files from documentation
find doc/ contrib/ -name '*.orig' -delete

%build

SMOD1=mod_sql:mod_sql_passwd:mod_sql_mysql:mod_sql_postgres:mod_sql_sqlite
SMOD2=mod_quotatab:mod_quotatab_file:mod_quotatab_ldap:mod_quotatab_radius:mod_quotatab_sql
SMOD3=mod_ldap:mod_ban:mod_ctrls_admin:mod_facl:mod_load:mod_vroot
SMOD4=mod_radius:mod_ratio:mod_rewrite:mod_site_misc:mod_exec:mod_shaper
SMOD5=mod_wrap2:mod_wrap2_file:mod_wrap2_sql:mod_copy:mod_deflate:mod_ifversion:mod_qos
SMOD6=mod_sftp:mod_sftp_pam:mod_sftp_sql:mod_tls_shmcache:mod_tls_memcache
SMOD7=mod_proxy:mod_unique_id
%configure \
			--libexecdir="%{_libexecdir}/proftpd" \
			--localstatedir="/run/proftpd" \
			--disable-strip \
			--enable-ctrls \
			--enable-dso \
			--enable-facl \
			--enable-ipv6 \
			--enable-memcache \
			--enable-nls \
			--enable-openssl \
			--disable-pcre \
			--enable-pcre2 \
			--enable-sodium \
			--disable-redis \
			--enable-shadow \
			--enable-tests=nonetwork \
			--with-libraries="%{_libdir}/mariadb" \
			--with-includes="%{_includedir}/mysql" \
			--with-modules=mod_readme:mod_auth_pam:mod_tls \
			--with-shared=${SMOD1}:${SMOD2}:${SMOD3}:${SMOD4}:${SMOD5}:${SMOD6}:${SMOD7}:mod_ifsession
%{make_build}
%install
%{make_install} INSTALL_USER=`id -un` INSTALL_GROUP=`id -gn`
mkdir -p %{buildroot}%{_sysconfdir}/proftpd/conf.d
install -D -p -m 640 proftpd.conf	%{buildroot}%{_sysconfdir}/proftpd.conf
install -D -p -m 640 anonftp.conf	%{buildroot}%{_sysconfdir}/proftpd/anonftp.conf
install -D -p -m 640 modules.conf	%{buildroot}%{_sysconfdir}/proftpd/modules.conf
install -D -p -m 640 mod_ban.conf	%{buildroot}%{_sysconfdir}/proftpd/mod_ban.conf
install -D -p -m 640 mod_qos.conf	%{buildroot}%{_sysconfdir}/proftpd/mod_qos.conf
install -D -p -m 640 mod_tls.conf	%{buildroot}%{_sysconfdir}/proftpd/mod_tls.conf
install -D -p -m 644 contrib/dist/rpm/proftpd.pam \
					%{buildroot}%{_sysconfdir}/pam.d/proftpd
install -D -p -m 644 contrib/dist/rpm/proftpd.service \
					%{buildroot}%{_unitdir}/proftpd.service
install -D -p -m 644 contrib/dist/systemd/proftpd.socket \
					%{buildroot}%{_unitdir}/proftpd.socket
install -D -p -m 644 contrib/dist/systemd/proftpd@.service \
					%{buildroot}%{_unitdir}/proftpd@.service
install -D -p -m 644 contrib/dist/rpm/proftpd.logrotate \
					%{buildroot}%{_sysconfdir}/logrotate.d/proftpd
install -D -p -m 644 %{SOURCE8}		%{buildroot}%{_localstatedir}/ftp/welcome.msg
install -D -p -m 644 %{SOURCE9}		%{buildroot}%{_sysconfdir}/sysconfig/proftpd
mkdir -p %{buildroot}%{_localstatedir}/{ftp/{pub,uploads},log/proftpd}
touch %{buildroot}%{_sysconfdir}/ftpusers
rm %{buildroot}%{_sysconfdir}/cacerts.pem
install -d -m 755 %{buildroot}%{_prefix}/lib/tmpfiles.d
install -p -m 644 contrib/dist/rpm/proftpd-tmpfs.conf \
					%{buildroot}%{_prefix}/lib/tmpfiles.d/proftpd.conf
%find_lang proftpd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if 0%{?_with_integrationtests:1}
ln ftpdctl tests/
make check
%else
if ! make -C tests api-tests; then
	cat tests/api-tests.log
	./proftpd -V
	false
fi
%endif
%post

%systemd_post proftpd.service
if [ $1 -eq 1 ]; then
	IFS=":"; cat /etc/passwd | \
	while { read username nu nu gid nu nu nu nu; }; do \
		if [ $gid -lt 100 -a "$username" != "ftp" ]; then
			echo $username >> %{_sysconfdir}/ftpusers
		fi
	done
fi
%preun

%systemd_preun proftpd.service
if [ $1 -eq 0 ]; then
	find /run/proftpd -depth -mindepth 1 |
		xargs rm -rf &>/dev/null || :
fi
%postun

%systemd_postun_with_restart proftpd.service
%files -f %{oreon_filedir}/main.list
%files -n proftpd-devel -f %{oreon_filedir}/proftpd-devel.list
%files -n proftpd-ldap -f %{oreon_filedir}/proftpd-ldap.list
%files -n proftpd-mysql -f %{oreon_filedir}/proftpd-mysql.list
%files -n proftpd-postgresql -f %{oreon_filedir}/proftpd-postgresql.list
%files -n proftpd-proxy -f %{oreon_filedir}/proftpd-proxy.list
%files -n proftpd-sqlite -f %{oreon_filedir}/proftpd-sqlite.list
%files -n proftpd-utils -f %{oreon_filedir}/proftpd-utils.list

%changelog

%autochangelog
