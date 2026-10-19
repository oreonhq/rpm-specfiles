%global source0_hash 521c0712e9291fa96558df9e2ff431376a3a79329f13751896b694cae12765b4
%bcond_with     debug
%bcond_without  testsuite
Name:           mariadb-connector-c
Version:        3.4.11
Release:        1%{?dist}
Summary:        The MariaDB Native Client library (C driver)
License:        LGPL-2.1-or-later AND PHP-3.0 AND PHP-3.01
Source0:        https://archive.mariadb.org/connector-c-%{version}/%{name}-%{version}-src.tar.gz
Source2:        my.cnf.in
Source3:        client.cnf
Url:            http://mariadb.org/
%if %{with testsuite}
Patch1:         testsuite.patch
%endif
%if 0%{?flatpak}
Requires:       %{name}-config = %{version}-%{release}
%else
Requires:       %{_sysconfdir}/my.cnf
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  krb5-devel
BuildRequires:  libcurl-devel
BuildRequires:  libzstd-devel
BuildRequires:  multilib-rpm-config
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The MariaDB Native Client library (C driver) is used to connect applications
developed in C/C++ to MariaDB and MySQL databases.

%package devel
Summary:        Development files for mariadb-connector-c
Requires:       %{name} = %{version}-%{release}
Recommends:     %{name}-doc = %{version}-%{release}
Requires:       openssl-devel zlib-devel
BuildRequires:  multilib-rpm-config
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
Requires:       %{name} = %{version}-%{release}
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
Obsoletes:      mariadb-config <= 3:10.3.8-4
%description config
This package delivers /etc/my.cnf that includes other configuration files
from the /etc/my.cnf.d directory and ships this directory as well.
Other packages should only put their files into /etc/my.cnf.d directory
and require this package, so the /etc/my.cnf file is present.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}-src
%if %{with testsuite}
%patch -P1 -p1
%endif

# Remove unsused parts
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
%if %{with debug}
CFLAGS="$CFLAGS     -O0 -g"; export CFLAGS
CXXFLAGS="$CXXFLAGS -O0 -g"; export CXXFLAGS
FFLAGS="$FFLAGS     -O0 -g"; export FFLAGS
FCFLAGS="$FCFLAGS   -O0 -g"; export FCFLAGS
%endif
cmake -B %__cmake_builddir -LAH
%cmake_build
sed -e 's|@SYSCONFDIR@|%{_sysconfdir}|' %{SOURCE2} > my.cnf
%install
%cmake_install
%multilib_fix_c_header --file %{_includedir}/mysql/mariadb_version.h
rm %{buildroot}%{_libdir}/lib*.a
ln -s mariadb_config %{buildroot}%{_bindir}/mysql_config
ln -s mariadb_version.h %{buildroot}%{_includedir}/mysql/mysql_version.h
install -D -p -m 0644 my.cnf %{buildroot}%{_sysconfdir}/my.cnf
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/my.cnf.d/client.cnf
%if %{with testsuite}
echo %{_libdir}/mariadb/connector-c/tests > %{name}.conf
install -D -p -m 0644 %{name}.conf %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%{buildroot}%{_bindir}/mariadb_config
%if %{with testsuite}
%ctest --test-dir %{__cmake_builddir}/unittest/libmariadb/
%endif
%if %{with testsuite}
%post -n %{name}-test -p /usr/bin/ldconfig

%postun -n %{name}-test -p /usr/bin/ldconfig

%endif
%files -f %{oreon_filedir}/main.list
%files -n mariadb-connector-c-devel -f %{oreon_filedir}/mariadb-connector-c-devel.list
%files -n mariadb-connector-c-doc -f %{oreon_filedir}/mariadb-connector-c-doc.list
%files -n mariadb-connector-c-test -f %{oreon_filedir}/mariadb-connector-c-test.list
%files -n mariadb-connector-c-config -f %{oreon_filedir}/mariadb-connector-c-config.list

%changelog

%autochangelog
