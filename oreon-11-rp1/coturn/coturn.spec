%global source0_hash e01c0701792231d67768e0e314ebad6395501759ea56772dc7e36d3badec5549

Name:           coturn
Version:        4.9.0
Release:        1%{?dist}
Summary:        TURN/STUN & ICE Server
# MIT (src/{apps/relay/acme.c,server/ns_turn_khash.h} and BSD-3-Clause (the rest)
License:        BSD-3-Clause AND MIT
URL:            https://github.com/coturn/coturn/
Source0:        https://github.com/coturn/coturn/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        coturn.service
Source2:        coturn.tmpfilesd
Source3:        coturn.logrotate
Source4:        coturn.sysusersd
Patch0:         coturn-4.9.0-openssl-1.1.patch
BuildRequires:  gcc
BuildRequires:  hiredis-devel
BuildRequires:  libevent-devel >= 2.0.0
BuildRequires:  libpq-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  openssl-devel >= 3
%else
BuildRequires:  openssl-devel >= 1.1.1
%endif
BuildRequires:  sqlite-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
Recommends:     perl-interpreter
Recommends:     perl(DBI)
Recommends:     perl(HTTP::Request::Common)
Recommends:     perl(strict)
Recommends:     perl(warnings)
Recommends:     telnet
Provides:       turnserver = %{version}
%{?systemd_requires}
%{?sysusers_requires_compat}

%description
The Coturn TURN Server is a VoIP media traffic NAT traversal server and gateway.
It can be used as a general-purpose network traffic TURN server/gateway, too.

This implementation also includes some extra features. Supported RFCs:

TURN specs:
- RFC 5766 - base TURN specs
- RFC 6062 - TCP relaying TURN extension
- RFC 6156 - IPv6 extension for TURN
- Experimental DTLS support as client protocol.

STUN specs:
- RFC 3489 - "classic" STUN
- RFC 5389 - base "new" STUN specs
- RFC 5769 - test vectors for STUN protocol testing
- RFC 5780 - NAT behavior discovery support

The implementation fully supports the following client-to-TURN-server protocols:
- UDP (per RFC 5766)
- TCP (per RFC 5766 and RFC 6062)
- TLS (per RFC 5766 and RFC 6062); TLS1.0/TLS1.1/TLS1.2
- DTLS (experimental non-standard feature)

Supported relay protocols:
- UDP (per RFC 5766)
- TCP (per RFC 6062)

Supported user databases (for user repository, with passwords or keys, if
authentication is required):
- SQLite
- MySQL
- PostgreSQL
- Redis

Redis can also be used for status and statistics storage and notification.

Supported TURN authentication mechanisms:
- long-term
- TURN REST API (a modification of the long-term mechanism, for time-limited
  secret-based authentication, for WebRTC applications)

The load balancing can be implemented with the following tools (either one or a
combination of them):
- network load-balancer server
- DNS-based load balancing
- built-in ALTERNATE-SERVER mechanism.

%package utils
Summary:        Coturn utils

%description utils
This package contains the TURN client utils.

%package client-libs
Summary:        TURN client static library

%description client-libs
This package contains the TURN client static library.

%package client-devel
Summary:        Coturn client development headers

%description client-devel
This package contains the TURN client development headers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Use Fedora Default Ciphers
sed -i \
    -e 's|#define DEFAULT_CIPHER_LIST "DEFAULT"|#define DEFAULT_CIPHER_LIST "PROFILE=SYSTEM"|g' \
    src/apps/relay/mainrelay.h
sed -i \
    -e 's|*csuite = "ALL"; //"AES256-SHA" "DH"|*csuite = "PROFILE=SYSTEM"; // Fedora Defaults|g' \
    src/apps/uclient/mainuclient.c

%build
%configure \
    --confdir=%{_sysconfdir}/%{name} \
    --examplesdir=%{_docdir}/%{name} \
    --schemadir=%{_datadir}/%{name} \
    --manprefix=%{_datadir} \
    --docdir=%{_docdir}/%{name} \
    --turndbdir=%{_localstatedir}/lib/%{name} \
    --disable-rpath
%make_build

%install
%make_install
mkdir -p %{buildroot}{%{_sysconfdir}/pki/coturn/{public,private},{%{_rundir},%{_localstatedir}/{lib,log}}/%{name}}
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/coturn.service
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/coturn.conf
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/coturn.conf
sed -i \
    -e "s|^syslog$|#syslog|g" \
    -e "s|^#*log-file=.*|log-file=/var/log/coturn/turnserver.log|g" \
    -e "s|^#*simple-log|simple-log|g" \
    -e "s|^#*cert=.*|#cert=/etc/pki/coturn/public/turn_server_cert.pem|g" \
    -e "s|^#*pkey=.*|#pkey=/etc/pki/coturn/private/turn_server_pkey.pem|g" \
    %{buildroot}%{_sysconfdir}/%{name}/turnserver.conf.default
touch -c -r examples/etc/turnserver.conf %{buildroot}%{_sysconfdir}/%{name}/turnserver.conf.default
mv -f %{buildroot}%{_sysconfdir}/%{name}/turnserver.conf{.default,}

# Remove generated SQLite database, certificate and key
rm -f %{buildroot}%{_localstatedir}/lib/%{name}/turndb
rm -f %{buildroot}%{_docdir}/%{name}/etc/{cacert,turn_{client,server}_{cert,pkey}}.pem
rm -f %{buildroot}%{_docdir}/%{name}/etc/coturn.service

%check
make test

# Check if turnserver is really linked against MariaDB, PostgreSQL and systemd,
# because ./configure unfortunately has no proper failure mechanism...
ldd %{buildroot}%{_bindir}/turnserver | grep -q libmariadb.so
ldd %{buildroot}%{_bindir}/turnserver | grep -q libpq.so
ldd %{buildroot}%{_bindir}/turnserver | grep -q libsystemd.so

%pre
%sysusers_create_compat %{SOURCE4}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%{_bindir}/turnserver
%{_bindir}/turnadmin
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*.redis
%{_datadir}/%{name}/*.sql
%{_datadir}/%{name}/*.sh
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/README.*
%exclude %{_docdir}/%{name}/README.turnutils
%exclude %{_docdir}/%{name}/INSTALL
%exclude %{_docdir}/%{name}/LICENSE
%exclude %{_docdir}/%{name}/postinstall.txt
%dir %{_docdir}/%{name}/etc/
%doc %{_docdir}/%{name}/etc/turnserver.conf
%dir %{_docdir}/%{name}/scripts/
%dir %{_docdir}/%{name}/scripts/*/
%{_docdir}/%{name}/scripts/*.sh
%{_docdir}/%{name}/scripts/readme.txt
%doc %{_docdir}/%{name}/scripts/*/*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/turnserver.1.*
%{_mandir}/man1/turnadmin.1.*
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/turnserver.conf
%dir %{_sysconfdir}/pki/%{name}/
%dir %{_sysconfdir}/pki/%{name}/public/
%dir %attr(0750,root,%{name}) %{_sysconfdir}/pki/%{name}/private/
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}.conf
%dir %attr(0750,%{name},%{name}) %{_rundir}/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}/
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%files utils
%license LICENSE
%{_bindir}/turnutils_peer
%{_bindir}/turnutils_stunclient
%{_bindir}/turnutils_uclient
%{_bindir}/turnutils_oauth
%{_bindir}/turnutils_natdiscovery
%doc %{_docdir}/%{name}/README.turnutils
%{_mandir}/man1/turnutils.1.*
%{_mandir}/man1/turnutils_*.1.*

%files client-libs
%license LICENSE
%{_libdir}/libturnclient.a

%files client-devel
%license LICENSE
%dir %{_includedir}/turn/
%{_includedir}/turn/*.h
%dir %{_includedir}/turn/client/
%{_includedir}/turn/client/*

%changelog
%autochangelog
