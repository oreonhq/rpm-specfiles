%global source0_hash 1d23cfac659b4469aa0b64f0022a7c48150287049c33f60fde88b7e55b95726a
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}}
%bcond_without  ldap
%bcond_without  mysql
%bcond_without  pcre2
%bcond_without  tre
%bcond_without  sqlite
%bcond_without  gnutls
%bcond_without  openssl
Summary:        IRC services designed for flexibility and ease of use
Name:           anope
Version:        2.1.27
Release:        1%{?dist}
License:        GPL-2.0-only AND BSD-3-Clause AND MIT AND LicenseRef-Fedora-Public-Domain AND LicenseRef-RSA
URL:            https://www.anope.org/
Source0:        https://github.com/anope/anope/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        anope.service
Source2:        anope.tmpfilesd
Source3:        anope.sysusersd
Source10:       anope.conf
Source11:       anope.motd
Source12:       anope-botserv.conf
Source13:       anope-chanserv.conf
Source14:       anope-chanstats.conf
Source15:       anope-global.conf
Source16:       anope-hostserv.conf
Source17:       anope-irc2sql.conf
Source18:       anope-memoserv.conf
Source19:       anope-modules.conf
Source20:       anope-nickserv.conf
Source21:       anope-operserv.conf
Patch0:         https://github.com/anope/anope/commit/87a8af0ad71a11c248ba94c9ba20668dcb0fe831.patch#/anope-2.1.4-paths1.patch
Patch1:         https://github.com/anope/anope/commit/c08aaa86d1ada72ad6e185837f9c179693b60c22.patch#/anope-2.1.4-paths2.patch
Patch2:         https://github.com/anope/anope/commit/5fdc6373275de9c0844c6507509c153ce69fa0c1.patch#/anope-2.1.4-paths3.patch
Requires:       %{_sbindir}/sendmail
Provides:       %{name}-redis = %{version}-%{release}
Provides:       %{name}-redis%{?_isa} = %{version}-%{release}
%{?systemd_requires}
%{?sysusers_requires_compat}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gnutls-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tre-devel
# /oreon:deps
%description
Anope is a set of IRC services forked from Epona early 2003 to pick up where
Epona had been abandoned. It offers various services clients to maintain an
IRC network: NickServ, ChanServ, MemoServ, OperServ, BotServ and HostServ as
well as less often used services clients like HelpServ, DevNull and Global.

%if %{with ldap}
%package ldap
Summary:        LDAP modules for Anope IRC services
BuildRequires:  openldap-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description ldap
Anope is a set of IRC services designed for flexibility and ease of use.

This package provides Anope modules to enable IRC commands such as IDENTIFY,
RELEASE, RECOVER, GHOST, etc. to use LDAP to authenticate users. It provides
a module to tie users to Anope opertypes when they identify via LDAP group
membership, too.
%endif

%if %{with mysql}
%package mysql
Summary:        MariaDB/MySQL modules for Anope IRC services
BuildRequires:  mariadb-devel >= 5.5
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-mariadb = %{version}-%{release}
Provides:       %{name}-mariadb%{?_isa} = %{version}-%{release}
%description mysql
Anope is a set of IRC services designed for flexibility and ease of use.

This package provides Anope modules to store services data in a MariaDB or
MySQL database and uses that for maintaining the IRC services. It provides
further modules for IRC channel statistics or to log the IRC services' logs
into a MariaDB or MySQL database.
%endif

%if %{with pcre2}
%package pcre2
Summary:        PCRE regular expression module Anope IRC services
BuildRequires:  pcre2-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-pcre = %{version}-%{release}
Obsoletes:      %{name}-pcre < 2.0.12-1
%description pcre2
Anope is a set of IRC services designed for flexibility and ease of use.

This package provides an Anope module to support regular expressions using
the Perl Compatible Regular Expressions (PCRE) library in version 2.
%endif

%if %{with tre}
%package tre
Summary:        TRE regular expression module Anope IRC services
BuildRequires:  tre-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tre
Anope is a set of IRC services designed for flexibility and ease of use.

This package provides an Anope module to support regular expressions using
the TRE library.
%endif

%if %{with sqlite}
%package sqlite
Summary:        SQLite module for Anope IRC services
BuildRequires:  sqlite-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description sqlite
Anope is a set of IRC services designed for flexibility and ease of use.

This package provides an Anope module to support SQLite databases for e.g.
authenticating IRC users against a SQLite database using a custom query.
%endif

%if %{with gnutls}
%package gnutls
Summary:        GnuTLS module for Anope IRC services
BuildRequires:  gnutls-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description gnutls
Anope is a set of IRC services designed for flexibility and ease of use.

This package provides an Anope module using GnuTLS to e.g. connect to the
uplink server(s) via SSL/TLS.
%endif

%if %{with openssl}
%package openssl
Summary:        OpenSSL module for Anope IRC services
BuildRequires:  openssl11-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description openssl
Anope is a set of IRC services designed for flexibility and ease of use.

This package provides an Anope module using OpenSSL to e.g. connect to the
uplink server(s) via SSL/TLS.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if %{with mysql}
%endif
%if %{with openssl}
%endif
mv -f modules/extra/regex_posix.cpp modules/
%{?with_ldap:mv -f modules/extra/ldap.cpp modules/}
%{?with_mysql:mv -f modules/extra/mysql.cpp modules/}
%{?with_pcre2:mv -f modules/extra/regex_pcre2.cpp modules/}
%{?with_tre:mv -f modules/extra/regex_tre.cpp modules/}
%{?with_sqlite:mv -f modules/extra/sqlite.cpp modules/}
%{?with_gnutls:mv -f modules/extra/ssl_gnutls.cpp modules/}
%{?with_openssl:mv -f modules/extra/ssl_openssl.cpp modules/}
%cmake \
  -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
  -DBIN_DIR:STRING=%{_sbindir} \
  -DDATA_DIR:STRING=%{_localstatedir}/lib/%{name} \
  -DCONF_DIR:STRING=%{_sysconfdir}/%{name} \
  -DMODULE_DIR:STRING=%{_libdir}/%{name} \
  -DLOCALE_DIR:STRING=%{_datadir}/locale \
  -DLOG_DIR:STRING=%{_localstatedir}/log/%{name} \
  -DPROGRAM_NAME:STRING=%{name} \
  -DREPRODUCIBLE_BUILD:BOOL=ON \
  -DDISABLE_TOOLS:BOOL=ON \
  -DDEFUMASK:STRING=027 \
  -DEXTRA_INCLUDE=$EXTRA_INCLUDE \
  -DEXTRA_LIBS:STRING=$EXTRA_LIBS
%cmake_build
%install
%cmake_install
mkdir -p $RPM_BUILD_ROOT{%{_rundir}/%{name},%{_pkgdocdir}/examples}/
mv -f $RPM_BUILD_ROOT{%{_sysconfdir}/%{name}/*.conf,%{_pkgdocdir}/examples/}
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
install -D -p -m 0640 %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.conf
install -D -p -m 0640 %{SOURCE11} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/motd
install -D -p -m 0640 %{SOURCE12} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/botserv.conf
install -D -p -m 0640 %{SOURCE13} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/chanserv.conf
install -D -p -m 0640 %{SOURCE14} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/chanstats.conf
install -D -p -m 0640 %{SOURCE15} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/global.conf
install -D -p -m 0640 %{SOURCE16} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/hostserv.conf
install -D -p -m 0640 %{SOURCE17} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/irc2sql.conf
install -D -p -m 0640 %{SOURCE18} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/memoserv.conf
install -D -p -m 0640 %{SOURCE19} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/modules.conf
install -D -p -m 0640 %{SOURCE20} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/nickserv.conf
install -D -p -m 0640 %{SOURCE21} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/operserv.conf
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/example.chk
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/webcpanel.so
rm -rf $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}/webcpanel/
%{!?with_mysql:rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/{chanstats,cs_fantasy_stats,cs_fantasy_top,irc2sql}.so}
%find_lang %{name}
%oreon_autofiles anope-ldap usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles anope-mysql usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles anope-pcre2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles anope-tre usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles anope-sqlite usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles anope-gnutls usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles anope-openssl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

%sysusers_create_compat %{SOURCE3}
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n anope-ldap -f %{oreon_filedir}/anope-ldap.list
%files -n anope-mysql -f %{oreon_filedir}/anope-mysql.list
%files -n anope-pcre2 -f %{oreon_filedir}/anope-pcre2.list
%files -n anope-tre -f %{oreon_filedir}/anope-tre.list
%files -n anope-sqlite -f %{oreon_filedir}/anope-sqlite.list
%files -n anope-gnutls -f %{oreon_filedir}/anope-gnutls.list
%files -n anope-openssl -f %{oreon_filedir}/anope-openssl.list

%changelog

%autochangelog
