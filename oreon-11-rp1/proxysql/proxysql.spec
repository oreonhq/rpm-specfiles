%global source0_hash b8b2e2b27fd1d9bd013b3bde698f27c0290876e4a97de14fd8577693785dcfa3
Summary:        A high-performance MySQL proxy
Name:          proxysql
Version:       4.0.11
Release:        1%{?dist}
URL:           https://proxysql.com/
License:       GPL-3.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause AND BSD-2-Clause AND MIT
Suggests: mariadb, mysql, postgresql
ExcludeArch:   %{power64} s390x %{ix86}
Provides:      bundled(jemalloc) = 5.2.0
Provides:      bundled(mariadb-connector-c) = 3.3.8
Provides:      bundled(re2) = 20221201
Provides:      bundled(clickhouse-cpp) = 2.3.0
Provides:      bundled(prometheus-cpp) = 1.1.0
Provides:      bundled(cityhash) = 1.1.1
Provides:      bundled(libhttpserver) = 0.18.2
Provides:      bundled(libmicrohttpd) = 0.9.77
Provides:      bundled(coredumper) = 0^cb6cead
Source0:        https://github.com/sysown/proxysql/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:       proxysql.1
Source2:       0007-Fix-gcc-15.patch
Source3:       0009-Fix-gcc-15-postgresql.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  libconfig-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdaemon-devel
BuildRequires:  libev-devel
BuildRequires:  libevent-devel
BuildRequires:  libicu-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  perl
BuildRequires:  python3
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
ProxySQL is a high performance, high availability, protocol aware proxy for
MySQL and forks (like Percona Server and MariaDB).

# The upstream code bundles multiple libraries: libconfig, libdaemon, sqlite3, re2,
# mariadb-connector-c, pcre, clickhouse-cpp, prometheus-cpp, lz4, cityhash, microhttpd, curl
# ev, coredumper, libssl and jemalloc.
# This patch de-bundles 8 of these libraries: libconfig, libdaemon and sqlite3,
# libsl, pcre, curl, lz4, ev
# The remaining libraries are not de-bundled due to different reasons (mainly
# being patched, more info here: https://bugzilla.redhat.com/show_bug.cgi?id=1457929).
# Other remaining libraries are not maintained in Fedora (clickhouse-cpp,
# cityhash, prometheus-cpp)
#
# NOTE: libdaemon contains custom patch (since https://github.com/sysown/proxysql/pull/4291)
#       but I don't believe it is worth to bundle it just because of that.
%patchlist
0001-Unbundle-libconfig-libdaemon-sqlite3-pcre-lz3-curl-e.patch
0002-Enable-tcp_fastopen-in-bundled-libhttpserver.patch
0003-Simplify-systemd-services.patch
0004-Apply-fPIC-properly-in-re2-build.patch
0006-Fix-coredumper-build.patch
0008-apply-gcc15-patches.patch
0010-btree-uint16_t.patch 

%prep

%autosetup -p1
# Remove sources of debundled libraries
rm -r deps/{libssl,pcre,curl,lz4,libev,libconfig,libdaemon,sqlite3}

# Create a sysusers.d config file
cat >proxysql.sysusers.conf <<EOF
u proxysql - 'ProxySQL' /var/lib/proxysql -
EOF

# Patch 0007
mv %{SOURCE2} deps/mariadb-client-library/ma_global.h.patch

# Patch 0009
mv %{SOURCE3} deps/postgresql/c.h.patch

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
export GIT_VERSION=%{version}
%global _configure :
%configure help
CXXFLAGS="$CXXFLAGS -Wno-error=cpp -Wno-error=template-body"
export CPPFLAGS=$CXXFLAGS
%make_build
%install
install -p -D -m 0755 src/proxysql %{buildroot}%{_bindir}/proxysql
install -p -D -m 0640 etc/proxysql.cnf %{buildroot}%{_sysconfdir}/proxysql.cnf
install -p -D -m 0755 tools/proxysql_galera_checker.sh %{buildroot}%{_datadir}/%{name}/tools/proxysql_galera_checker.sh
install -p -D -m 0755 tools/proxysql_galera_writer.pl %{buildroot}%{_datadir}/%{name}/tools/proxysql_galera_writer.pl
install -p -D -m 0644 systemd/system/proxysql.service %{buildroot}%{_unitdir}/proxysql.service
install -p -D -m 0644 systemd/system/proxysql-initial.service %{buildroot}%{_unitdir}/proxysql-initial.service
install -p -D -m 0644 README.md %{buildroot}%{_docdir}/proxysql/README.md
install -p -D -m 0644 RUNNING.md %{buildroot}%{_docdir}/proxysql/RUNNING.md
install -p -D -m 0644 FAQ.md %{buildroot}%{_docdir}/proxysql/FAQ.md
install -p -D -m 0644 doc/release_notes/*.md -t %{buildroot}%{_docdir}/proxysql
install -p -D -m 0644 doc/internal/*.txt -t %{buildroot}%{_docdir}/proxysql
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1
install -d -m 0755 %{buildroot}%{_sharedstatedir}/proxysql
install -m0644 -D proxysql.sysusers.conf %{buildroot}%{_sysusersdir}/proxysql.conf
%oreon_autofiles main

%post

%systemd_post proxysql.service
%preun

%systemd_preun proxysql.service
%postun

%systemd_postun_with_restart proxysql.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
