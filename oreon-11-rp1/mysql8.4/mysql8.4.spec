%global source0_hash none

ExcludeArch: %{ix86}

# Name of the package without any prefixes
%global majorname mysql
%global package_version 8.4.9
%global majorversion %(echo %{package_version} | cut -d'.' -f1-2 )
%global pkgnamepatch mysql


# Set if this package will be the default one in distribution (never in RHEL)
%if 0%{?rhel} || (0%{?oreon} >= 11)
%global mysql_default 0
%else
%{!?mysql_default:%global mysql_default 1}
%endif

# Regression tests may take a long time (many cores recommended), skip them by
# passing --nocheck to rpmbuild or by setting runselftest to 0 if defining
# --nocheck is not possible (e.g. in koji build)
%{!?runselftest:%global runselftest 1}

# Set this to 1 to see which tests fail, but 0 on production ready build
%global ignore_testsuite_result 0

# The last version on which the full testsuite has been run
# In case of further rebuilds of that version, don't require full testsuite to be run
# run only "main" suite
%global last_tested_version 8.4.9
# Set to 1 to force run the testsuite even if it was already tested in current version
%global force_run_testsuite 0

# Filtering: 
%global __requires_exclude ^perl\\((hostnames|lib::mtr|lib::v1|mtr_|My::)
%global __provides_exclude_from ^(%{_datadir}/(mysql|mysql-test)/.*|%{_libdir}/mysql/plugin/.*\\.so)$

%global skiplist platform-specific-tests.list

%global boost_bundled_version 1.84.0


# For some use cases we do not need some parts of the package
%bcond clibrary 1
%bcond devel 1
%bcond client 1
%bcond common 1
%bcond errmsg 1
%bcond test 1

# When there is already another package that ships /etc/my.cnf,
# rather include it than ship the file again, since conflicts between
# those files may create issues
%bcond config 0

# Various plugins
# TO-DO:
#   Need to check and fix the ON/OFF matrix of those plugins.
#   It seems the current implementation is buggy, e.g.:
#     - ldap needs krb5-devel too
#     - when kr5-devel is part of the buildroot, kerberos plugin is compiled no matter the WITH_AUTHENTICATION_KERBEROS value
#     - when fido is disabled but ldap enabled, authentication_oci_client.so is still built
# To avoid issues, leave either all ON or all OFF.
%if 0%{?fedora} || (0%{?oreon} >= 11)
%bcond fido 1
%bcond kerberos 1
%bcond ldap 1
%else
%bcond fido 0
%bcond kerberos 0
%bcond ldap 0
%endif

# For deep debugging we need to build binaries with extra debug info
%bcond debug 0

# Aditional SELinux rules from a standalone package 'mysql-selinux' (that holds rules shared between MariaDB and MySQL)
%bcond require_mysql_selinux 1


# Include files for systemd
%global daemon_name       mysqld
%global daemon_no_prefix  mysqld

# We define some system's well known locations here so we can use them easily
# later when building to another location (like SCL)
%global logrotateddir     %{_sysconfdir}/logrotate.d
%global logfiledir        %{_localstatedir}/log/mysql
%global logfile           %{logfiledir}/%{daemon_no_prefix}.log
# Directory for storing pid file
%global pidfiledir        %{_rundir}/%{daemon_name}
# Defining where database data live
%global dbdatadir         %{_localstatedir}/lib/mysql


# Set explicit conflicts with 'mariadb' packages
%bcond conflicts_mariadb 1

# Make long macros shorter
%global sameevr   %{?epoch:%{epoch}:}%{version}-%{release}

Name:             %{majorname}%{majorversion}
Version:          %{package_version}
Release:          1%{?with_debug:.debug}%{?dist}
Summary:          MySQL client programs and shared libraries
URL:              http://www.mysql.com

# The the `Universal-FOSS-exception-1.0` exception allow client libraries to be linked with most open source SW, not only GPL code.
# Usage of the `Universal-FOSS-exception-1.0` in the SPDX license expression does not signify that we regard "Interfaces" as protected by copyright.
License:          GPL-2.0-only AND ( GPL-2.0-only WITH Universal-FOSS-exception-1.0 ) AND GPL-2.0-or-later AND ( LGPL-2.0-only WITH Universal-FOSS-exception-1.0 ) AND ( GPL-3.0-or-later WITH Bison-exception-2.2 ) AND ( GPL-2.0-only OR BSD-2-Clause ) AND BSD-2-Clause AND BSL-1.0 AND Apache-2.0 AND MIT

Source0:          https://cdn.mysql.com/Downloads/MySQL-8.4/mysql-%{version}.tar.gz
Source3:          my.cnf.in
Source6:          README.mysql-docs
Source7:          README.mysql-license
Source10:         mysql.tmpfiles.d.in
Source11:         mysql.service.in
Source12:         mysql-prepare-db-dir.sh
Source14:         mysql-check-socket.sh
Source15:         mysql-scripts-common.sh
Source17:         mysql-wait-stop.sh
Source18:         mysql@.service.in
# To track rpmlint warnings
Source30:         %{name}.rpmlintrc
# Configuration for server
Source31:         server.cnf.in
# Skipped tests lists
Source50:         rh-skipped-tests-list-base.list
Source51:         rh-skipped-tests-list-arm.list
Source52:         rh-skipped-tests-list-s390.list
Source53:         rh-skipped-tests-list-ppc.list
Source54:         rh-skipped-tests-list-riscv.list

# Comments for these patches are in the patch files
# Patches common for more mysql-like packages
Patch1:           %{pkgnamepatch}-install-test.patch
Patch3:           %{pkgnamepatch}-file-contents.patch
Patch4:           %{pkgnamepatch}-scripts.patch
Patch5:           %{pkgnamepatch}-paths.patch

# Patches specific for this mysql package
Patch51:          %{pkgnamepatch}-sharedir.patch
Patch52:          %{pkgnamepatch}-rpath.patch
Patch54:          %{pkgnamepatch}-gcc-15.patch
Patch56:          %{pkgnamepatch}-flush-logrotate.patch

# Patches taken from boost 1.59
Patch112:         boost-1.57.0-mpl-print.patch

# This macro is used for package/sub-package names in the entire specfile
%if %?mysql_default
%global pkgname %{majorname}
%package -n %{pkgname}
Summary:          MySQL client programs and shared libraries
%else
%global pkgname %{name}
%endif

BuildRequires:    cmake
BuildRequires:    gcc-c++
BuildRequires:    libaio-devel
BuildRequires:    libedit-devel
BuildRequires:    libevent-devel
BuildRequires:    libicu-devel
BuildRequires:    lz4-devel
BuildRequires:    mecab-devel
BuildRequires:    bison
BuildRequires:    libzstd-devel
BuildRequires:    libcurl-devel
%ifnarch aarch64 s390x riscv64
BuildRequires:    numactl-devel
BuildRequires:    libquadmath-devel
%endif
BuildRequires:    openssl
BuildRequires:    openssl-devel

BuildRequires:    perl-interpreter
BuildRequires:    perl-generators
BuildRequires:    rpcgen
BuildRequires:    libtirpc-devel
BuildRequires:    protobuf-lite-devel
BuildRequires:    zlib-devel
# Tests requires time and ps and some perl modules
BuildRequires:    procps
BuildRequires:    time
BuildRequires:    perl(base)
BuildRequires:    perl(Carp)
BuildRequires:    perl(Cwd)
BuildRequires:    perl(Digest::file)
BuildRequires:    perl(Digest::MD5)
BuildRequires:    perl(English)
BuildRequires:    perl(Env)
BuildRequires:    perl(Errno)
BuildRequires:    perl(Exporter)
BuildRequires:    perl(Fcntl)
BuildRequires:    perl(File::Basename)
BuildRequires:    perl(File::Compare)
BuildRequires:    perl(File::Copy)
BuildRequires:    perl(File::Find)
BuildRequires:    perl(File::Spec)
BuildRequires:    perl(File::Spec::Functions)
BuildRequires:    perl(File::Temp)
BuildRequires:    perl(FindBin)
BuildRequires:    perl(Data::Dumper)
BuildRequires:    perl(Getopt::Long)
BuildRequires:    perl(if)
BuildRequires:    perl(IO::File)
BuildRequires:    perl(IO::Handle)
BuildRequires:    perl(IO::Select)
BuildRequires:    perl(IO::Socket::INET)
BuildRequires:    perl(IPC::Open3)
BuildRequires:    perl(JSON)
BuildRequires:    perl(lib)
BuildRequires:    perl(LWP::Simple)
BuildRequires:    perl(Memoize)
BuildRequires:    perl(Net::Ping)
BuildRequires:    perl(POSIX)
BuildRequires:    perl(Socket)
BuildRequires:    perl(strict)
BuildRequires:    perl(Sys::Hostname)
BuildRequires:    perl(Test::More)
BuildRequires:    perl(Time::HiRes)
BuildRequires:    perl(Time::localtime)
BuildRequires:    perl(warnings)
BuildRequires:    systemd

# Since MySQL 8.0.28
%{?with_fido:BuildRequires:    libfido2-devel}

%{?with_kerberos:BuildRequires:    krb5-devel}
%{?with_ldap:BuildRequires:    openldap-devel cyrus-sasl-devel cyrus-sasl-scram}


Requires:         bash coreutils grep
Requires:         %{pkgname}-common = %{sameevr}

# 'boost' header files must be bundled
# See https://bugzilla.redhat.com/show_bug.cgi?id=2260138#c7 for details
Provides:         bundled(boost) = %{boost_bundled_version}

# 'rapidjson' library must be bundled
# The rapidjson upstream made the last release in 2016, even though it has an active development till today (2024, ~750 commits since)
# The MySQL upstream forked the project from a specific commit and added custom patches. See "extra/RAPIDJSON-README" for details.
# In the MySQL 8.0.34, the MySQL upsstream made the 'rapidjson' library to be bundled by default.
Provides:         bundled(rapidjson)

# Not available in Fedora
# https://github.com/martinus/unordered_dense
Provides:         bundled(unordered_dense)

%{?with_conflicts_mariadb:Conflicts: mariadb-any}
# Explicitly disallow installation of mysql + mariadb-server
%{?with_conflicts_mariadb:Conflicts: mariadb-server-any}

%define conflict_with_other_streams() %{expand:\
Provides: %{majorname}%{?1:-%{1}}-any\
Conflicts: %{majorname}%{?1:-%{1}}-any\
}

# Provide also mysqlX.X if default
%if %?mysql_default
%define mysqlX_if_default_arched() %{expand:\
Obsoletes: mysql%{?1:-%{1}} < %{sameevr}\
Obsoletes: mysql%{majorversion}%{?1:-%{1}} < %{sameevr}\
Provides: mysql%{majorversion}%{?1:-%{1}} = %{sameevr}\
Provides: mysql%{majorversion}%{?1:-%{1}}%{?_isa} = %{sameevr}\
}
%define mysqlX_if_default_noarch() %{expand:\
Obsoletes: mysql%{?1:-%{1}} < %{sameevr}\
Obsoletes: mysql%{majorversion}%{?1:-%{1}} < %{sameevr}\
Provides: mysql%{majorversion}%{?1:-%{1}} = %{sameevr}\
}
%else
%define mysqlX_if_default_arched() %{nil}
%define mysqlX_if_default_noarch() %{nil}
%endif

%define add_metadata_arched() %{expand:\
%conflict_with_other_streams %{**}\
%mysqlX_if_default_arched %{**}\
}
%define add_metadata_noarch() %{expand:\
%conflict_with_other_streams %{**}\
%mysqlX_if_default_noarch %{**}\
}

%add_metadata_arched

%description
MySQL is a multi-user, multi-threaded SQL database server. MySQL is a
client/server implementation consisting of a server daemon (mysqld)
and many different client programs and libraries. The base package
contains the standard MySQL client programs and generic MySQL files.

%if %?mysql_default
%description -n %{pkgname}
MySQL is a multi-user, multi-threaded SQL database server. MySQL is a
client/server implementation consisting of a server daemon (mysqld)
and many different client programs and libraries. The base package
contains the standard MySQL client programs and generic MySQL files.
%endif

%if %{with clibrary}
%package          -n %{pkgname}-libs
Summary:          The shared libraries required for MySQL clients
Requires:         %{pkgname}-common = %{sameevr}

%add_metadata_arched libs

%description      -n %{pkgname}-libs
The mysql-libs package provides the essential shared libraries for any
MySQL client program or interface. You will need to install this package
to use any other MySQL package or any clients that need to connect to a
MySQL server.
%endif


%if %{with config}
%package          -n %{pkgname}-config
Summary:          The config files required by server and client

%add_metadata_arched config

%description      -n %{pkgname}-config
The package provides the config file my.cnf and my.cnf.d directory used by any
MariaDB or MySQL program. You will need to install this package to use any
other MariaDB or MySQL package if the config files are not provided in the
package itself.
%endif


%if %{with common}
%package          -n %{pkgname}-common
Summary:          The shared files required for MySQL server and client
BuildArch:        noarch
%if 0%{?flatpak}
Requires:         mariadb-connector-c-config
%else
Requires:         %{_sysconfdir}/my.cnf
%endif

# As this package is noarch, it can't use the %%{?_isa} RPM macro
%add_metadata_noarch common

%description      -n %{pkgname}-common
The mysql-common package provides the essential shared files for any
MySQL program. You will need to install this package to use any other
MySQL package.
%endif


%if %{with errmsg}
%package          -n %{pkgname}-errmsg
Summary:          The error messages files required by MySQL server
BuildArch:        noarch
Requires:         %{pkgname}-common = %{sameevr}

# As this package is noarch, it can't use the %%{?_isa} RPM macro
%add_metadata_noarch errmsg

%description      -n %{pkgname}-errmsg
The package provides error messages files for the MySQL daemon
%endif


%package          -n %{pkgname}-server
Summary:          The MySQL server and related files

Requires:         %{pkgname}%{?_isa} = %{sameevr}

Requires:         %{pkgname}-common = %{sameevr}
%if 0%{?flatpak}
Requires:         mariadb-connector-c-config
%else
Requires:         %{_sysconfdir}/my.cnf
Requires:         %{_sysconfdir}/my.cnf.d
%endif
Requires:         %{pkgname}-errmsg = %{sameevr}
%{?mecab:Requires: mecab-ipadic}
Requires:         coreutils
# We require this to be present for %%{_tmpfilesdir}
# `systemd` is also required for logrotate, as it uses `systemctl kill`
Requires:         systemd
# Make sure it's there when scriptlets run, too
%{?systemd_requires: %systemd_requires}
# SYS_NICE capabilities; #1540946
Recommends:       libcap
# semanage
Requires(post):   policycoreutils-python-utils

# Aditional SELinux rules (common for MariaDB & MySQL) shipped in a separate package
# For cases, where we want to fix a SELinux issues in MySQL sooner than patched selinux-policy-targeted package is released
%if %{with require_mysql_selinux}
Requires:         (mysql-selinux if selinux-policy-targeted)
%endif

Suggests:         logrotate

%{?with_conflicts_mariadb:Conflicts: mariadb-server-any}
%{?with_conflicts_mariadb:Conflicts: mariadb-server-utils-any}
%{?with_conflicts_mariadb:Conflicts: mariadb-server-galera-any}
# Explicitly disallow installation of mysql + mariadb-server
%{?with_conflicts_mariadb:Conflicts: mariadb-any}

%add_metadata_arched server

%description      -n %{pkgname}-server
MySQL is a multi-user, multi-threaded SQL database server. MySQL is a
client/server implementation consisting of a server daemon (mysqld)
and many different client programs and libraries. This package contains
the MySQL server and some accompanying files and directories.


%if %{with devel}
%package          -n %{pkgname}-devel
Summary:          Files for development of MySQL applications
%{?with_clibrary:Requires:         %{pkgname}-libs%{?_isa} = %{sameevr}}
Requires:         openssl-devel
Requires:         zlib-devel
Requires:         libzstd-devel
%{?with_conflicts_mariadb:Conflicts: mariadb-devel-any}
%{?with_conflicts_mariadb:Conflicts: mariadb-connector-c-devel}

%add_metadata_arched devel

%description      -n %{pkgname}-devel
MySQL is a multi-user, multi-threaded SQL database server. This
package contains the libraries and header files that are needed for
developing MySQL client applications.
%endif

%if %{with test}
%package          -n %{pkgname}-test
Summary:          The test suite distributed with MySQL
Requires:         %{pkgname}-test-data = %{sameevr}
Requires:         %{pkgname}%{?_isa} = %{sameevr}
Requires:         %{pkgname}-common = %{sameevr}
Requires:         %{pkgname}-server%{?_isa} = %{sameevr}
Requires:         gzip
Requires:         lz4
Requires:         openssl
Requires:         perl(Digest::file)
Requires:         perl(Digest::MD5)
Requires:         perl(Env)
Requires:         perl(Exporter)
Requires:         perl(Fcntl)
Requires:         perl(File::Temp)
Requires:         perl(FindBin)
Requires:         perl(Data::Dumper)
Requires:         perl(Getopt::Long)
Requires:         perl(IPC::Open3)
Requires:         perl(JSON)
Requires:         perl(LWP::Simple)
Requires:         perl(Memoize)
Requires:         perl(Socket)
Requires:         perl(Sys::Hostname)
Requires:         perl(Test::More)
Requires:         perl(Time::HiRes)
Requires:         perl(File::Compare)

%{?with_conflicts_mariadb:Conflicts: mariadb-test-any}

%add_metadata_arched test

%description      -n %{pkgname}-test
MySQL is a multi-user, multi-threaded SQL database server. This
package contains the architecture specific files for the
regression test suite distributed with the MySQL sources.

%package          -n %{pkgname}-test-data
Summary:          The test suite distributed with MySQL
BuildArch:        noarch
Requires:         %{pkgname}-test = %{sameevr}

# As this package is noarch, it can't use the %%{?_isa} RPM macro
%add_metadata_noarch test-data

%description      -n %{pkgname}-test-data
MySQL is a multi-user, multi-threaded SQL database server. This
package contains the architecture independent data for the
regression test suite distributed with the MySQL sources.
%endif


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -N -n mysql-%{version}
%autopatch -p1

# Remove bundled code that is unused (all cases in which we use the system version of the library instead)
# as required by https://docs.fedoraproject.org/en-US/packaging-guidelines/#bundling
rm -r extra/curl
rm -r extra/icu
rm -r extra/libcbor
rm -r extra/libedit
rm -r extra/libfido2
rm -r extra/protobuf
rm -r extra/tirpc
rm -r extra/zlib
rm -r extra/zstd
# Three files from the lz4 bundle tree are still needed.
# They are the 'xxhash' library with custom extension to it.
find extra/lz4 -type f ! \( -name 'xxhash.c' -o -name 'xxhash.h' -o -name 'my_xxhash.h' \) -delete
# Needed for unit tests (different from MTR tests), which we doesn't run, as they doesn't work on some architectures: #1989847
rm -r extra/googletest
rm -r extra/abseil

# generate a list of tests that fail, but are not disabled by upstream
cat %{SOURCE50} | tee -a mysql-test/%{skiplist}

# disable some tests failing on different architectures
%ifarch aarch64
cat %{SOURCE51} | tee -a mysql-test/%{skiplist}
%endif

%ifarch s390x
cat %{SOURCE52} | tee -a mysql-test/%{skiplist}
%endif

%ifarch ppc64le
cat %{SOURCE53} | tee -a mysql-test/%{skiplist}
%endif

%ifarch riscv64
cat %{SOURCE54} | tee -a mysql-test/%{skiplist}
%endif


cp %{SOURCE3} %{SOURCE10} %{SOURCE11} %{SOURCE12} \
   %{SOURCE14} %{SOURCE15} %{SOURCE17} %{SOURCE18} %{SOURCE31} scripts

%build
# fail quickly and obviously if user tries to build as root
%if %runselftest
    if [ x"$(id -u)" = "x0" ]; then
        echo "mysql's regression tests fail if run as root."
        echo "If you really need to build the RPM as root, use"
        echo "--nocheck to skip the regression tests."
        exit 1
    fi
%endif

# The INSTALL_xxx macros have to be specified relative to CMAKE_INSTALL_PREFIX
# so we can't use %%{_datadir} and so forth here.
%cmake \
         -DBUILD_CONFIG=mysql_release \
         -DINSTALL_LAYOUT=RPM \
         -DDAEMON_NAME="%{daemon_name}" \
         -DDAEMON_NO_PREFIX="%{daemon_no_prefix}" \
         -DLOGFILE_RPM="%{logfile}" \
         -DPID_FILE_DIR="%{pidfiledir}" \
         -DNICE_PROJECT_NAME="MySQL" \
         -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
         -DSYSCONFDIR="%{_sysconfdir}" \
         -DSYSCONF2DIR="%{_sysconfdir}/my.cnf.d" \
         -DINSTALL_DOCDIR="share/doc/%{majorname}" \
         -DINSTALL_DOCREADMEDIR="share/doc/%{majorname}" \
         -DINSTALL_INCLUDEDIR=include/mysql \
         -DINSTALL_INFODIR=share/info \
         -DINSTALL_LIBEXECDIR=libexec \
         -DINSTALL_LIBDIR="%{_lib}/mysql" \
         -DRPATH_LIBDIR="%{_libdir}" \
         -DINSTALL_MANDIR=share/man \
         -DINSTALL_MYSQLSHAREDIR=share/%{majorname} \
         -DINSTALL_MYSQLTESTDIR=share/mysql-test \
         -DINSTALL_PLUGINDIR="%{_lib}/mysql/plugin" \
         -DINSTALL_SBINDIR=bin \
         -DINSTALL_SUPPORTFILESDIR=share/%{majorname} \
         -DMYSQL_DATADIR="%{dbdatadir}" \
         -DMYSQL_UNIX_ADDR="/var/lib/mysql/mysql.sock" \
         -DENABLED_LOCAL_INFILE=ON \
         -DWITH_SYSTEMD=1 \
         -DSYSTEMD_SERVICE_NAME="%{daemon_name}" \
         -DSYSTEMD_PID_DIR="%{pidfiledir}" \
         -DWITH_INNODB_MEMCACHED=ON \
%ifnarch aarch64 s390x riscv64
         -DWITH_NUMA=ON \
%endif
%ifarch s390x riscv64
         -DUSE_LD_GOLD=OFF \
%endif
         -DWITH_ROUTER=OFF \
         -DWITH_SYSTEM_LIBS=ON \
         -DWITH_ZLIB=system \
         -DWITH_RAPIDJSON=bundled \
         -DWITH_MECAB=system \
         -DWITH_FIDO=%{?with_fido:system}%{!?with_fido:none} \
         -DWITH_AUTHENTICATION_FIDO=%{?with_fido:ON}%{!?with_fido:OFF} \
         -DWITH_AUTHENTICATION_KERBEROS=%{?with_kerberos:ON}%{!?with_kerberos:OFF} \
         -DWITH_AUTHENTICATION_LDAP=%{?with_ldap:ON}%{!?with_ldap:OFF} \
         -DWITH_BOOST=boost \
         -DREPRODUCIBLE_BUILD=OFF \
         -DCMAKE_C_FLAGS="%{optflags}%{?with_debug: -fno-strict-overflow -Wno-unused-result -Wno-unused-function -Wno-unused-but-set-variable}" \
         -DCMAKE_CXX_FLAGS="%{optflags}%{?with_debug: -fno-strict-overflow -Wno-unused-result -Wno-unused-function -Wno-unused-but-set-variable}" \
         -DCMAKE_EXE_LINKER_FLAGS="-pie %{build_ldflags}" \
         -DWITH_LTO=ON \
%{?with_debug: -DWITH_DEBUG=1} \
%{?with_debug: -DMYSQL_MAINTAINER_MODE=0} \
         -DTMPDIR=/var/tmp \
         -DCMAKE_C_LINK_FLAGS="%{build_ldflags}" \
         -DCMAKE_CXX_LINK_FLAGS="%{build_ldflags}" \
         -DCMAKE_SKIP_INSTALL_RPATH=YES \
         -DWITH_UNIT_TESTS=0


# Note: disabling building of unittests to workaround #1989847

# Print all Cmake options values; "-LAH" means "List Advanced Help"
cmake -B %{_vpath_builddir} -LAH

%cmake_build

%install
%cmake_install

# install INFO_SRC, INFO_BIN into libdir (upstream thinks these are doc files,
# but that's pretty wacko --- see also %%{name}-file-contents.patch)
install -p -m 0644 %{_vpath_builddir}/Docs/INFO_SRC %{buildroot}%{_libdir}/mysql/
install -p -m 0644 %{_vpath_builddir}/Docs/INFO_BIN %{buildroot}%{_libdir}/mysql/

mkdir -p %{buildroot}%{logfiledir}

mkdir -p %{buildroot}%{pidfiledir}
install -p -m 0755 -d %{buildroot}%{dbdatadir}
install -p -m 0750 -d %{buildroot}%{_localstatedir}/lib/mysql-files
install -p -m 0700 -d %{buildroot}%{_localstatedir}/lib/mysql-keyring

%if %{with config}
install -D -p -m 0644 %{_vpath_builddir}/scripts/my.cnf %{buildroot}%{_sysconfdir}/my.cnf
%endif

# install systemd unit files and scripts for handling server startup
install -D -p -m 644 %{_vpath_builddir}/scripts/mysql.service %{buildroot}%{_unitdir}/%{daemon_name}.service
install -D -p -m 644 %{_vpath_builddir}/scripts/mysql@.service %{buildroot}%{_unitdir}/%{daemon_name}@.service
install -D -p -m 0644 %{_vpath_builddir}/scripts/mysql.tmpfiles.d %{buildroot}%{_tmpfilesdir}/%{daemon_name}.conf
rm -r %{buildroot}%{_tmpfilesdir}/mysql.conf

# Create a sysusers.d config file
# We no longer enforce the hardcoded UID/GID 27
mkdir -p %{buildroot}%{_sysusersdir}
cat > %{buildroot}%{_sysusersdir}/%{name}.conf << EOF
u mysql 27 'MariaDB and MySQL Server' %{dbdatadir} -
EOF

# helper scripts for service starting
install -D -p -m 755 %{_vpath_builddir}/scripts/mysql-prepare-db-dir %{buildroot}%{_libexecdir}/mysql-prepare-db-dir
install -p -m 755 %{_vpath_builddir}/scripts/mysql-wait-stop %{buildroot}%{_libexecdir}/mysql-wait-stop
install -p -m 755 %{_vpath_builddir}/scripts/mysql-check-socket %{buildroot}%{_libexecdir}/mysql-check-socket
install -p -m 644 %{_vpath_builddir}/scripts/mysql-scripts-common %{buildroot}%{_libexecdir}/mysql-scripts-common
install -D -p -m 0644 %{_vpath_builddir}/scripts/server.cnf %{buildroot}%{_sysconfdir}/my.cnf.d/%{majorname}-server.cnf

rm %{buildroot}%{_libdir}/mysql/*.a
rm %{buildroot}%{_mandir}/man1/comp_err.1*

# Put logrotate script where it needs to be
mkdir -p %{buildroot}%{logrotateddir}
# Remove the wrong file
rm %{buildroot}%{_datadir}/%{majorname}/mysql-log-rotate
# Install the correct one (meant for FSH layout in RPM packages)
install -D -m 0644 %{_vpath_builddir}/packaging/rpm-common/mysql.logrotate %{buildroot}%{logrotateddir}/%{daemon_name}

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/mysql" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

# for back-ward compatibility and SELinux, let's keep the mysqld in libexec
# and just create a symlink in /usr/sbin
mv %{buildroot}%{_bindir}/mysqld %{buildroot}%{_libexecdir}/mysqld
mkdir -p %{buildroot}%{_sbindir}
ln -s ../libexec/mysqld %{buildroot}%{_sbindir}/mysqld

%if %{with debug}
mv %{buildroot}%{_bindir}/mysqld-debug %{buildroot}%{_libexecdir}/mysqld
%endif

# copy additional docs into build tree so %%doc will find them
install -p -m 0644 %{SOURCE6} %{_vpath_srcdir}/%{basename:%{SOURCE6}}
install -p -m 0644 %{SOURCE7} %{_vpath_srcdir}/%{basename:%{SOURCE7}}

# Install the list of skipped tests to be available for user runs
install -p -m 0644 %{_vpath_srcdir}/mysql-test/%{skiplist} %{buildroot}%{_datadir}/mysql-test

%if ! %{with clibrary}
unlink %{buildroot}%{_libdir}/mysql/libmysqlclient.so
rm -r %{buildroot}%{_libdir}/mysql/libmysqlclient*.so.*
rm -r %{buildroot}%{_sysconfdir}/ld.so.conf.d
%endif

%if ! %{with devel}
rm %{buildroot}%{_bindir}/mysql_config
rm -r %{buildroot}%{_includedir}/mysql
rm %{buildroot}%{_datadir}/aclocal/mysql.m4
rm %{buildroot}%{_libdir}/pkgconfig/mysqlclient.pc
rm %{buildroot}%{_libdir}/mysql/libmysqlclient*.so
rm %{buildroot}%{_mandir}/man1/mysql_config.1*
%endif

%if ! %{with client}
rm %{buildroot}%{_bindir}/{mysql,mysql_config_editor,\
mysqladmin,mysqlbinlog,\
mysqlcheck,mysqldump,mysqlimport,mysqlshow,mysqlslap}
rm %{buildroot}%{_mandir}/man1/{mysql,mysql_config_editor,\
mysqladmin,mysqlbinlog,\
mysqlcheck,mysqldump,mysqlimport,mysqlshow,mysqlslap}.1*
%endif

%if %{with config}
mkdir -p %{buildroot}%{_sysconfdir}/my.cnf.d
%else
#rm %%{buildroot}%%{_sysconfdir}/my.cnf
%endif

%if ! %{with common}
rm -r %{buildroot}%{_datadir}/%{majorname}/charsets
%endif

%if ! %{with errmsg}
rm %{buildroot}%{_datadir}/%{majorname}/{messages_to_error_log.txt,messages_to_clients.txt}
rm -r %{buildroot}%{_datadir}/%{majorname}/{english,bulgarian,czech,danish,dutch,estonian,\
french,german,greek,hungarian,italian,japanese,korean,norwegian,norwegian-ny,\
polish,portuguese,romanian,russian,serbian,slovak,spanish,swedish,ukrainian}
%endif

%if ! %{with test}
rm %{buildroot}%{_bindir}/{mysql_client_test,mysqlxtest,mysqltest_safe_process}
rm -r %{buildroot}%{_datadir}/mysql-test
%endif



%check
%if %{with test}
%if %runselftest
pushd %_vpath_builddir
# Note: disabling building of unittests to workaround #1989847
#make test VERBOSE=1
pushd mysql-test
cp ../../mysql-test/%{skiplist} .
(
  set -ex
  cd %{buildroot}%{_datadir}/mysql-test

  export MTR_MAX_PARALLEL=16

  export common_testsuite_arguments=" %{?with_debug:--debug-server} \
                                     --force --skip-combinations --report-unstable-tests --clean-vardir --nocheck-testcases \
                                     --suite-timeout=900 --testcase-timeout=30 --port-base=$(( $(date +%s) % 20000 + 10000 )) \
                                     --max-save-core=1 --parallel=auto --retry=3 --max-test-fail=30 \
                                     --mysqld=--skip-innodb-use-native-aio "

  # If full testsuite has already been run on this version and we don't explicitly want the full testsuite to be run
  if [[ "%{last_tested_version}" == "%{version}" ]] && [[ %{force_run_testsuite} -eq 0 ]]
  then
    # in further rebuilds only run the basic "main" suite (~800 tests)
    echo "running only base testsuite"
    perl ./mysql-test-run.pl $common_testsuite_arguments --suite=main --skip-test-list=%{skiplist}
  fi

 # If either this version wasn't marked as tested yet or I explicitly want to run the testsuite, run everything we have (~4000 test)
  if [[ "%{last_tested_version}" != "%{version}" ]] || [[ %{force_run_testsuite} -ne 0 ]]
  then
    echo "running advanced testsuite"
    perl ./mysql-test-run.pl $common_testsuite_arguments \
    %if %{ignore_testsuite_result}
      --max-test-fail=9999 || :
    %else
      --skip-test-list=%{skiplist}
    %endif
  fi

  # There might be a dangling symlink left from the testing, remove it to not be installed
  rm -r var $(readlink var)
)

popd
popd

%endif
%endif



%post -n %{pkgname}-server
%systemd_post %{daemon_name}.service

%preun -n %{pkgname}-server
%systemd_preun %{daemon_name}.service

%postun -n %{pkgname}-server
%systemd_postun_with_restart %{daemon_name}.service



%if %{with client}
%files -n %{pkgname}
%{_bindir}/mysql
%{_bindir}/mysqladmin
%{_bindir}/mysqlbinlog
%{_bindir}/mysqlcheck
%{_bindir}/mysql_config_editor
%{_bindir}/mysqldump
%{_bindir}/mysqlimport
%{_bindir}/mysqlshow
%{_bindir}/mysqlslap

%{_mandir}/man1/mysql.1*
%{_mandir}/man1/mysqladmin.1*
%{_mandir}/man1/mysqlbinlog.1*
%{_mandir}/man1/mysqlcheck.1*
%{_mandir}/man1/mysql_config_editor.1*
%{_mandir}/man1/mysqldump.1*
%{_mandir}/man1/mysqlimport.1*
%{_mandir}/man1/mysqlshow.1*
%{_mandir}/man1/mysqlslap.1*
%endif

%if %{with clibrary}
%files -n %{pkgname}-libs
%dir %{_libdir}/mysql
%{_libdir}/mysql/libmysqlclient*.so.*
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/*
%endif

%if %{with config}
%files -n %{pkgname}-config
# although the default my.cnf contains only server settings, we put it in the
# common package because it can be used for client settings too.
%dir %{_sysconfdir}/my.cnf.d
%config(noreplace) %{_sysconfdir}/my.cnf
%endif

%if %{with common}
%files -n %{pkgname}-common
%license LICENSE storage/innobase/COPYING.Percona storage/innobase/COPYING.Google
%doc README README.mysql-license README.mysql-docs
%dir %{_datadir}/%{majorname}
%{_datadir}/%{majorname}/charsets
%endif

%if %{with errmsg}
%files -n %{pkgname}-errmsg
%{_datadir}/%{majorname}/messages_to_error_log.txt
%{_datadir}/%{majorname}/messages_to_clients.txt
%{_datadir}/%{majorname}/english
%lang(bg) %{_datadir}/%{majorname}/bulgarian
%lang(cs) %{_datadir}/%{majorname}/czech
%lang(da) %{_datadir}/%{majorname}/danish
%lang(nl) %{_datadir}/%{majorname}/dutch
%lang(et) %{_datadir}/%{majorname}/estonian
%lang(fr) %{_datadir}/%{majorname}/french
%lang(de) %{_datadir}/%{majorname}/german
%lang(el) %{_datadir}/%{majorname}/greek
%lang(hu) %{_datadir}/%{majorname}/hungarian
%lang(it) %{_datadir}/%{majorname}/italian
%lang(ja) %{_datadir}/%{majorname}/japanese
%lang(ko) %{_datadir}/%{majorname}/korean
%lang(no) %{_datadir}/%{majorname}/norwegian
%lang(no) %{_datadir}/%{majorname}/norwegian-ny
%lang(pl) %{_datadir}/%{majorname}/polish
%lang(pt) %{_datadir}/%{majorname}/portuguese
%lang(ro) %{_datadir}/%{majorname}/romanian
%lang(ru) %{_datadir}/%{majorname}/russian
%lang(sr) %{_datadir}/%{majorname}/serbian
%lang(sk) %{_datadir}/%{majorname}/slovak
%lang(es) %{_datadir}/%{majorname}/spanish
%lang(sv) %{_datadir}/%{majorname}/swedish
%lang(uk) %{_datadir}/%{majorname}/ukrainian
%endif

%files -n %{pkgname}-server
%{_bindir}/ibd2sdi
%{_bindir}/innochecksum
%{_bindir}/myisamchk
%{_bindir}/myisam_ftdump
%{_bindir}/myisamlog
%{_bindir}/myisampack
%{_bindir}/my_print_defaults
%{_bindir}/mysqld_pre_systemd
%{_bindir}/mysqldumpslow
%{_bindir}/mysql_migrate_keyring
%{_bindir}/mysql_secure_installation
%{_bindir}/mysql_tzinfo_to_sql
%{_bindir}/perror

%config(noreplace) %{_sysconfdir}/my.cnf.d/%{majorname}-server.cnf

%{_sbindir}/mysqld
# sys_nice capability required for rhbz#1628814
%caps(cap_sys_nice=ep) %{_libexecdir}/mysqld

%{_libdir}/mysql/INFO_SRC
%{_libdir}/mysql/INFO_BIN
%if ! %{with common}
%dir %{_datadir}/%{majorname}
%endif

%dir %{_libdir}/mysql
%dir %{_libdir}/mysql/plugin
%{_libdir}/mysql/plugin/adt_null.so
%{_libdir}/mysql/plugin/auth_socket.so
%{_libdir}/mysql/plugin/component_audit_api_message_emit.so
%{_libdir}/mysql/plugin/component_keyring_file.so
%{_libdir}/mysql/plugin/component_log_filter_dragnet.so
%{_libdir}/mysql/plugin/component_log_sink_json.so
%{_libdir}/mysql/plugin/component_log_sink_syseventlog.so
%{_libdir}/mysql/plugin/component_mysqlbackup.so
%{_libdir}/mysql/plugin/component_query_attributes.so
%{_libdir}/mysql/plugin/component_reference_cache.so
%{_libdir}/mysql/plugin/component_validate_password.so
%{_libdir}/mysql/plugin/conflicting_variables.so
%{_libdir}/mysql/plugin/connection_control.so
%{_libdir}/mysql/plugin/daemon_example.ini
%{_libdir}/mysql/plugin/ddl_rewriter.so
%{_libdir}/mysql/plugin/group_replication.so
%{_libdir}/mysql/plugin/ha_example.so
%{_libdir}/mysql/plugin/ha_mock.so
%{_libdir}/mysql/plugin/keyring_udf.so
%{_libdir}/mysql/plugin/libpluginmecab.so
%{_libdir}/mysql/plugin/locking_service.so
%{_libdir}/mysql/plugin/mypluglib.so
%{_libdir}/mysql/plugin/mysql_clone.so
%{_libdir}/mysql/plugin/mysql_no_login.so
%{_libdir}/mysql/plugin/rewrite_example.so
%{_libdir}/mysql/plugin/rewriter.so
%{_libdir}/mysql/plugin/semisync_master.so
%{_libdir}/mysql/plugin/semisync_replica.so
%{_libdir}/mysql/plugin/semisync_slave.so
%{_libdir}/mysql/plugin/semisync_source.so
%{_libdir}/mysql/plugin/validate_password.so
%{_libdir}/mysql/plugin/version_token.so
%{?with_fido:%{_libdir}/mysql/plugin/authentication_webauthn_client.so}
%{?with_fido:%{_libdir}/mysql/plugin/authentication_oci_client.so}
%{?with_kerberos:%{_libdir}/mysql/plugin/authentication_kerberos_client.so}
%{?with_ldap:%{_libdir}/mysql/plugin/authentication_ldap_sasl_client.so}

%{_mandir}/man1/ibd2sdi.1*
%{_mandir}/man1/innochecksum.1*
%{_mandir}/man1/myisamchk.1*
%{_mandir}/man1/myisam_ftdump.1*
%{_mandir}/man1/myisamlog.1*
%{_mandir}/man1/myisampack.1*
%{_mandir}/man1/my_print_defaults.1*
%{_mandir}/man1/mysqldumpslow.1*
%{_mandir}/man1/mysqlman.1*
%{_mandir}/man1/mysql_secure_installation.1*
%{_mandir}/man1/mysql_tzinfo_to_sql.1*
%{_mandir}/man1/perror.1*
%{_mandir}/man8/mysqld.8*

%{_datadir}/%{majorname}/dictionary.txt
%{_datadir}/%{majorname}/*.sql

%{_unitdir}/%{daemon_name}*
%{_libexecdir}/mysql-prepare-db-dir
%{_libexecdir}/mysql-wait-stop
%{_libexecdir}/mysql-check-socket
%{_libexecdir}/mysql-scripts-common

%{_tmpfilesdir}/%{daemon_name}.conf
%{_sysusersdir}/%{name}.conf

# Remember to also update the mysql.tmpfiles.d.in file when updating these permissions
%attr(0755,mysql,mysql) %dir %{dbdatadir}
%attr(0750,mysql,mysql) %dir %{_localstatedir}/lib/mysql-files
%attr(0700,mysql,mysql) %dir %{_localstatedir}/lib/mysql-keyring
%attr(0755,mysql,mysql) %dir %{pidfiledir}
%attr(0750,mysql,mysql) %dir %{logfiledir}

%config(noreplace) %{logrotateddir}/%{daemon_name}

%if %{with devel}
%files -n %{pkgname}-devel
%{_bindir}/mysql_config
%{_includedir}/mysql
%{_datadir}/aclocal/mysql.m4
%dir %{_libdir}/mysql
%if %{with clibrary}
%{_libdir}/mysql/libmysqlclient.so
%endif
%{_libdir}/pkgconfig/mysqlclient.pc
%{_mandir}/man1/mysql_config.1*
%endif

%if %{with test}
%files -n %{pkgname}-test
%{_bindir}/comp_err
%{_bindir}/mysql_client_test
%{_bindir}/mysqld_safe
%{_bindir}/mysql_keyring_encryption_test
%{_bindir}/mysqltest
%{_bindir}/mysql_test_event_tracking
%{_bindir}/mysqltest_safe_process
%{_bindir}/mysqlxtest

%dir %attr(-,mysql,mysql) %{_datadir}/mysql-test
%attr(-,mysql,mysql) %{_datadir}/mysql-test/%{skiplist}

%dir %{_libdir}/mysql
%dir %{_libdir}/mysql/plugin
%{_libdir}/mysql/plugin/auth.so
%{_libdir}/mysql/plugin/auth_test_plugin.so
%{_libdir}/mysql/plugin/component_example_component1.so
%{_libdir}/mysql/plugin/component_example_component2.so
%{_libdir}/mysql/plugin/component_example_component3.so
%{_libdir}/mysql/plugin/component_log_sink_test.so
%{_libdir}/mysql/plugin/component_mysqlx_global_reset.so
%{_libdir}/mysql/plugin/component_pfs_example_component_population.so
%{_libdir}/mysql/plugin/component_pfs_example.so
%{_libdir}/mysql/plugin/component_test_audit_api_message.so
%{_libdir}/mysql/plugin/component_test_backup_lock_service.so
%{_libdir}/mysql/plugin/component_test_component_deinit.so
%{_libdir}/mysql/plugin/component_test_event_tracking_consumer_a.so
%{_libdir}/mysql/plugin/component_test_event_tracking_consumer_b.so
%{_libdir}/mysql/plugin/component_test_event_tracking_consumer_c.so
%{_libdir}/mysql/plugin/component_test_event_tracking_consumer.so
%{_libdir}/mysql/plugin/component_test_event_tracking_producer_a.so
%{_libdir}/mysql/plugin/component_test_event_tracking_producer_b.so
%{_libdir}/mysql/plugin/component_test_execute_prepared_statement.so
%{_libdir}/mysql/plugin/component_test_execute_regular_statement.so
%{_libdir}/mysql/plugin/component_test_host_application_signal.so
%{_libdir}/mysql/plugin/component_test_mysql_command_services.so
%{_libdir}/mysql/plugin/component_test_mysql_current_thread_reader.so
%{_libdir}/mysql/plugin/component_test_mysql_runtime_error.so
%{_libdir}/mysql/plugin/component_test_mysql_signal_handler.so
%{_libdir}/mysql/plugin/component_test_mysql_system_variable_set.so
%{_libdir}/mysql/plugin/component_test_mysql_thd_store_service.so
%{_libdir}/mysql/plugin/component_test_pfs_notification.so
%{_libdir}/mysql/plugin/component_test_pfs_resource_group.so
%{_libdir}/mysql/plugin/component_test_sensitive_system_variables.so
%{_libdir}/mysql/plugin/component_test_server_telemetry_metrics.so
%{_libdir}/mysql/plugin/component_test_server_telemetry_traces.so
%{_libdir}/mysql/plugin/component_test_server_telemetry_logs_client.so
%{_libdir}/mysql/plugin/component_test_server_telemetry_logs_export.so
%{_libdir}/mysql/plugin/component_test_status_var_reader.so
%{_libdir}/mysql/plugin/component_test_status_var_service_int.so
%{_libdir}/mysql/plugin/component_test_status_var_service_reg_only.so
%{_libdir}/mysql/plugin/component_test_status_var_service.so
%{_libdir}/mysql/plugin/component_test_status_var_service_str.so
%{_libdir}/mysql/plugin/component_test_status_var_service_unreg_only.so
%{_libdir}/mysql/plugin/component_test_string_service_charset.so
%{_libdir}/mysql/plugin/component_test_string_service_long.so
%{_libdir}/mysql/plugin/component_test_string_service.so
%{_libdir}/mysql/plugin/component_test_system_variable_source.so
%{_libdir}/mysql/plugin/component_test_sys_var_service_int.so
%{_libdir}/mysql/plugin/component_test_sys_var_service_same.so
%{_libdir}/mysql/plugin/component_test_sys_var_service.so
%{_libdir}/mysql/plugin/component_test_sys_var_service_str.so
%{_libdir}/mysql/plugin/component_test_table_access.so
%{_libdir}/mysql/plugin/component_test_udf_registration.so
%{_libdir}/mysql/plugin/component_test_udf_services.so
%{_libdir}/mysql/plugin/component_udf_reg_3_func.so
%{_libdir}/mysql/plugin/component_udf_reg_avg_func.so
%{_libdir}/mysql/plugin/component_udf_reg_int_func.so
%{_libdir}/mysql/plugin/component_udf_reg_int_same_func.so
%{_libdir}/mysql/plugin/component_udf_reg_only_3_func.so
%{_libdir}/mysql/plugin/component_udf_reg_real_func.so
%{_libdir}/mysql/plugin/component_udf_unreg_3_func.so
%{_libdir}/mysql/plugin/component_udf_unreg_int_func.so
%{_libdir}/mysql/plugin/component_udf_unreg_real_func.so
%{_libdir}/mysql/plugin/libdaemon_example.so
%{_libdir}/mysql/plugin/libtest_framework.so
%{_libdir}/mysql/plugin/libtest_services.so
%{_libdir}/mysql/plugin/libtest_services_threaded.so
%{_libdir}/mysql/plugin/libtest_session_attach.so
%{_libdir}/mysql/plugin/libtest_session_detach.so
%{_libdir}/mysql/plugin/libtest_session_info.so
%{_libdir}/mysql/plugin/libtest_session_in_thd.so
%{_libdir}/mysql/plugin/libtest_sql_2_sessions.so
%{_libdir}/mysql/plugin/libtest_sql_all_col_types.so
%{_libdir}/mysql/plugin/libtest_sql_cmds_1.so
%{_libdir}/mysql/plugin/libtest_sql_commit.so
%{_libdir}/mysql/plugin/libtest_sql_complex.so
%{_libdir}/mysql/plugin/libtest_sql_errors.so
%{_libdir}/mysql/plugin/libtest_sql_lock.so
%{_libdir}/mysql/plugin/libtest_sql_processlist.so
%{_libdir}/mysql/plugin/libtest_sql_replication.so
%{_libdir}/mysql/plugin/libtest_sql_reset_connection.so
%{_libdir}/mysql/plugin/libtest_sql_shutdown.so
%{_libdir}/mysql/plugin/libtest_sql_sleep_is_connected.so
%{_libdir}/mysql/plugin/libtest_sql_sqlmode.so
%{_libdir}/mysql/plugin/libtest_sql_stmt.so
%{_libdir}/mysql/plugin/libtest_sql_stored_procedures_functions.so
%{_libdir}/mysql/plugin/libtest_sql_views_triggers.so
%{_libdir}/mysql/plugin/libtest_x_sessions_deinit.so
%{_libdir}/mysql/plugin/libtest_x_sessions_init.so
%{_libdir}/mysql/plugin/pfs_example_plugin_employee.so
%{_libdir}/mysql/plugin/qa_auth_client.so
%{_libdir}/mysql/plugin/qa_auth_interface.so
%{_libdir}/mysql/plugin/qa_auth_server.so
%{_libdir}/mysql/plugin/replication_observers_example_plugin.so
%{_libdir}/mysql/plugin/test_security_context.so
%{_libdir}/mysql/plugin/test_services_command_services.so
%{_libdir}/mysql/plugin/test_services_host_application_signal.so
%{_libdir}/mysql/plugin/test_services_plugin_registry.so
%{_libdir}/mysql/plugin/test_udf_services.so
%{_libdir}/mysql/plugin/udf_example.so

%files -n %{pkgname}-test-data
%attr(-,mysql,mysql) %{_datadir}/mysql-test
%exclude %{_datadir}/mysql-test/%{skiplist}

%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.4.9-1
- Import
