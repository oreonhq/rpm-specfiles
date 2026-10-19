%global source0_hash f8a10edbf60e49d8c160e93121989d5ebcdad838d0e0b747f26ef7e89fd220c0
%global _hardened_build 1
%global backends %{nil}
Name: pdns
Version: 5.1.4
Release:        1%{?dist}
Summary:        A modern, advanced and high performance authoritative-only name server
License: GPL-2.0-only
URL: http://powerdns.com
Source0:        http://downloads.powerdns.com/releases/%{name}-%{version}.tar.bz2
ExcludeArch: %{arm} %{ix86}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%ifarch ppc64le riscv64
%define lua_implementation lua
%else
%define lua_implementation luajit
%endif
Provides: powerdns = %{version}-%{release}
%global backends %{backends} bind
# oreon:deps
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  krb5-devel
BuildRequires:  libcurl-devel
BuildRequires:  libpq-devel
BuildRequires:  libsodium-devel
BuildRequires:  lmdb-devel
BuildRequires:  luajit-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  p11-kit-devel
BuildRequires:  perl
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  tinycdb-devel
BuildRequires:  yaml-cpp-devel
# /oreon:deps
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
%oreon_prep
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
%{__mv} %{buildroot}/%{_bindir}/zone2ldap %{buildroot}/%{_bindir}/pdns_zone2ldap
%{__mv} %{buildroot}/%{_mandir}/man1/zone2ldap.1 %{buildroot}/%{_mandir}/man1/pdns_zone2ldap.1
sed -i \
    -e 's/# setuid=/setuid=pdns/' \
    -e 's/# setgid=/setgid=pdns/' \
    -e 's/# launch=/launch=bind/' \
    -e 's/# security-poll-suffix=secpoll\.powerdns\.com\./security-poll-suffix=/' \
    %{buildroot}%{_sysconfdir}/%{name}/pdns.conf
%{__rm} %{buildroot}/%{_bindir}/stubquery
%{__install} -d %{buildroot}/%{_sharedstatedir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make %{?_smp_mflags} -C pdns check
%post

%systemd_post pdns.service
%preun

%systemd_preun pdns.service
%postun

%systemd_postun_with_restart pdns.service
%files -f %{oreon_filedir}/main.list
%files -n pdns-tools -f %{oreon_filedir}/pdns-tools.list
%files -n pdns-backend-mysql -f %{oreon_filedir}/pdns-backend-mysql.list
%files -n pdns-backend-postgresql -f %{oreon_filedir}/pdns-backend-postgresql.list
%files -n pdns-backend-pipe -f %{oreon_filedir}/pdns-backend-pipe.list
%files -n pdns-backend-remote -f %{oreon_filedir}/pdns-backend-remote.list
%files -n pdns-backend-ldap -f %{oreon_filedir}/pdns-backend-ldap.list
%files -n pdns-backend-lmdb -f %{oreon_filedir}/pdns-backend-lmdb.list
%files -n pdns-backend-lua2 -f %{oreon_filedir}/pdns-backend-lua2.list
%files -n pdns-backend-sqlite -f %{oreon_filedir}/pdns-backend-sqlite.list
%files -n pdns-backend-tinydns -f %{oreon_filedir}/pdns-backend-tinydns.list
%files -n pdns-ixfrdist -f %{oreon_filedir}/pdns-ixfrdist.list

%changelog

%autochangelog
