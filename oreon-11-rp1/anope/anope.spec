%global source0_hash fb9fba0d331aced342a8bb79a2c898633442d45f6f837f601f48d11a2784e68d

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
Version:        2.1.4
Release:        6%{?dist}
# Anope itself is GPL-2.0-only but uses other source codes, breakdown:
# BSD-3-Clause: include/pstdint.h and modules/encryption/enc_sha256.cpp
# MIT: src/siphash.cpp
# LicenseRef-Fedora-Public-Domain: modules/encryption/enc_bcrypt.cpp
# LicenseRef-RSA: modules/encryption/enc_md5.cpp
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
BuildRequires:  cmake
%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires:  cmake3
# Compiler with C++17 language, filesystem headers and linking support
BuildRequires:  devtoolset-12-toolchain
%endif
%if 0%{?rhel} == 8
# Compiler with C++17 filesystem headers and linking support
BuildRequires:  gcc-toolset-12
%endif
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  systemd-rpm-macros
%if 0%{?fedora} || 0%{?rhel} > 7
Recommends:     %{_sbindir}/sendmail
%else
Requires:       %{_sbindir}/sendmail
%endif
Provides:       %{name}-redis = %{version}-%{release}
Provides:       %{name}-redis%{?_isa} = %{version}-%{release}
%{?systemd_requires}
%{?sysusers_requires_compat}

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
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  mariadb-connector-c-devel
%else
BuildRequires:  mariadb-devel >= 5.5
%endif
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
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  openssl-devel
%else
BuildRequires:  openssl11-devel
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description openssl
Anope is a set of IRC services designed for flexibility and ease of use.

This package provides an Anope module using OpenSSL to e.g. connect to the
uplink server(s) via SSL/TLS.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%if 0%{?rhel} && 0%{?rhel} < 8
%global cmake %cmake3
%global cmake_build %cmake3_build
%global cmake_install %cmake3_install

%if %{with mysql}
EXTRA_LIBS+=";%{_libdir}/mysql"
%endif

%if %{with openssl}
EXTRA_INCLUDE+=";%{_includedir}/openssl11"
EXTRA_LIBS+=";%{_libdir}/openssl11"
%endif

. /opt/rh/devtoolset-12/enable
%endif
%if 0%{?rhel} == 8
. /opt/rh/gcc-toolset-12/enable
%endif

# Build extra modules
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

# Remove crontab script (pseudo init script) for anope
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/example.chk

# Remove webcpanel, doesn't seem to be widely used
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/webcpanel.so
rm -rf $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}/webcpanel/

# Remove MySQL related modules when built without MySQL
%{!?with_mysql:rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/{chanstats,cs_fantasy_stats,cs_fantasy_top,irc2sql}.so}

%find_lang %{name}

%pre
%sysusers_create_compat %{SOURCE3}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files -f %{name}.lang
%license docs/COPYING
%doc docs/Changes docs/Changes.conf docs/DEFCON
%doc docs/FAQ docs/MODULES docs/README docs/XMLRPC
%doc %{_pkgdocdir}/examples/
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/*.conf
%if %{with mysql}
%exclude %{_sysconfdir}/%{name}/chanstats.conf
%exclude %{_sysconfdir}/%{name}/irc2sql.conf
%endif
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/motd
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_sbindir}/%{name}
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/*.so
%if %{with ldap}
%exclude %{_libdir}/%{name}/ldap.so
%exclude %{_libdir}/%{name}/ldap_authentication.so
%exclude %{_libdir}/%{name}/ldap_oper.so
%endif
%if %{with mysql}
%exclude %{_libdir}/%{name}/mysql.so
%exclude %{_libdir}/%{name}/chanstats.so
%exclude %{_libdir}/%{name}/cs_fantasy_stats.so
%exclude %{_libdir}/%{name}/cs_fantasy_top.so
%exclude %{_libdir}/%{name}/irc2sql.so
%endif
%{?with_pcre2:%exclude %{_libdir}/%{name}/regex_pcre2.so}
%{?with_tre:%exclude %{_libdir}/%{name}/regex_tre.so}
%{?with_sqlite:%exclude %{_libdir}/%{name}/sqlite.so}
%{?with_gnutls:%exclude %{_libdir}/%{name}/ssl_gnutls.so}
%{?with_openssl:%exclude %{_libdir}/%{name}/ssl_openssl.so}
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/backups/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}/
%dir %attr(0755,%{name},%{name}) %{_rundir}/%{name}/

%if %{with ldap}
%files ldap
%{_libdir}/%{name}/ldap.so
%{_libdir}/%{name}/ldap_authentication.so
%{_libdir}/%{name}/ldap_oper.so
%endif

%if %{with mysql}
%files mysql
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/chanstats.conf
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/irc2sql.conf
%{_libdir}/%{name}/mysql.so
%{_libdir}/%{name}/chanstats.so
%{_libdir}/%{name}/cs_fantasy_stats.so
%{_libdir}/%{name}/cs_fantasy_top.so
%{_libdir}/%{name}/irc2sql.so
%endif

%if %{with pcre2}
%files pcre2
%{_libdir}/%{name}/regex_pcre2.so
%endif

%if %{with tre}
%files tre
%{_libdir}/%{name}/regex_tre.so
%endif

%if %{with sqlite}
%files sqlite
%{_libdir}/%{name}/sqlite.so
%endif

%if %{with gnutls}
%files gnutls
%{_libdir}/%{name}/ssl_gnutls.so
%endif

%if %{with openssl}
%files openssl
%{_libdir}/%{name}/ssl_openssl.so
%endif

%changelog
%autochangelog
