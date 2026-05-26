# For deep debugging we need to build binaries with extra debug info
%bcond_with     debug
# Enable building and packing of the testsuite
%bcond_without  testsuite



Name:           mariadb-connector-c
Version:        3.4.8
Release:        3%{?with_debug:.debug}%{?dist}
Summary:        The MariaDB Native Client library (C driver)
License:        LGPL-2.1-or-later AND PHP-3.0 AND PHP-3.01
Source:         https://archive.mariadb.org/connector-c-%{version}/%{name}-%{version}-src.tar.gz
Source2:        my.cnf.in
Source3:        client.cnf
Url:            http://mariadb.org/
# More information: https://mariadb.com/kb/en/mariadb/building-connectorc-from-source/

%if %{with testsuite}
Patch1:         testsuite.patch
# oreon url source checksums begin
%global source0_sha256 156aed3b49f857d0ac74fb76f1982968bcbfd8382da3f5b6ae71f616729920d7
%global source0_file mariadb-connector-c-3.4.8-src.tar.gz
# oreon url source checksums end
%endif

%if 0%{?flatpak}
Requires:       %{name}-config = %{version}-%{release}
%else
Requires:       %{_sysconfdir}/my.cnf
%endif
BuildRequires:  gcc-c++ cmake openssl-devel zlib-devel libzstd-devel
# Remote-IO plugin
BuildRequires:  libcurl-devel
# auth_gssapi_client plugin
BuildRequires:  krb5-devel

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/mariadb-connector-c-3.4.8-src.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "156aed3b49f857d0ac74fb76f1982968bcbfd8382da3f5b6ae71f616729920d7" || { echo "oreon: Source0 SHA256 mismatch for mariadb-connector-c-3.4.8-src.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{name}-%{version}-src
%if %{with testsuite}
%patch -P1 -p1
%endif

# Remove unsused parts
rm -r win win-iconv external/zlib



%build
# https://jira.mariadb.org/browse/MDEV-13836:
#   The server has (used to have for ages) some magic around the port number.
#   If it's 0, the default port value will use getservbyname("mysql", "tcp"), that is, whatever is written in /etc/services.
#   If it's a positive number, say, 3306, it will be 3306, no matter what /etc/services say.
#   I don't know if that behavior makes much sense, /etc/services wasn't supposed to be a system configuration file.

# The INSTALL_* macros have to be specified relative to CMAKE_INSTALL_PREFIX
# so we can't use %%{_datadir} and so forth here.

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

# Override all optimization flags when making a debug build
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

# Remove static linked libraries and symlinks to them
rm %{buildroot}%{_libdir}/lib*.a

# Add a compatibility symlinks
ln -s mariadb_config %{buildroot}%{_bindir}/mysql_config
ln -s mariadb_version.h %{buildroot}%{_includedir}/mysql/mysql_version.h

# Install config files
install -D -p -m 0644 my.cnf %{buildroot}%{_sysconfdir}/my.cnf
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/my.cnf.d/client.cnf
%if %{with testsuite}
echo %{_libdir}/mariadb/connector-c/tests > %{name}.conf
install -D -p -m 0644 %{name}.conf %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf
%endif



%check
# Check the generated configuration on the actual machine
%{buildroot}%{_bindir}/mariadb_config

# Run the unit tests
# - don't run mytap tests
# - ignore the testsuite result for now. Enable tests now, fix them later.
# Note: there must be a database called 'test' created for the testcases to be run
%if %{with testsuite}
%ctest --test-dir %{__cmake_builddir}/unittest/libmariadb/
%endif

%if %{with testsuite}
%post -n %{name}-test -p /usr/bin/ldconfig

%postun -n %{name}-test -p /usr/bin/ldconfig
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
# Library manual pages
%{_mandir}/man3/{mariadb,mysql}_*.3*



%files devel
# Binary which provides compiler info for software compiling against this library
%{_bindir}/mariadb_config
%{_bindir}/mysql_config

# Symlinks to the versioned library
%{_libdir}/libmariadb.so
%{_libdir}/libmysqlclient.so
%{_libdir}/libmysqlclient_r.so

# Pkgconfig
%{_libdir}/pkgconfig/libmariadb.pc

# Header files
%dir %{_includedir}/mysql
%{_includedir}/mysql/*



%files config
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


# Opened issues on the upstream tracker:
#   https://jira.mariadb.org/browse/CONC-293
#      DESCRIPTION: add mysql_config and mariadb_config man page
#      IN_PROGRESS: upsteam plans to add it to 3.1 release
#   https://jira.mariadb.org/browse/CONC-436
#      DESCRIPTION: Make testsuite independent / portable
#      NEW:         PR submitted, problem explained, waiting on upstream response

# Downstream issues:
#   Start running this package testsuite at the build time
#      It requires a running MariaDB server
#         mariadb-server package pulls in mariadb-connector-c as a dependency
#         Need to ensure, that the testsuite is ran against the newly build library, instead of the one from the pulled package
#      Need to ensure, that the testsuite will also run properly on 'fedpkg local' buid, not damaging the host machine

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.4.8-3
- Import
