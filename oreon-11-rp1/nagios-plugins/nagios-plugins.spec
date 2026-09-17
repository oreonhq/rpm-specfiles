%global source0_hash 9a246245d8270f15759763160c48df5dcdc2af9632733a5238930fde6778b578

%global _hardened_build 1

%global commit 72dd0a308130b9778828d143d1b9d9906218d6ac
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commdate 20191209
%global fromgit 0
## Use when first building a package set to see what patches are needed
%global bootstrap 0

%if 0%{?fedora} >= 36 || 0%{?rhel} >= 9
%bcond_with libdbi
%else
%bcond_without libdbi
%endif

%if 0%{?rhel} >= 9
%bcond_with radius
%else
%bcond_without radius
%endif

Name: nagios-plugins
Version: 2.4.12
%if 0%{?fromgit}
Release: 4.%{?commdate}git%{?shortcommit}%{?dist}
%else
Release: 4%{?dist}
%endif

Summary: Host/service/network monitoring program plugins for Nagios

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://www.nagios-plugins.org/

## When using checkouts from git, use the following
%if 0%{?fromgit} 
Source0: https://github.com/%{name}/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0: https://github.com/%{name}/%{name}/releases/download/release-%{version}/%{name}-%{version}.tar.gz
%endif
Source1: nagios-plugins.README.Fedora

# Patch from upstream PR https://github.com/nagios-plugins/nagios-plugins/pull/581
Patch1: %{name}-ntpsec-support.patch
Patch2: nagios-plugins-0002-Remove-assignment-of-not-parsed-to-jitter.patch
Patch7: nagios-plugins-0007-Fix-the-use-lib-statement-and-the-external-ntp-comma.patch
Patch12: nagios-plugins-0012-fix-perl-ntp-ipv6.patch

BuildRequires: make
BuildRequires: %{_bindir}/mailq
BuildRequires: procps
BuildRequires: %{_bindir}/ssh
BuildRequires: %{_bindir}/uptime
BuildRequires: %{_sbindir}/fping

# Needed for the git code
%if 0%{?fromgit}
BuildRequires: automake
BuildRequires: autoconf
%endif
#
BuildRequires: bind-utils
BuildRequires: gcc
BuildRequires: gettext
%if %{with libdbi}
BuildRequires: libdbi-devel
%else
Obsoletes: nagios-plugins-dbi < 2.4.0-6
%endif
BuildRequires: iputils
BuildRequires: net-snmp-devel
BuildRequires: net-snmp-utils
%if 0%{?fedora}
BuildRequires: ntpsec
%endif
BuildRequires: openldap-devel
BuildRequires: perl(Net::SNMP)
BuildRequires: perl(Crypt::X509)
BuildRequires: perl(Date::Parse)
BuildRequires: perl(LWP::Simple)
BuildRequires: perl(Text::Glob)
BuildRequires: perl-generators
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires: postgresql-devel
%else
BuildRequires: libpq-devel
%endif
BuildRequires: qstat
BuildRequires: samba-client

BuildRequires: mariadb-connector-c-devel
%if %{with radius}
BuildRequires: freeradius-client-devel
%endif
BuildRequires: %{_bindir}/uptime
BuildRequires: iputils
BuildRequires: %{_bindir}/ps

Requires: nagios-common >= 3.3.1-1

Obsoletes: nagios-plugins-linux_raid < 1.4.16-11

# nagios-plugins-1.4.16: the included gnulib files were last updated
# in June/July 2010
# Bundled gnulib exception (https://fedorahosted.org/fpc/ticket/174)
Provides: bundled(gnulib)

# Do not provide private Perl modules
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(utils\\)
%global reqfilt sh -c "%{__perl_requires} | sed -e 's!perl(utils)!nagios-plugins-perl!'"
%global __perl_requires %{reqfilt}

%description
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a Unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios. This package
contains those plugins.

%package all
Summary: Nagios Plugins - All plugins
Requires: nagios-plugins-breeze, nagios-plugins-by_ssh, nagios-plugins-dhcp, nagios-plugins-dig, nagios-plugins-disk, nagios-plugins-disk_smb, nagios-plugins-dns, nagios-plugins-dummy, nagios-plugins-file_age, nagios-plugins-flexlm, nagios-plugins-fping, nagios-plugins-hpjd, nagios-plugins-http, nagios-plugins-icmp, nagios-plugins-ide_smart, nagios-plugins-ircd, nagios-plugins-ldap, nagios-plugins-load, nagios-plugins-log, nagios-plugins-mailq, nagios-plugins-mrtg, nagios-plugins-mrtgtraf, nagios-plugins-mysql, nagios-plugins-nagios, nagios-plugins-nt, nagios-plugins-ntp, nagios-plugins-nwstat, nagios-plugins-oracle, nagios-plugins-overcr, nagios-plugins-pgsql, nagios-plugins-ping, nagios-plugins-procs, nagios-plugins-game, nagios-plugins-real, nagios-plugins-rpc, nagios-plugins-smtp, nagios-plugins-snmp, nagios-plugins-ssh, nagios-plugins-ssl_validity, nagios-plugins-swap, nagios-plugins-tcp, nagios-plugins-time, nagios-plugins-ups, nagios-plugins-users, nagios-plugins-wave, nagios-plugins-cluster
%ifnarch ppc ppc64 ppc64p7 sparc sparc64
Requires: nagios-plugins-sensors
%endif
%if 0%{?fedora}
Requires: nagios-plugins-ntp-perl
%endif

%description all
This package provides all Nagios plugins.

%package apt
Summary: Nagios Plugin - check_apt
Requires: nagios-plugins = %{version}-%{release}

%description apt
Provides check_apt support for Nagios.

%package breeze
Summary: Nagios Plugin - check_breeze
Requires: nagios-plugins = %{version}-%{release}

%description breeze
Provides check_breeze support for Nagios.

%package by_ssh
Summary: Nagios Plugin - check_by_ssh
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/ssh

%description by_ssh
Provides check_by_ssh support for Nagios.

%package cluster
Summary: Nagios Plugin - check_cluster
Requires: nagios-plugins = %{version}-%{release}

%description cluster
Provides check_cluster support for Nagios.

%if %{with libdbi}
%package dbi
Summary: Nagios Plugin - check_dbi
Requires: nagios-plugins = %{version}-%{release}

%description dbi
Provides check_dbi support for Nagios.
%endif

%package dhcp
Summary: Nagios Plugin - check_dhcp
Requires: nagios-plugins = %{version}-%{release}
Requires: group(nagios)
Requires(pre): group(nagios)

%description dhcp
Provides check_dhcp support for Nagios.

%package dig
Summary: Nagios Plugin - check_dig
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/dig

%description dig
Provides check_dig support for Nagios.

%package disk
Summary: Nagios Plugin - check_disk
Requires: nagios-plugins = %{version}-%{release}

%description disk
Provides check_disk support for Nagios.

%package disk_smb
Summary: Nagios Plugin - check_disk_smb
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/smbclient
Requires: perl(utf8::all)

%description disk_smb
Provides check_disk_smb support for Nagios.

%package dns
Summary: Nagios Plugin - check_dns
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/nslookup

%description dns
Provides check_dns support for Nagios.

%package dummy
Summary: Nagios Plugin - check_dummy
Requires: nagios-plugins = %{version}-%{release}

%description dummy
Provides check_dummy support for Nagios.
This plugin does not actually check anything, simply provide it with a flag
0-4 and it will return the corresponding status code to Nagios.

%package file_age
Summary: Nagios Plugin - check_file_age
Requires: nagios-plugins = %{version}-%{release}

%description file_age
Provides check_file_age support for Nagios.

%package flexlm
Summary: Nagios Plugin - check_flexlm
Requires: nagios-plugins = %{version}-%{release}

%description flexlm
Provides check_flexlm support for Nagios.

%package fping
Summary: Nagios Plugin - check_fping
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_sbindir}/fping
Requires: group(nagios)
Requires(pre): group(nagios)

%description fping
Provides check_fping support for Nagios.

%package game
Summary: Nagios Plugin - check_game
Requires: nagios-plugins = %{version}-%{release}
Requires: qstat

%description game
Provides check_game support for Nagios.

%package hpjd
Summary: Nagios Plugin - check_hpjd
Requires: nagios-plugins = %{version}-%{release}

%description hpjd
Provides check_hpjd support for Nagios.

%package http
Summary: Nagios Plugin - check_http
Requires: nagios-plugins = %{version}-%{release}
Requires: openssl

%description http
Provides check_http support for Nagios.

%package icmp
Summary: Nagios Plugin - check_icmp
Requires: nagios-plugins = %{version}-%{release}
Requires: group(nagios)
Requires(pre): group(nagios)

%description icmp
Provides check_icmp support for Nagios.

%package ide_smart
Summary: Nagios Plugin - check_ide_smart
Requires: nagios-plugins = %{version}-%{release}
Requires: group(nagios)
Requires(pre): group(nagios)

%description ide_smart
Provides check_ide_smart support for Nagios.

%package ifoperstatus
Summary: Nagios Plugin - check_ifoperstatus
Requires: nagios-plugins = %{version}-%{release}

%description ifoperstatus
Provides check_ifoperstatus support for Nagios to monitor network interfaces.

%package ifstatus
Summary: Nagios Plugin - check_ifstatus
Requires: nagios-plugins = %{version}-%{release}

%description ifstatus
Provides check_ifstatus support for Nagios to monitor network interfaces.

%package ircd
Summary: Nagios Plugin - check_ircd
Requires: nagios-plugins = %{version}-%{release}

%description ircd
Provides check_ircd support for Nagios.

%package ldap
Summary: Nagios Plugin - check_ldap
Requires: nagios-plugins = %{version}-%{release}
Requires: openssl

%description ldap
Provides check_ldap support for Nagios.

%package load
Summary: Nagios Plugin - check_load
Requires: nagios-plugins = %{version}-%{release}

%description load
Provides check_load support for Nagios.

%package log
Summary: Nagios Plugin - check_log
Requires: nagios-plugins = %{version}-%{release}
Requires: grep
Requires: coreutils

%description log
Provides check_log support for Nagios.

%package mailq
Summary: Nagios Plugin - check_mailq
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/mailq

%description mailq
Provides check_mailq support for Nagios.

%package mrtg
Summary: Nagios Plugin - check_mrtg
Requires: nagios-plugins = %{version}-%{release}

%description mrtg
Provides check_mrtg support for Nagios.

%package mrtgtraf
Summary: Nagios Plugin - check_mrtgtraf
Requires: nagios-plugins = %{version}-%{release}

%description mrtgtraf
Provides check_mrtgtraf support for Nagios.

%package mysql
Summary: Nagios Plugin - check_mysql
Requires: nagios-plugins = %{version}-%{release}
Requires: openssl

%description mysql
Provides check_mysql and check_mysql_query support for Nagios.

%package nagios
Summary: Nagios Plugin - check_nagios
Requires: nagios-plugins = %{version}-%{release}

%description nagios
Provides check_nagios support for Nagios.

%package nt
Summary: Nagios Plugin - check_nt
Requires: nagios-plugins = %{version}-%{release}

%description nt
Provides check_nt support for Nagios.

%package ntp
Summary: Nagios Plugin - check_ntp
Requires: nagios-plugins = %{version}-%{release}

%description ntp
Provides check_ntp support for Nagios.

%if 0%{?fedora}
%package ntp-perl
Summary: Nagios Plugin - check_ntp.pl
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_sbindir}/ntpdate
Requires: %{_sbindir}/ntpq

%description ntp-perl
Provides check_ntp.pl support for Nagios.
%endif

%package nwstat
Summary: Nagios Plugin - check_nwstat
Requires: nagios-plugins = %{version}-%{release}

%description nwstat
Provides check_nwstat support for Nagios.

%package oracle
Summary: Nagios Plugin - check_oracle
Requires: nagios-plugins = %{version}-%{release}

%description oracle
Provides check_oracle support for Nagios.

%package overcr
Summary: Nagios Plugin - check_overcr
Requires: nagios-plugins = %{version}-%{release}

%description overcr
Provides check_overcr support for Nagios.

%package perl
Summary: Nagios plugins perl dep.
Requires: nagios-plugins = %{version}-%{release}

%description perl
Perl dep for nagios plugins.  This is *NOT* an actual plugin it simply provides
utils.pm

%package pgsql
Summary: Nagios Plugin - check_pgsql
Requires: nagios-plugins = %{version}-%{release}

%description pgsql
Provides check_pgsql (PostgreSQL)  support for Nagios.

%package ping
Summary: Nagios Plugin - check_ping
Requires: nagios-plugins = %{version}-%{release}
Requires: iputils
Requires: iputils

%description ping
Provides check_ping support for Nagios.

%package procs
Summary: Nagios Plugin - check_procs
Requires: nagios-plugins = %{version}-%{release}

%description procs
Provides check_procs support for Nagios.

%if %{with radius}
%package radius
Summary: Nagios Plugin - check_radius
Requires: nagios-plugins = %{version}-%{release}

%description radius
Provides check_radius support for Nagios.
%endif

%package real
Summary: Nagios Plugin - check_real
Requires: nagios-plugins = %{version}-%{release}

%description real
Provides check_real (rtsp) support for Nagios.

%package remove_perfdata
Summary: Nagios plugin tool to remove perf data
Requires: nagios-plugins = %{version}-%{release}

%description remove_perfdata
Removes perfdata from specified plugin's output

%package rpc
Summary: Nagios Plugin - check_rpc
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_sbindir}/rpcinfo

%description rpc
Provides check_rpc support for Nagios.

%ifnarch ppc ppc64 sparc sparc64
%package sensors
Summary: Nagios Plugin - check_sensors
Requires: nagios-plugins = %{version}-%{release}
Requires: grep
Requires: %{_bindir}/sensors

%description sensors
Provides check_sensors support for Nagios.
%endif

%package smtp
Summary: Nagios Plugin - check_smtp
Requires: nagios-plugins = %{version}-%{release}
Requires: openssl

%description smtp
Provides check_smtp support for Nagios.

%package snmp
Summary: Nagios Plugin - check_snmp
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/snmpgetnext
Requires: %{_bindir}/snmpget

%description snmp
Provides check_snmp support for Nagios.

%package ssh
Summary: Nagios Plugin - check_ssh
Requires: nagios-plugins = %{version}-%{release}

%description ssh
Provides check_ssh support for Nagios.

%package ssl_validity
Summary: Nagios Plugin - check_ssl_validity
Requires: nagios-plugins = %{version}-%{release}
Requires: perl(Crypt::X509)
Requires: perl(Date::Parse)
Requires: perl(LWP::Simple)
Requires: perl(Text::Glob)
Requires: openssl

%description ssl_validity
Provides check_ssl_validity support for Nagios.

%package swap
Summary: Nagios Plugin - check_swap
Requires: nagios-plugins = %{version}-%{release}

%description swap
Provides check_swap support for Nagios.

%package tcp
Summary: Nagios Plugin - check_tcp
Requires: nagios-plugins = %{version}-%{release}
Provides: nagios-plugins-ftp = %{version}-%{release}
Provides: nagios-plugins-imap = %{version}-%{release}
Provides: nagios-plugins-jabber = %{version}-%{release}
Provides: nagios-plugins-nntp = %{version}-%{release}
Provides: nagios-plugins-nntps = %{version}-%{release}
Provides: nagios-plugins-pop = %{version}-%{release}
Provides: nagios-plugins-simap = %{version}-%{release}
Provides: nagios-plugins-spop = %{version}-%{release}
Provides: nagios-plugins-ssmtp = %{version}-%{release}
Provides: nagios-plugins-udp = %{version}-%{release}
Provides: nagios-plugins-udp2 = %{version}-%{release}
Obsoletes: nagios-plugins-udp < 1.4.15-2
Requires: openssl

%description tcp
Provides check_tcp, check_ftp, check_imap, check_jabber, check_nntp,
check_nntps, check_pop, check_simap, check_spop, check_ssmtp, check_udp
and check_clamd support for Nagios.

%package time
Summary: Nagios Plugin - check_time
Requires: nagios-plugins = %{version}-%{release}

%description time
Provides check_time support for Nagios.

%package ups
Summary: Nagios Plugin - check_ups
Requires: nagios-plugins = %{version}-%{release}

%description ups
Provides check_ups support for Nagios.

%package uptime
Summary: Nagios Plugin - check_uptime
Requires: nagios-plugins = %{version}-%{release}

%description uptime
Provides check_uptime support for Nagios.

%package users
Summary: Nagios Plugin - check_users
Requires: nagios-plugins = %{version}-%{release}

%description users
Provides check_users support for Nagios.

%package wave
Summary: Nagios Plugin - check_wave
Requires: nagios-plugins = %{version}-%{release}

%description wave
Provides check_wave support for Nagios.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?fromgit}
%autosetup -n %{name}-%{commit} -N
%else
%autosetup -n %{name}-%{version} -N
%endif

%patch -P 1 -p1 -b .ntpsec-support.patch
%patch -P 2 -p1 -b .remove_ntp_jitter
%patch -P 7 -p1 -b .fix_ntpcommands
%if 0%{?bootstrap} == 0
%patch -P 12 -p1 -b .fix_perl_ntp
%endif

%build

%if 0%{?fromgit}
./tools/setup
%endif
%configure \
	--libexecdir=%{_libdir}/nagios/plugins \
%if %{with libdbi}
	--with-dbi \
%endif
	--with-mysql \
	PATH_TO_SUDO=%{_bindir}/sudo \
	PATH_TO_QSTAT=%{_bindir}/quakestat \
	PATH_TO_FPING=%{_sbindir}/fping \
%if 0%{?fedora}
	PATH_TO_NTPQ=%{_sbindir}/ntpq \
	PATH_TO_NTPDC=%{_sbindir}/ntpdc \
	PATH_TO_NTPDATE=%{_sbindir}/ntpdate \
%endif
	PATH_TO_RPCINFO=%{_sbindir}/rpcinfo \
	--with-ps-command="`which ps` -eo 's uid pid ppid vsz rss pcpu etime comm args'" \
	--with-ps-format='%s %d %d %d %d %d %f %s %s %n' \
	--with-ps-cols=10 \
	--with-ping-command='%{_bindir}/ping -4 -n -U -w %d -c %d %s' \
	--with-ping6-command='%{_sbindir}/ping6 -n -U -w %d -c %d %s' \
	--enable-extra-opts \
	--with-ps-varlist='procstat,&procuid,&procpid,&procppid,&procvsz,&procrss,&procpcpu,procetime,procprog,&pos'

%make_build

%if 0%{?fromgit}
make THANKS
%endif

cd plugins-scripts
%make_build check_ntp
cd ..

cp %{SOURCE1} ./README.Fedora

%install
sed -i 's,^MKINSTALLDIRS.*,MKINSTALLDIRS = ../mkinstalldirs,' po/Makefile
%make_install AM_INSTALL_PROGRAM_FLAGS=""
install -m 0755 plugins-root/check_icmp %{buildroot}/%{_libdir}/nagios/plugins
install -m 0755 plugins-root/check_dhcp %{buildroot}/%{_libdir}/nagios/plugins
install -m 0755 plugins/check_ide_smart %{buildroot}/%{_libdir}/nagios/plugins
install -m 0755 plugins/check_ldap %{buildroot}/%{_libdir}/nagios/plugins
%if 0%{?fedora}
install -m 0755 plugins-scripts/check_ntp %{buildroot}/%{_libdir}/nagios/plugins/check_ntp.pl
%endif
## This is to fix https://bugzilla.redhat.com/show_bug.cgi?id=1664981 because they are installing the wrong thing
install -m 0755 plugins/check_ntp %{buildroot}/%{_libdir}/nagios/plugins/check_ntp
%if %{with radius}
install -m 0755 plugins/check_radius %{buildroot}/%{_libdir}/nagios/plugins
%endif
install -m 0755 plugins/check_pgsql %{buildroot}/%{_libdir}/nagios/plugins

%ifarch ppc ppc64 ppc64p7 sparc sparc64
rm -f %{buildroot}/%{_libdir}/nagios/plugins/check_sensors
%endif

chmod 644 %{buildroot}/%{_libdir}/nagios/plugins/utils.pm

%find_lang %{name}

%files -f %{name}.lang
%doc ACKNOWLEDGEMENTS AUTHORS po/ChangeLog CODING FAQ LEGAL NEWS README REQUIREMENTS SUPPORT THANKS README.Fedora
%license COPYING
%{_libdir}/nagios/plugins/negate
%{_libdir}/nagios/plugins/urlize
%{_libdir}/nagios/plugins/utils.sh

%files all

%files apt
%{_libdir}/nagios/plugins/check_apt

%files breeze
%{_libdir}/nagios/plugins/check_breeze

%files by_ssh
%{_libdir}/nagios/plugins/check_by_ssh

%files cluster
%{_libdir}/nagios/plugins/check_cluster

%if %{with libdbi}
%files dbi
%{_libdir}/nagios/plugins/check_dbi
%endif

%files dhcp
%defattr(4750,root,nagios,-)
%{_libdir}/nagios/plugins/check_dhcp

%files dig
%{_libdir}/nagios/plugins/check_dig

%files disk
%{_libdir}/nagios/plugins/check_disk

%files disk_smb
%{_libdir}/nagios/plugins/check_disk_smb

%files dns
%{_libdir}/nagios/plugins/check_dns

%files dummy
%{_libdir}/nagios/plugins/check_dummy

%files file_age
%{_libdir}/nagios/plugins/check_file_age

%files flexlm
%{_libdir}/nagios/plugins/check_flexlm

%files fping
%defattr(4750,root,nagios,-)
%{_libdir}/nagios/plugins/check_fping

%files game
%{_libdir}/nagios/plugins/check_game

%files hpjd
%{_libdir}/nagios/plugins/check_hpjd

%files http
%{_libdir}/nagios/plugins/check_http

%files icmp
%defattr(4750,root,nagios,-)
%{_libdir}/nagios/plugins/check_icmp

%files ifoperstatus
%{_libdir}/nagios/plugins/check_ifoperstatus

%files ifstatus
%{_libdir}/nagios/plugins/check_ifstatus

%files ide_smart
%defattr(4750,root,nagios,-)
%{_libdir}/nagios/plugins/check_ide_smart

%files ircd
%{_libdir}/nagios/plugins/check_ircd

%files ldap
%{_libdir}/nagios/plugins/check_ldap
%{_libdir}/nagios/plugins/check_ldaps

%files load
%{_libdir}/nagios/plugins/check_load

%files log
%{_libdir}/nagios/plugins/check_log

%files mailq
%{_libdir}/nagios/plugins/check_mailq

%files mrtg
%{_libdir}/nagios/plugins/check_mrtg

%files mrtgtraf
%{_libdir}/nagios/plugins/check_mrtgtraf

%files mysql
%{_libdir}/nagios/plugins/check_mysql
%{_libdir}/nagios/plugins/check_mysql_query

%files nagios
%{_libdir}/nagios/plugins/check_nagios

%files nt
%{_libdir}/nagios/plugins/check_nt

%files ntp
%{_libdir}/nagios/plugins/check_ntp
%{_libdir}/nagios/plugins/check_ntp_peer
%{_libdir}/nagios/plugins/check_ntp_time

%if 0%{?fedora}
%files ntp-perl
%{_libdir}/nagios/plugins/check_ntp.pl
%endif

%files nwstat
%{_libdir}/nagios/plugins/check_nwstat

%files oracle
%{_libdir}/nagios/plugins/check_oracle

%files overcr
%{_libdir}/nagios/plugins/check_overcr

%files perl
%{_libdir}/nagios/plugins/utils.pm

%files pgsql
%{_libdir}/nagios/plugins/check_pgsql

%files ping
%{_libdir}/nagios/plugins/check_ping

%files procs
%{_libdir}/nagios/plugins/check_procs

%if %{with radius}
%files radius
%{_libdir}/nagios/plugins/check_radius
%endif

%files real
%{_libdir}/nagios/plugins/check_real

%files remove_perfdata
%{_libdir}/nagios/plugins/remove_perfdata

%files rpc
%{_libdir}/nagios/plugins/check_rpc

%ifnarch ppc ppc64 ppc64p7 sparc sparc64
%files sensors
%{_libdir}/nagios/plugins/check_sensors
%endif

%files smtp
%{_libdir}/nagios/plugins/check_smtp

%files snmp
%{_libdir}/nagios/plugins/check_snmp

%files ssh
%{_libdir}/nagios/plugins/check_ssh

%files ssl_validity
%{_libdir}/nagios/plugins/check_ssl_validity

%files swap
%{_libdir}/nagios/plugins/check_swap

%files tcp
%{_libdir}/nagios/plugins/check_clamd
%{_libdir}/nagios/plugins/check_ftp
%{_libdir}/nagios/plugins/check_imap
%{_libdir}/nagios/plugins/check_jabber
%{_libdir}/nagios/plugins/check_nntp
%{_libdir}/nagios/plugins/check_nntps
%{_libdir}/nagios/plugins/check_pop
%{_libdir}/nagios/plugins/check_simap
%{_libdir}/nagios/plugins/check_spop
%{_libdir}/nagios/plugins/check_ssmtp
%{_libdir}/nagios/plugins/check_tcp
%{_libdir}/nagios/plugins/check_udp

%files time
%{_libdir}/nagios/plugins/check_time

%files ups
%{_libdir}/nagios/plugins/check_ups

%files uptime
%{_libdir}/nagios/plugins/check_uptime

%files users
%{_libdir}/nagios/plugins/check_users

%files wave
%{_libdir}/nagios/plugins/check_wave

%changelog
%autochangelog
