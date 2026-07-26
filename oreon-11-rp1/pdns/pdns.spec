%global source0_hash d360e1fa127a562a4ad0ff648aef56af76b678311c6553a7f7034677438a085d

%global _hardened_build 1
%global backends %{nil}

Name: pdns
Version: 5.0.2
Release: 3%{?dist}
Summary: A modern, advanced and high performance authoritative-only name server
License: GPL-2.0-only
URL: http://powerdns.com
Source0: http://downloads.powerdns.com/releases/%{name}-%{version}.tar.bz2
ExcludeArch: %{arm} %{ix86}

%if 0%{?rhel}
Requires(pre): shadow-utils
%endif
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

BuildRequires: chrpath
BuildRequires: make
BuildRequires: bison
BuildRequires: boost-devel
BuildRequires: gcc-c++
BuildRequires: krb5-devel
BuildRequires: libcurl-devel
BuildRequires: libsodium-devel
%if 0%{?rhel} == 9
BuildRequires: lua-devel
%define lua_implementation lua
%else
%ifarch ppc64le riscv64
%define lua_implementation lua
BuildRequires: lua-devel
%else
BuildRequires: luajit-devel
%define lua_implementation luajit
%endif
%endif
%if 0%{?fedora} >= 41
BuildRequires: openssl-devel-engine
%else
BuildRequires: openssl-devel
%endif
BuildRequires: p11-kit-devel
BuildRequires: perl
BuildRequires: protobuf-compiler
BuildRequires: protobuf-devel
BuildRequires: libcurl-devel
BuildRequires: systemd
BuildRequires: systemd-devel
Provides: powerdns = %{version}-%{release}
%global backends %{backends} bind

%description
The PowerDNS Nameserver is a modern, advanced and high performance
authoritative-only name server. It is written from scratch and conforms
to all relevant DNS standards documents.
Furthermore, PowerDNS interfaces with almost any database.

%package tools
Summary: Extra tools for %{name}

%description tools
This package contains the extra tools for %{name}

%package backend-mysql
Summary: MySQL backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: mariadb-connector-c-devel openssl-devel
%global backends %{backends} gmysql

%description backend-mysql
This package contains the gmysql backend for %{name}

%package backend-postgresql
Summary: PostgreSQL backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libpq-devel
%global backends %{backends} gpgsql

%description backend-postgresql
This package contains the gpgsql backend for %{name}

%package backend-pipe
Summary: Pipe backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%global backends %{backends} pipe

%description backend-pipe
This package contains the pipe backend for %{name}

%package backend-remote
Summary: Remote backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%global backends %{backends} remote

%description backend-remote
This package contains the remote backend for %{name}

%package backend-ldap
Summary: LDAP backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: openldap-devel
%global backends %{backends} ldap

%description backend-ldap
This package contains the ldap backend for %{name}

%package backend-lmdb
Summary: LMDB backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: lmdb-devel
%global backends %{backends} lmdb

%description backend-lmdb
This package contains the lmdb backend for %{name}

%package backend-lua2
Summary: LUA2 backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%global backends %{backends} lua2

%description backend-lua2
This package contains the lua2 backend for %{name}

%package backend-sqlite
Summary: SQLite backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: sqlite-devel
%global backends %{backends} gsqlite3

%description backend-sqlite
This package contains the SQLite backend for %{name}

%package backend-tinydns
Summary: TinyDNS backend for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: tinycdb-devel
%global backends %{backends} tinydns

%description backend-tinydns
This package contains the TinyDNS backend for %{name}

%package ixfrdist
Summary: A program to redistribute zones over AXFR and IXFR
BuildRequires: yaml-cpp-devel

%description ixfrdist
This package contains the ixfrdist program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%if 0%{?fedora}
# Create a sysusers.d config file
cat >pdns.sysusers.conf <<EOF
u pdns - 'PowerDNS Authoritative Server' /var/lib/pdns -
EOF
%endif

%build
export CPPFLAGS="-DLDAP_DEPRECATED"

%configure \
	--enable-option-checking=fatal \
	--sysconfdir=%{_sysconfdir}/%{name} \
	--disable-static \
	--disable-dependency-tracking \
	--disable-silent-rules \
	--with-modules='' \
	--with-lua=%{lua_implementation} \
	--with-dynmodules='%{backends}' \
	--enable-tools \
	--with-libsodium \
	--enable-ixfrdist \
	--enable-unit-tests \
	--enable-lua-records \
	--enable-experimental-pkcs11 \
	--enable-dns-over-tls \
	--enable-systemd

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/dnsbulktest || :
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/dnspcap2calidns || :
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/dnspcap2protobuf || :
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/dnsreplay || :
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/dnsscope || :
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/dnstcpbench || :
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/dnswasher || :
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/ixfrdist || :
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/pdns_notify || :
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/pdnsutil || :
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/nproxy || :
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/calidns || :
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/pdns/liblmdbbackend.so || :

%{__rm} -f %{buildroot}%{_libdir}/%{name}/*.la
%{__mv} %{buildroot}%{_sysconfdir}/%{name}/pdns.conf{-dist,}

# rename zone2ldap to pdns-zone2ldap (#1193116)
%{__mv} %{buildroot}/%{_bindir}/zone2ldap %{buildroot}/%{_bindir}/pdns_zone2ldap
%{__mv} %{buildroot}/%{_mandir}/man1/zone2ldap.1 %{buildroot}/%{_mandir}/man1/pdns_zone2ldap.1

# change user/group to pdns
# change default backend to bind
sed -i \
    -e 's/# setuid=/setuid=pdns/' \
    -e 's/# setgid=/setgid=pdns/' \
    -e 's/# launch=/launch=bind/' \
    -e 's/# security-poll-suffix=secpoll\.powerdns\.com\./security-poll-suffix=/' \
    %{buildroot}%{_sysconfdir}/%{name}/pdns.conf

%{__rm} %{buildroot}/%{_bindir}/stubquery
%{__install} -d %{buildroot}/%{_sharedstatedir}/%{name}

%if 0%{?fedora}
install -m0644 -D pdns.sysusers.conf %{buildroot}%{_sysusersdir}/pdns.conf
%endif

%check
make %{?_smp_mflags} -C pdns check

%if 0%{?rhel}
%pre
getent group pdns >/dev/null || groupadd -r pdns
getent passwd pdns >/dev/null || \
	useradd -r -g pdns -d /var/lib/pdns -s /sbin/nologin \
	-c "PowerDNS Authoritative Server" pdns
%endif

%post
%systemd_post pdns.service

%preun
%systemd_preun pdns.service

%postun
%systemd_postun_with_restart pdns.service

%files
%doc README
%license COPYING
%{_bindir}/pdns_control
%{_bindir}/pdnsutil
%{_bindir}/pdns_zone2ldap
%{_bindir}/zone2sql
%{_bindir}/zone2json
%{_sbindir}/pdns_server
%{_mandir}/man1/pdns_control.1.gz
%{_mandir}/man1/pdns_server.1.gz
%{_mandir}/man1/zone2sql.1.gz
%{_mandir}/man1/zone2json.1.gz
%{_mandir}/man1/pdns_zone2ldap.1.gz
%{_mandir}/man1/pdnsutil.1.gz
%{_unitdir}/pdns.service
%{_unitdir}/pdns@.service
%{_libdir}/%{name}/libbindbackend.so
%dir %{_libdir}/%{name}/
%dir %attr(-,pdns,pdns) %{_sharedstatedir}/%{name}
%dir %attr(-,root,pdns) %{_sysconfdir}/%{name}/
%attr(0640,root,pdns) %config(noreplace) %{_sysconfdir}/%{name}/pdns.conf
%if 0%{?fedora}
%{_sysusersdir}/pdns.conf
%endif

%files tools
%{_bindir}/calidns
%{_bindir}/dnsbulktest
%{_bindir}/dnsgram
%{_bindir}/dnspcap2calidns
%{_bindir}/dnspcap2protobuf
%{_bindir}/dnsreplay
%{_bindir}/dnsscan
%{_bindir}/dnsscope
%{_bindir}/dnstcpbench
%{_bindir}/dnswasher
%{_bindir}/dumresp
%{_bindir}/ixplore
%{_bindir}/pdns_notify
%{_bindir}/nproxy
%{_bindir}/nsec3dig
%{_bindir}/saxfr
%{_bindir}/sdig
%{_mandir}/man1/calidns.1.gz
%{_mandir}/man1/dnsbulktest.1.gz
%{_mandir}/man1/dnsgram.1.gz
%{_mandir}/man1/dnspcap2calidns.1.gz
%{_mandir}/man1/dnspcap2protobuf.1.gz
%{_mandir}/man1/dnsreplay.1.gz
%{_mandir}/man1/dnsscan.1.gz
%{_mandir}/man1/dnsscope.1.gz
%{_mandir}/man1/dnstcpbench.1.gz
%{_mandir}/man1/dnswasher.1.gz
%{_mandir}/man1/dumresp.1.gz
%{_mandir}/man1/ixplore.1.gz
%{_mandir}/man1/pdns_notify.1.gz
%{_mandir}/man1/nproxy.1.gz
%{_mandir}/man1/nsec3dig.1.gz
%{_mandir}/man1/saxfr.1.gz
%{_mandir}/man1/sdig.1.gz
%{_pkgdocdir}/bind-dnssec.4.2.0_to_4.3.0_schema.sqlite3.sql
%{_pkgdocdir}/bind-dnssec.schema.sqlite3.sql

%files backend-mysql
%{_pkgdocdir}/schema.mysql.sql
%{_pkgdocdir}/dnssec-3.x_to_3.4.0_schema.mysql.sql
%{_pkgdocdir}/nodnssec-3.x_to_3.4.0_schema.mysql.sql
%{_pkgdocdir}/3.4.0_to_4.1.0_schema.mysql.sql
%{_pkgdocdir}/4.1.0_to_4.2.0_schema.mysql.sql
%{_pkgdocdir}/4.2.0_to_4.3.0_schema.mysql.sql
%{_pkgdocdir}/4.3.0_to_4.7.0_schema.mysql.sql
%{_pkgdocdir}/enable-foreign-keys.mysql.sql
%{_libdir}/%{name}/libgmysqlbackend.so

%files backend-postgresql
%{_pkgdocdir}/schema.pgsql.sql
%{_pkgdocdir}/dnssec-3.x_to_3.4.0_schema.pgsql.sql
%{_pkgdocdir}/nodnssec-3.x_to_3.4.0_schema.pgsql.sql
%{_pkgdocdir}/3.4.0_to_4.1.0_schema.pgsql.sql
%{_pkgdocdir}/4.1.0_to_4.2.0_schema.pgsql.sql
%{_pkgdocdir}/4.2.0_to_4.3.0_schema.pgsql.sql
%{_pkgdocdir}/4.3.0_to_4.7.0_schema.pgsql.sql
%{_libdir}/%{name}/libgpgsqlbackend.so

%files backend-pipe
%{_libdir}/%{name}/libpipebackend.so

%files backend-remote
%{_libdir}/%{name}/libremotebackend.so

%files backend-ldap
%{_libdir}/%{name}/libldapbackend.so
%{_pkgdocdir}/dnsdomain2.schema
%{_pkgdocdir}/pdns-domaininfo.schema

%files backend-lmdb
%{_libdir}/%{name}/liblmdbbackend.so

%files backend-lua2
%{_libdir}/%{name}/liblua2backend.so

%files backend-sqlite
%{_pkgdocdir}/schema.sqlite3.sql
%{_pkgdocdir}/dnssec-3.x_to_3.4.0_schema.sqlite3.sql
%{_pkgdocdir}/nodnssec-3.x_to_3.4.0_schema.sqlite3.sql
%{_pkgdocdir}/3.4.0_to_4.0.0_schema.sqlite3.sql
%{_pkgdocdir}/4.0.0_to_4.2.0_schema.sqlite3.sql
%{_pkgdocdir}/4.2.0_to_4.3.0_schema.sqlite3.sql
%{_pkgdocdir}/4.3.0_to_4.3.1_schema.sqlite3.sql
%{_pkgdocdir}/4.3.1_to_4.7.0_schema.sqlite3.sql
%{_libdir}/%{name}/libgsqlite3backend.so

%files backend-tinydns
%{_libdir}/%{name}/libtinydnsbackend.so

%files ixfrdist
%{_bindir}/ixfrdist
%{_mandir}/man1/ixfrdist.1.gz
%{_mandir}/man5/ixfrdist.yml.5.gz
%{_sysconfdir}/%{name}/ixfrdist.example.yml
%{_unitdir}/ixfrdist.service
%{_unitdir}/ixfrdist@.service

%changelog
%autochangelog
