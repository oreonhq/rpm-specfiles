%global source0_hash c46b8691d41944b220a7aed3b728e18d2da47ab9d25025ae62f21266caef9b49

#
# Rebuild switch:
#  --with integrationtests	enable integration tests (not fully maintained, likely to fail)
#

# Switch from libmemcached to libmemcached-awesome from Fedora 35 onwards
%if (0%{?rhel} && 0%{?rhel} <= 8) || (0%{?fedora} && 0%{?fedora} <= 34)
%global libmemcached_pkg libmemcached
%else
%global libmemcached_pkg libmemcached-awesome
%endif

# Do a hardened build where possible
%global _hardened_build 1

# Dynamic modules contain references to symbols in main dæmon, so we need to disable linker checks for undefined symbols
%undefine _strict_symbol_defs_build

#global prever rc4
%global baserelease 3
%global mod_proxy_version 0.9.5
%global mod_vroot_version 0.9.12

Summary:		Flexible, stable and highly-configurable FTP server
Name:			proftpd
Version:		1.3.9
Release:		%{?prever:0.}%{baserelease}%{?prever:.%{prever}}%{?dist}
License:		GPL-2.0-or-later
URL:			http://www.proftpd.org/

Source0:		ftp://ftp.proftpd.org/distrib/source/proftpd-%{version}%{?prever}.tar.gz
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

BuildRequires:		coreutils
BuildRequires:		gcc
BuildRequires:		gettext
BuildRequires:		libacl-devel
BuildRequires:		libcap-devel
BuildRequires:		libidn2-devel
BuildRequires:		%{libmemcached_pkg}-devel >= 0.41
BuildRequires:		libpq-devel
BuildRequires:		libsodium-devel >= 1.0
BuildRequires:		libxcrypt-devel
BuildRequires:		logrotate
BuildRequires:		make
BuildRequires:		mariadb-connector-c-devel
BuildRequires:		ncurses-devel
BuildRequires:		openldap-devel
BuildRequires:		openssl-devel
BuildRequires:		pam-devel
BuildRequires:		pcre2-devel >= 10.30
BuildRequires:		perl-generators
BuildRequires:		perl-interpreter
BuildRequires:		pkgconfig
BuildRequires:		sed
BuildRequires:		sqlite-devel >= 3.8.5
BuildRequires:		systemd-rpm-macros
BuildRequires:		tar
BuildRequires:		zlib-devel

# Test suite requirements
BuildRequires:		check-devel
%if 0%{?fedora} > 34 || 0%{?rhel} > 8
BuildRequires:		glibc-gconv-extra
%endif
%if 0%{?_with_integrationtests:1}
BuildRequires:		perl(Compress::Zlib)
BuildRequires:		perl(Digest::MD5)
BuildRequires:		perl(HTTP::Request)
BuildRequires:		perl(IO::Socket::SSL)
BuildRequires:		perl(LWP::UserAgent)
BuildRequires:		perl(Net::FTPSSL)
BuildRequires:		perl(Net::SSLeay)
BuildRequires:		perl(Net::Telnet)
BuildRequires:		perl(Sys::HostAddr)
BuildRequires:		perl(Test::Harness)
BuildRequires:		perl(Test::Unit) >= 0.25
BuildRequires:		perl(Time::HiRes)
%endif

# Need systemd for ownership of /usr/lib/tmpfiles.d directory
Requires:		systemd

# Logs should be rotated periodically
Requires:		logrotate

# Scriptlet dependencies
Requires(preun):	coreutils, findutils
BuildRequires:		systemd
%{?systemd_requires}

Provides:		ftpserver

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
# devel package requires the same devel packages as were build-required
# for the main package
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
# ftpasswd --use-cracklib requires Crypt::Cracklib
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
# Modules to be built as DSO's (excluding mod_ifsession, always specified last)
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

# We'll be using the system certificate database, not the one provided by mod_proxy
rm %{buildroot}%{_sysconfdir}/cacerts.pem

# Make sure /run/proftpd exists at boot time for systems where it's on tmpfs (#656675)
install -d -m 755 %{buildroot}%{_prefix}/lib/tmpfiles.d
install -p -m 644 contrib/dist/rpm/proftpd-tmpfs.conf \
					%{buildroot}%{_prefix}/lib/tmpfiles.d/proftpd.conf

# Find translations
%find_lang proftpd

%check
# Integration tests not fully maintained - stick to API tests only by default
%if 0%{?_with_integrationtests:1}
ln ftpdctl tests/
make check
%else
# API tests should always be OK
if ! make -C tests api-tests; then
	# Diagnostics to report upstream
	cat tests/api-tests.log
	./proftpd -V
	# Fail the build
	false
fi
%endif

%post
%systemd_post proftpd.service
if [ $1 -eq 1 ]; then
	# Initial installation
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
	# Package removal, not upgrade
	find /run/proftpd -depth -mindepth 1 |
		xargs rm -rf &>/dev/null || :
fi

%postun
%systemd_postun_with_restart proftpd.service

%files -f proftpd.lang
%license COPYING
%doc CREDITS ChangeLog NEWS README.md
%doc contrib/README.contrib contrib/README.ratio
%doc doc/* sample-configurations/
%dir %{_localstatedir}/ftp/
%dir %{_localstatedir}/ftp/pub/
%dir /run/proftpd/
%dir %{_sysconfdir}/logrotate.d/
%dir %{_sysconfdir}/proftpd/
%dir %{_sysconfdir}/proftpd/conf.d/
%config(noreplace) %{_localstatedir}/ftp/welcome.msg
%config(noreplace) %{_sysconfdir}/blacklist.dat
%config(noreplace) %{_sysconfdir}/dhparams.pem
%config(noreplace) %{_sysconfdir}/ftpusers
%config(noreplace) %{_sysconfdir}/logrotate.d/proftpd
%config(noreplace) %{_sysconfdir}/pam.d/proftpd
%config(noreplace) %{_sysconfdir}/proftpd.conf
%config(noreplace) %{_sysconfdir}/proftpd/anonftp.conf
%config(noreplace) %{_sysconfdir}/proftpd/modules.conf
%config(noreplace) %{_sysconfdir}/proftpd/mod_ban.conf
%config(noreplace) %{_sysconfdir}/proftpd/mod_qos.conf
%config(noreplace) %{_sysconfdir}/proftpd/mod_tls.conf
%config(noreplace) %{_sysconfdir}/sysconfig/proftpd
%{_unitdir}/proftpd.service
%{_unitdir}/proftpd.socket
%{_unitdir}/proftpd@.service
%{_prefix}/lib/tmpfiles.d/proftpd.conf
%{_bindir}/ftpdctl
%{_sbindir}/ftpscrub
%{_sbindir}/ftpshut
%{_sbindir}/in.proftpd
%{_sbindir}/proftpd
%{_mandir}/man5/proftpd.conf.5*
%{_mandir}/man5/xferlog.5*
%{_mandir}/man8/ftpdctl.8*
%{_mandir}/man8/ftpscrub.8*
%{_mandir}/man8/ftpshut.8*
%{_mandir}/man8/proftpd.8*
%dir %{_libexecdir}/proftpd/
%{_libexecdir}/proftpd/mod_ban.so
%{_libexecdir}/proftpd/mod_ctrls_admin.so
%{_libexecdir}/proftpd/mod_copy.so
%{_libexecdir}/proftpd/mod_deflate.so
%{_libexecdir}/proftpd/mod_exec.so
%{_libexecdir}/proftpd/mod_facl.so
%{_libexecdir}/proftpd/mod_ifsession.so
%{_libexecdir}/proftpd/mod_ifversion.so
%{_libexecdir}/proftpd/mod_load.so
%{_libexecdir}/proftpd/mod_qos.so
%{_libexecdir}/proftpd/mod_quotatab.so
%{_libexecdir}/proftpd/mod_quotatab_file.so
%{_libexecdir}/proftpd/mod_quotatab_radius.so
%{_libexecdir}/proftpd/mod_quotatab_sql.so
%{_libexecdir}/proftpd/mod_radius.so
%{_libexecdir}/proftpd/mod_ratio.so
%{_libexecdir}/proftpd/mod_rewrite.so
%{_libexecdir}/proftpd/mod_sftp.so
%{_libexecdir}/proftpd/mod_sftp_pam.so
%{_libexecdir}/proftpd/mod_sftp_sql.so
%{_libexecdir}/proftpd/mod_shaper.so
%{_libexecdir}/proftpd/mod_site_misc.so
%{_libexecdir}/proftpd/mod_sql.so
%{_libexecdir}/proftpd/mod_sql_passwd.so
%{_libexecdir}/proftpd/mod_tls_memcache.so
%{_libexecdir}/proftpd/mod_tls_shmcache.so
%{_libexecdir}/proftpd/mod_unique_id.so
%{_libexecdir}/proftpd/mod_vroot.so
%{_libexecdir}/proftpd/mod_wrap2.so
%{_libexecdir}/proftpd/mod_wrap2_file.so
%{_libexecdir}/proftpd/mod_wrap2_sql.so
%exclude %{_libexecdir}/proftpd/*.a
%if 0%{?fedora} < 36 && 0%{?rhel} < 10
%exclude %{_libexecdir}/proftpd/*.la
%endif
%attr(331, ftp, ftp) %dir %{_localstatedir}/ftp/uploads/
%attr(750, root, root) %dir %{_localstatedir}/log/proftpd/

%files devel
%{_bindir}/prxs
%{_includedir}/proftpd/
%{_libdir}/pkgconfig/proftpd.pc

%files ldap
%doc contrib/mod_quotatab_ldap.ldif contrib/mod_quotatab_ldap.schema
%{_libexecdir}/proftpd/mod_ldap.so
%{_libexecdir}/proftpd/mod_quotatab_ldap.so

%files mysql
%{_libexecdir}/proftpd/mod_sql_mysql.so

%files postgresql
%{_libexecdir}/proftpd/mod_sql_postgres.so

%files proxy
%doc contrib/mod_proxy/README.md
%{_libexecdir}/proftpd/mod_proxy.so

%files sqlite
%{_libexecdir}/proftpd/mod_sql_sqlite.so

%files utils
%doc contrib/xferstats.holger-preiss
%{_bindir}/ftpasswd
%{_bindir}/ftpcount
%{_bindir}/ftpmail
%{_bindir}/ftpquota
%{_bindir}/ftptop
%{_bindir}/ftpwho
%{_mandir}/man1/ftpasswd.1*
%{_mandir}/man1/ftpcount.1*
%{_mandir}/man1/ftpmail.1*
%{_mandir}/man1/ftpquota.1*
%{_mandir}/man1/ftptop.1*
%{_mandir}/man1/ftpwho.1*

%changelog
%autochangelog
