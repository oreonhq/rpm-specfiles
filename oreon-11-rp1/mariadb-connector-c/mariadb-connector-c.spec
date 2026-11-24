# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 521c0712e9291fa96558df9e2ff431376a3a79329f13751896b694cae12765b4
%global source2_hash 2193c5c3592a3356ec131c819fc173b577c458c708cec7144a815089f69282db
%global source3_hash 5c65d419b0ab8a18ae14a14d54046a5cffb2f1966ec9cb5a88ecffc02503648f
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond debug 0
%bcond testsuite 1

%if %{with debug}
%global _pkg_extra_cflags   -O0 -g
%global _pkg_extra_cxxflags -O0 -g
%undefine _fortify_level
%endif

Name:           mariadb-connector-c
Version:        3.4.11
Release:        1%{?with_debug:.debug}%{?dist}
Summary:        MariaDB Native Client library (C driver)
License:        LGPL-2.1-or-later AND PHP-3.0 AND PHP-3.01 AND LicenseRef-Fedora-Public-Domain
Source0:        https://archive.mariadb.org/connector-c-%{version}/%{name}-%{version}-src.tar.gz
Source2:        my.cnf.in
Source3:        client.cnf
URL:            https://mariadb.org/

%if %{with testsuite}
Patch1:         testsuite.patch
%endif

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  cmake
BuildRequires:  libzstd-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  libcurl-devel
BuildRequires:  krb5-devel

Requires:       %{name}-config = %{version}-%{release}

Provides:       bundled(ed25519-ref10)

%description
The MariaDB Native Client library (C driver) is used to connect applications
developed in C/C++ to MariaDB and MySQL databases.

%package devel
Summary:        Development files for mariadb-connector-c
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     %{name}-doc = %{version}-%{release}
Requires:       openssl-devel
Requires:       zlib-devel
%{!?rhel:BuildRequires:  multilib-rpm-config}
Conflicts:      mysql-devel-any

%description devel
Development files for mariadb-connector-c.
Contains everything needed to build against libmariadb.so >=3 client library.

%package doc
Summary:        Manual pages documenting API of the libmariadb.so library
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Manual pages documenting API of the libmariadb.so library.

%if %{with testsuite}
%package test
Summary:        Testsuite files for mariadb-connector-c
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake
Recommends:     mariadb-server

%description test
Testsuite files for mariadb-connector-c.
Contains binaries and a prepared CMake ctest file.
Requires running MariaDB / MySQL server with create database "test".
%endif

%package config
Summary:        Configuration files for packages that use /etc/my.cnf as a configuration file
BuildArch:      noarch

%description config
This package delivers /etc/my.cnf that includes other configuration files
from the /etc/my.cnf.d directory and ships this directory as well.
Other packages should only put their files into /etc/my.cnf.d directory
and require this package, so the /etc/my.cnf file is present.

%prep
%oreon_sha256
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
%autosetup -p1 -n %{name}-%{version}-src

rm -r win win-iconv external/zlib

%build

%cmake . \
       -DCMAKE_BUILD_TYPE="%{?with_debug:Debug}%{!?with_debug:RelWithDebInfo}" \
       -DCMAKE_SYSTEM_PROCESSOR="%{_arch}" \
       -DCMAKE_COMPILE_WARNING_AS_ERROR=0 \
\
       -DMARIADB_UNIX_ADDR=%{_sharedstatedir}/mysql/mysql.sock \
       -DMARIADB_PORT=3306 \
\
       -DWITH_EXTERNAL_ZLIB=ON \
       -DWITH_SSL=OPENSSL \
       -DWITH_MYSQLCOMPAT=ON \
       -DPLUGIN_CLIENT_ED25519=DYNAMIC \
\
       -DDEFAULT_SSL_VERIFY_SERVER_CERT=OFF \
\
       -DINSTALL_LAYOUT=RPM \
       -DINSTALL_BINDIR="bin" \
       -DINSTALL_LIBDIR="%{_lib}" \
       -DINSTALL_INCLUDEDIR="include/mysql" \
       -DINSTALL_PLUGINDIR="%{_lib}/mariadb/plugin" \
       -DINSTALL_PCDIR="%{_lib}/pkgconfig" \
\
%if %{with testsuite}
       -DWITH_UNIT_TESTS=ON
%endif

cmake -B %{_vpath_builddir} -N -LAH

%cmake_build

sed -e 's|@SYSCONFDIR@|%{_sysconfdir}|' %{SOURCE2} > my.cnf

%install
%cmake_install

%if %{undefined rhel}
%multilib_fix_c_header --file %{_includedir}/mysql/mariadb_version.h
%endif

rm %{buildroot}%{_libdir}/lib*.a

ln -s mariadb_config %{buildroot}%{_bindir}/mysql_config
ln -s mariadb_version.h %{buildroot}%{_includedir}/mysql/mysql_version.h

install -D -p -m 0644 my.cnf %{buildroot}%{_sysconfdir}/my.cnf
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/my.cnf.d/client.cnf
%if %{with testsuite}
echo %{_libdir}/mariadb/connector-c/tests > %{name}.conf
install -D -p -m 0644 %{name}.conf %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf
%endif

%check
%{buildroot}%{_bindir}/mariadb_config

%if %{with testsuite}
%ctest --test-dir %{_vpath_builddir}/unittest/libmariadb/
%endif

%files
%{_libdir}/libmariadb.so.3

%dir %{_libdir}/mariadb
%dir %{_libdir}/mariadb/plugin
%{_libdir}/mariadb/plugin/auth_gssapi_client.so
%{_libdir}/mariadb/plugin/caching_sha2_password.so
%{_libdir}/mariadb/plugin/client_ed25519.so
%{_libdir}/mariadb/plugin/dialog.so
%{_libdir}/mariadb/plugin/mysql_clear_password.so
%{_libdir}/mariadb/plugin/parsec.so
%{_libdir}/mariadb/plugin/remote_io.so
%{_libdir}/mariadb/plugin/sha256_password.so
%{_libdir}/mariadb/plugin/zstd.so

%doc README
%license COPYING.LIB

%files doc
%{_mandir}/man3/{mariadb,mysql}_*.3*

%files devel
%{_bindir}/mariadb_config
%{_bindir}/mysql_config

%{_libdir}/libmariadb.so
%{_libdir}/libmysqlclient.so
%{_libdir}/libmysqlclient_r.so

%{_libdir}/pkgconfig/libmariadb.pc

%dir %{_includedir}/mysql
%{_includedir}/mysql/*

%files config
%license COPYING.LIB
%dir %{_sysconfdir}/my.cnf.d
%config(noreplace) %{_sysconfdir}/my.cnf
%config(noreplace) %{_sysconfdir}/my.cnf.d/client.cnf

%if %{with testsuite}
%files test
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%dir %{_libdir}/mariadb/connector-c
%dir %{_libdir}/mariadb/connector-c/tests
%{_libdir}/mariadb/connector-c/tests/libcctap.so
%{_sysconfdir}/ld.so.conf.d/%{name}.conf
%endif

%changelog
%autochangelog
