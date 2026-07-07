%global source0_hash bd023a4959faf012db7f0ebfc0d276729e67e5443df193163f98d80fdfc524c9

%global pkgname mariadb

Summary:        A community developed branch of MySQL
Name:           mariadb-server
Version:        11.8.8
Release:        1%{?dist}
License:        GPL-2.0-only
URL:            https://mariadb.org/
Source0:        https://archive.mariadb.org/mariadb-%{version}/source/mariadb-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  bison
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  libaio-devel
BuildRequires:  libxml2-devel
BuildRequires:  pcre2-devel
BuildRequires:  systemd-devel
BuildRequires:  libcurl-devel
BuildRequires:  libevent-devel
BuildRequires:  lz4-devel
BuildRequires:  zstd-devel
BuildRequires:  snappy-devel
BuildRequires:  judy-devel
BuildRequires:  perl-interpreter
BuildRequires:  systemd

Requires:       %{pkgname}-common = %{version}-%{release}
Requires:       %{pkgname}-errmsg = %{version}-%{release}
Requires:       systemd
Requires(pre):  shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
MariaDB is a community developed branch of MySQL, a relational database
management system. This is a placeholder description; see the individual
subpackages for %{pkgname}-server, %{pkgname} (client), %{pkgname}-common,
%{pkgname}-devel and %{pkgname}-libs.

This spec builds MariaDB with cmake's own default storage-engine
autodetection: engines whose external dependencies are not present at
configure time are skipped by the upstream build system itself (this is
how upstream ships every distro package), nothing is force-disabled here.

%package -n %{pkgname}-common
Summary:        The shared files required for MariaDB server and client

%description -n %{pkgname}-common
This package contains files shared between mariadb (client) and
mariadb-server, such as the base my.cnf configuration snippets.

%package -n %{pkgname}
Summary:        A community developed branch of MySQL (client)
Requires:       %{pkgname}-common = %{version}-%{release}
Requires:       %{pkgname}-libs%{?_isa} = %{version}-%{release}

%description -n %{pkgname}
This package contains the MariaDB command line client and other client
utilities (mysqldump equivalent, etc), used by plasma-nm to detect and
manage MariaDB-backed VPN provisioning databases and by other consumers
that need a MariaDB client.

%package -n %{pkgname}-libs
Summary:        The shared libraries required for MariaDB client programs

%description -n %{pkgname}-libs
This package contains the shared libraries (libmariadb / libmysqlclient
compatible) needed by MariaDB client programs.

%package -n %{pkgname}-devel
Summary:        Files needed for developing MariaDB client applications
Requires:       %{pkgname}-libs%{?_isa} = %{version}-%{release}

%description -n %{pkgname}-devel
Header files and development libraries needed to develop client
applications that link against MariaDB.

%package -n %{pkgname}-errmsg
Summary:        Error messages in different languages used by MariaDB server

%description -n %{pkgname}-errmsg
Native language message files used by mariadbd.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{pkgname}-%{version}

%build
%cmake \
        -DBUILD_CONFIG=mysql_release \
        -DMYSQL_MAINTAINER_MODE=OFF \
        -DWITH_SSL=system \
        -DWITH_ZLIB=system \
        -DWITH_PCRE=system \
        -DWITH_JEMALLOC=no \
        -DWITH_SYSTEMD=yes \
        -DINSTALL_SYSCONFDIR=%{_sysconfdir} \
        -DINSTALL_SYSCONF2DIR=%{_sysconfdir}/my.cnf.d \
        -DINSTALL_INFODIR=share/info \
        -DINSTALL_MANDIR=share/man \
        -DINSTALL_PLUGINDIR=%{_libdir}/mysql/plugin \
        -DINSTALL_SCRIPTDIR=bin \
        -DINSTALL_INCLUDEDIR=include/mysql \
        -DINSTALL_DOCDIR=share/doc/%{pkgname}-server \
        -DINSTALL_DOCREADMEDIR=share/doc/%{pkgname}-server \
        -DINSTALL_SHAREDIR=share \
        -DINSTALL_MYSQLSHAREDIR=share/mysql \
        -DINSTALL_MYSQLTESTDIR= \
        -DINSTALL_SQLBENCHDIR= \
        -DINSTALL_SUPPORTFILESDIR=share/mysql \
        -DINSTALL_LIBDIR=%{_lib} \
        -DINSTALL_UNIT_DIR=%{_unitdir}
%cmake_build

%install
%cmake_install
find %{buildroot} -name '*.a' -delete
rm -rf %{buildroot}%{_datadir}/mysql-test
rm -rf %{buildroot}%{_datadir}/mysql/sql-bench
install -d -m 0755 %{buildroot}%{_sharedstatedir}/mysql
install -d -m 0755 %{buildroot}%{_localstatedir}/log/mariadb
install -d -m 0755 %{buildroot}%{_sysconfdir}/my.cnf.d

%pre -n %{pkgname}-server
getent group mysql >/dev/null || groupadd -r mysql
getent passwd mysql >/dev/null || useradd -r -g mysql -d %{_sharedstatedir}/mysql -s /sbin/nologin -c "MariaDB Server" mysql
exit 0

%post -n %{pkgname}-server
%systemd_post mariadb.service

%preun -n %{pkgname}-server
%systemd_preun mariadb.service

%postun -n %{pkgname}-server
%systemd_postun_with_restart mariadb.service

%post -n %{pkgname}-libs -p /sbin/ldconfig
%postun -n %{pkgname}-libs -p /sbin/ldconfig

%files -n %{pkgname}-common
%license COPYING
%dir %{_sysconfdir}/my.cnf.d
%config(noreplace) %{_sysconfdir}/my.cnf
%doc README

%files -n %{pkgname}
%{_bindir}/mariadb
%{_bindir}/mysql
%{_bindir}/mariadb-admin
%{_bindir}/mariadb-dump
%{_bindir}/mariadb-show
%{_bindir}/mariadb-import
%{_bindir}/mariadb-check
%{_mandir}/man1/mariadb.1*

%files -n %{pkgname}-libs
%{_libdir}/libmariadb.so.*
%{_libdir}/mysql/

%files -n %{pkgname}-devel
%{_includedir}/mysql/
%{_libdir}/libmariadb.so
%{_libdir}/pkgconfig/libmariadb.pc
%{_bindir}/mariadb_config
%{_bindir}/mysql_config

%files -n %{pkgname}-errmsg
%{_datadir}/mysql/errmsg-utf8.txt
%{_datadir}/mysql/languages.html

%files -n %{pkgname}-server
%{_sbindir}/mariadbd
%{_bindir}/mariadbd-safe
%{_bindir}/mariadb-install-db
%{_bindir}/mariadb-secure-installation
%{_bindir}/mariadb-upgrade
%{_bindir}/mariadb-backup
%{_bindir}/mariadb-binlog
%{_bindir}/mariadb-tzinfo-to-sql
%{_unitdir}/mariadb.service
%dir %attr(0750, mysql, mysql) %{_sharedstatedir}/mysql
%dir %attr(0750, mysql, mysql) %{_localstatedir}/log/mariadb
%{_mandir}/man1/mariadbd*
%{_mandir}/man8/*

%changelog
%autochangelog
