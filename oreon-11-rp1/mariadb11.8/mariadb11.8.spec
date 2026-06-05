%global source0_hash b126581a8ca89376d2a3ce63fee97c114c3e15315345e769b9d00c51e1b7d619
%global source1_hash 695fd197fa5aff8fc67b5f2bbc110490a875cdf7a41686ac8512fb480fa8ada7
%global source4_hash 59c8556fd45e68599897cd5d74efad9c4a43f85e981fe7ac3ac5fd7aa70672ac

# Plain package name for cases, where %%{name} differs (e.g. for versioned packages)
%global majorname mariadb
%global package_version 11.8.6
%global majorversion %(echo %{package_version} | cut -d'.' -f1-2 )

# Set if this package will be the default one in distribution
%{!?mariadb_default:%global mariadb_default 1}

# Regression tests may take a long time (many cores recommended), skip them by
%{!?runselftest:%global runselftest 1}

# Set this to 1 to see which tests fail, but 0 on production ready build
%global ignore_testsuite_result 0

# The last version on which the full testsuite has been run
# In case of further rebuilds of that version, don't require full testsuite to be run
# run only "main" suite
%global last_tested_version 11.8.6
# Set to 1 to force run the testsuite even if it was already tested in current version
%global force_run_testsuite 0

# Filtering: https://docs.fedoraproject.org/en-US/packaging-guidelines/AutoProvidesAndRequiresFiltering/
%global __requires_exclude ^perl\\((hostnames|lib::mtr|lib::v1|mtr_|My::|wsrep)
%global __provides_exclude_from ^(%{_datadir}/(mysql|mariadb-test)/.*|%{_libdir}/%{majorname}/plugin/.*\\.so)$

# For some use cases we do not need some parts of the package. Set to "...with" to exclude
%bcond_with    clibrary
%bcond_with    config
%bcond_without embedded
%bcond_without devel
%bcond_without client
%bcond_without common
%bcond_without errmsg
%bcond_without backup

# Package 'galera' (which is a run-time requirement for 'mariadb-server-galera') is no longer built for i686 architecture in Fedora
%ifarch %{ix86}
%bcond_with galera
%else
%bcond_without galera
%endif

%if !0%{?flatpak}
%bcond_without test
%endif

# Page compression algorithms for various storage engines
%bcond_without lz4
%bcond_without bzip2
%bcond_without lzo
%bcond_without snappy
%bcond_without zstd
%if 0%{?fedora} || (0%{?oreon} >= 11)
%bcond_without lzma
%else
%bcond_with lzma
%endif

# Aditional SELinux rules from a standalone package 'mysql-selinux' (that holds rules shared between MariaDB and MySQL)
%bcond_without require_mysql_selinux

# For deep debugging we need to build binaries with extra debug info
%bcond_with    debug

# Authentication plugins
%bcond_without gssapi
%if !0%{?flatpak}
%bcond_without pam
%endif
%if 0%{?fedora} || (0%{?oreon} >= 11)
# MariaDB upstream packages this as a separate subpackage
%bcond_without hashicorp
%else
%bcond_with hashicorp
%endif

# The Open Query GRAPH engine (OQGRAPH) is a computation engine allowing
# hierarchies and more complex graph structures to be handled in a relational fashion
%bcond_without oqgraph

# Other plugins
# S3 storage engine
#   https://mariadb.com/kb/en/s3-storage-engine/
%if 0%{?fedora} || (0%{?oreon} >= 11)
%bcond_without cracklib
%bcond_without connect
%bcond_without sphinx
%bcond_without s3
%else
%bcond_with cracklib
%bcond_with connect
%bcond_with sphinx
%bcond_with s3
%endif

# Mroonga engine
#   https://mariadb.com/kb/en/mariadb/about-mroonga/
#   Current version in MariaDB, 7.07, only supports the x86_64
#   Mroonga upstream warns about using 32-bit package: http://mroonga.org/docs/install.html
# RocksDB engine
#   https://mariadb.com/kb/en/library/about-myrocks-for-mariadb/
#   RocksDB engine is available only for x86_64
#   RocksDB may be built with jemalloc, if specified in CMake
%ifarch x86_64
%if 0%{?fedora} || (0%{?oreon} >= 11)
%bcond_without mroonga
%bcond_without rocksdb
%else
%bcond_with mroonga
%bcond_with rocksdb
%endif
%endif


%global selinuxtype targeted

# MariaDB 10.0 and later requires pcre >= 10.34, otherwise we need to use
# the bundled library, since the package cannot be build with older version
#   https://mariadb.com/kb/en/pcre/
%bcond bundled_pcre 0
%if %{with bundled_pcre}
%global pcre_bundled_version 10.45
%endif

# To avoid issues with a breaking change in FMT library, bundle it on systems where FMT wasn't fixed yet
# See mariadb-libfmt.patch for detailed description.
# As the breaking issues are no longer present in fedora 41
# and higher, this issue only remains in rhel
%if 0%{?rhel} && 0%{?rhel} < 11 || (0%{?oreon} >= 11)
%bcond bundled_fmt 1
%else
%bcond bundled_fmt 0
%endif

%if %{with bundled_fmt}
%global fmt_bundled_version 12.1.0
%endif

# Include systemd files
%global daemon_name      %{majorname}
%global daemon_no_prefix %{majorname}

# We define some system's well known locations here so we can use them easily
# later when building to another location (like SCL)
%global logrotateddir    %{_sysconfdir}/logrotate.d
%global logfiledir       %{_localstatedir}/log/%{daemon_name}
%global logfile          %{logfiledir}/%{daemon_name}.log
# Directory for storing pid file
%global pidfiledir       %{_rundir}/%{daemon_name}
# Defining where database data live
%global dbdatadir        %{_localstatedir}/lib/mysql



# Set explicit conflicts with 'mysql' packages
%bcond_without conflicts_mysql

# Make long macros shorter
%global sameevr   %{epoch}:%{version}-%{release}

Name:             %{majorname}%{majorversion}
Version:          %{package_version}
Release:          2%{?with_debug:.debug}%{?dist}
Epoch:            3

Summary:          A very fast and robust SQL database server
URL:              http://mariadb.org
License:          ( GPL-2.0-only OR Apache-2.0 ) AND ( GPL-2.0-or-later OR Apache-2.0 ) AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-4.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later AND ( GPL-3.0-or-later WITH Bison-exception-2.2 ) AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND OpenSSL AND MIT AND OFL-1.1 AND CC0-1.0 AND PHP-3.0 AND PHP-3.01 AND zlib AND dtoa AND FSFAP AND blessing AND Info-ZIP AND Boehm-GC

Source0:        https://downloads.mariadb.org/interstitial/mariadb-%{version}/source/mariadb-%{version}.tar.gz
%if %{with bundled_fmt}
Source1:        https://github.com/fmtlib/fmt/releases/download/%{fmt_bundled_version}/fmt-%{fmt_bundled_version}.zip
%endif
Source2:        mysql_config_multilib.sh
Source3:        my.cnf.in
%if %{with bundled_pcre}
Source4:        https://github.com/PCRE2Project/pcre2/releases/download/pcre2-%{pcre_bundled_version}/pcre2-%{pcre_bundled_version}.zip
%endif
Source6:        README.mariadb-docs
Source8:        README.wsrep_sst_rsync_tunnel
Source10:        mariadb.tmpfiles.d.in
Source11:        mysql.service.in
Source12:        mariadb-prepare-db-dir.sh
Source14:        mariadb-check-socket.sh
Source15:        mariadb-scripts-common.sh
Source16:        mariadb-check-upgrade.sh
Source18:        mysql@.service.in
Source50:        rh-skipped-tests-base.list
Source51:        rh-skipped-tests-arm.list
Source52:        rh-skipped-tests-s390.list
Source53:        rh-skipped-tests-ppc.list
# Red Hat OpenStack scripts:
#   Clustercheck:
#     Maintainer:
#       Damien Ciabrini <dciabrin@redhat.com>
#     Source / Upstream:
#       Damien; based on https://github.com/olafz/percona-clustercheck
#       not updated in 5 years; low-effort maintenance
#     Purpose:
#       In Openstack, galera is accessed like an A/P database, we have a
#       load balancer (haproxy) that drives traffic to a single node and
#       performs failover when the galera node monitor fails.
#       clustercheck.sh is the monitoring script that is being called remotely
#       by haproxy. It is a glue between haproxy and the local galera node that
#       can run SQL commands to check whether the local galera is connected to the galera cluster.
#     Proposed to MariaDB upstream: https://jira.mariadb.org/browse/MDEV-12442
#       General upstream response was slightly positive
Source70:        clustercheck.sh
Source71:        LICENSE.clustercheck

# Upstream said: "Generally MariaDB has more allows to allow for xtradb sst mechanism".
# https://jira.mariadb.org/browse/MDEV-12646
Source72:        mariadb-server-galera.cil

# Script to support encrypted rsync transfers when SST is required between nodes.
# https://github.com/dciabrin/wsrep_sst_rsync_tunnel/blob/master/wsrep_sst_rsync_tunnel
Source73:        wsrep_sst_rsync_tunnel

#   Patch4: Use the correct log file pathname for Red Hat installations
Patch4:           %{majorname}-logrotate.patch
#   Patch7: add to the CMake file all files where we want macros to be expanded
Patch7:           %{majorname}-scripts.patch
#   Patch9: pre-configure to comply with guidelines
Patch9:           %{majorname}-ownsetup.patch
#   Patch14: make MTR port calculation reasonably predictable
Patch14:          %{majorname}-mtr.patch
#   Patch15: mark RISC-V64 as 64-bit architecture
Patch15:          mark-RISC-V64-as-64-bit-architecture.patch

Patch16:          %{majorname}-federated.patch

Patch17:          upstream_87309d3d4bb8f48910d05b0ca5ee989bcdd6b053.patch

# This macro is used for package/sub-package names in the entire specfile
%if %?mariadb_default
%global pkgname %{majorname}
%package -n %{pkgname}
Summary: A very fast and robust SQL database server
%else
%global pkgname %{name}
%endif

BuildRequires:    make cmake gcc-c++
BuildRequires:    libxcrypt-devel
BuildRequires:    multilib-rpm-config
BuildRequires:    selinux-policy-devel
BuildRequires:    systemd systemd-devel

# Page compression algorithms for various storage engines
BuildRequires:    zlib-devel
%{?with_lz4:BuildRequires:    lz4-devel >= 1.6}
%{?with_bzip2:BuildRequires:    bzip2-devel}
%{?with_lzma:BuildRequires:    xz-devel}
%{?with_lzo:BuildRequires:    lzo-devel}
%{?with_snappy:BuildRequires:    snappy-devel}
%{?with_zstd:BuildRequires:    libzstd-devel}

# asynchornous operations stuff; needed also for wsrep API
BuildRequires:    libaio-devel
# commands history features
BuildRequires:    libedit-devel
# CLI graphic; needed also for wsrep API
BuildRequires:    ncurses-devel
# debugging stuff
BuildRequires:    systemtap-sdt-devel
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 11 || (0%{?oreon} >= 11)
BuildRequires:    systemtap-sdt-dtrace
%endif
# Bison SQL parser; needed also for wsrep API
BuildRequires:    bison >= 2.4
BuildRequires:    bison-devel >= 2.4

%{?with_debug:BuildRequires:    valgrind-devel}

# use either new enough version of pcre2 or provide bundles(pcre2)
%{?with_bundled_pcre:Provides: bundled(pcre2) = %{pcre_bundled_version}}
%{!?with_bundled_pcre:BuildRequires: pcre2-devel >= 10.34 pkgconf}
# Few utilities needs Perl
BuildRequires:    perl-interpreter
BuildRequires:    perl-generators
# Some tests requires python
BuildRequires:    python3
# Tests requires time and ps and some perl modules
BuildRequires:    procps
BuildRequires:    time
BuildRequires:    perl(base)
BuildRequires:    perl(Cwd)
BuildRequires:    perl(Data::Dumper)
BuildRequires:    perl(English)
BuildRequires:    perl(Env)
BuildRequires:    perl(Errno)
BuildRequires:    perl(Exporter)
BuildRequires:    perl(Fcntl)
BuildRequires:    perl(File::Basename)
BuildRequires:    perl(File::Copy)
BuildRequires:    perl(File::Find)
BuildRequires:    perl(File::Spec)
BuildRequires:    perl(File::Spec::Functions)
BuildRequires:    perl(File::Temp)
BuildRequires:    perl(Getopt::Long)
BuildRequires:    perl(IO::File)
BuildRequires:    perl(IO::Handle)
BuildRequires:    perl(IO::Select)
BuildRequires:    perl(IO::Socket)
BuildRequires:    perl(IO::Socket::INET)
BuildRequires:    perl(IPC::Open3)
BuildRequires:    perl(lib)
BuildRequires:    perl(Memoize)
BuildRequires:    perl(POSIX)
BuildRequires:    perl(Socket)
BuildRequires:    perl(strict)
BuildRequires:    perl(Symbol)
BuildRequires:    perl(Sys::Hostname)
BuildRequires:    perl(Term::ANSIColor)
BuildRequires:    perl(Test::More)
BuildRequires:    perl(Time::HiRes)
BuildRequires:    perl(Time::localtime)
BuildRequires:    perl(warnings)
# for running some openssl tests rhbz#1189180
BuildRequires:    openssl openssl-devel

%{!?with_bundled_fmt:BuildRequires: fmt-devel >= 11.1.4-1}

Requires:         bash coreutils grep

Requires:         %{pkgname}-common = %{sameevr}

%if %{with clibrary}
# Explicit EVR requirement for -libs is needed for RHBZ#1406320
Requires:         %{pkgname}-libs%{?_isa} = %{sameevr}
%else
# If not built with client library in this package, use connector-c
Requires:         mariadb-connector-c >= 3.0
%endif

# Recommend additional client utils that require Perl
Recommends:       %{pkgname}-client-utils

Suggests:         %{pkgname}-server%{?_isa} = %{sameevr}

%{?with_conflicts_mysql:Conflicts: mysql-any}
# Explicitly disallow combination mariadb + mysql-server
%{?with_conflicts_mysql:Conflicts: mysql-server-any}

%define conflict_with_other_streams() %{expand:\
Provides: %{majorname}%{?1:-%{1}}-any\
Conflicts: %{majorname}%{?1:-%{1}}-any\
}

# Provide also mariadbXX.XX if default
%if %?mariadb_default
%define mariadbXX_if_default() %{expand:\
Provides: mariadb%{majorversion}%{?1:-%{1}} = %{sameevr}\
Provides: mariadb%{majorversion}%{?1:-%{1}}%{?_isa} = %{sameevr}\
}
%else
%define mariadbXX_if_default() %{nil}
%endif

%define virtual_conflicts_and_provides() %{expand:\
%conflict_with_other_streams %{**}\
%mariadbXX_if_default %{**}\
}

%virtual_conflicts_and_provides

%description
MariaDB is a community developed fork from MySQL - a multi-user, multi-threaded
SQL database server. It is a client/server implementation consisting of
a server daemon (mariadbd) and many different client programs and libraries.
The base package contains the standard MariaDB/MySQL client programs and
utilities.

%if %?mariadb_default
%description -n %{pkgname}
MariaDB is a community developed fork from MySQL - a multi-user, multi-threaded
SQL database server. It is a client/server implementation consisting of
a server daemon (mariadbd) and many different client programs and libraries.
The base package contains the standard MariaDB/MySQL client programs and
utilities.
%endif

%package          -n %{pkgname}-client-utils
BuildArch:        noarch
Summary:          Non-essential client utilities for MariaDB/MySQL applications
Requires:         %{pkgname} = %{sameevr}
Requires:         perl(DBI)

# Only conflicts, provides would add %%{_isa} provides for noarch,
# which is not wanted
%conflict_with_other_streams client-utils

%description      -n %{pkgname}-client-utils
This package contains all non-essential client utilities and scripts for
managing databases. It also contains all utilities requiring Perl and it is the
only MariaDB sub-package with the corresponding server-utils one, except test
subpackage, that depends on Perl.


%if %{with clibrary}
%package          -n %{pkgname}-libs
Summary:          The shared libraries required for MariaDB/MySQL clients
Requires:         %{pkgname}-common = %{sameevr}

%virtual_conflicts_and_provides libs

%{?with_conflicts_mysql:Conflicts: mysql-libs-any}

%description      -n %{pkgname}-libs
The mariadb-libs package provides the essential shared libraries for any
MariaDB/MySQL client program or interface. You will need to install this
package to use any other MariaDB package or any clients that need to connect
to a MariaDB/MySQL server.
%endif


# At least main config file /etc/my.cnf is shared for client and server part
# Since we want to support combination of different client and server
# implementations (e.g. mariadb library and community-mysql server),
# we need the config file(s) to be in a separate package, so no extra packages
# are pulled, because these would likely conflict.
# More specifically, the dependency on the main configuration file (/etc/my.cnf)
# is supposed to be defined as Requires: /etc/my.cnf rather than requiring
# a specific package, so installer app can choose whatever package fits to
# the transaction.
%if %{with config}
%package          -n %{pkgname}-config
Summary:          The config files required by server and client

%virtual_conflicts_and_provides config

%description      -n %{pkgname}-config
The package provides the config file my.cnf and my.cnf.d directory used by any
MariaDB or MySQL program. You will need to install this package to use any
other MariaDB or MySQL package if the config files are not provided in the
package itself.
%endif


%if %{with common}
%package          -n %{pkgname}-common
Summary:          The shared files required by server and client
BuildArch:        noarch
%if 0%{?flatpak}
Requires:         mariadb-connector-c-config
%else
Requires:         %{_sysconfdir}/my.cnf
%endif

# Only conflicts, provides would add %%{_isa} provides for noarch,
# which is not wanted
%conflict_with_other_streams common

%description      -n %{pkgname}-common
The package provides the essential shared files for any MariaDB program.
You will need to install this package to use any other MariaDB package.
%endif


%if %{with errmsg}
%package          -n %{pkgname}-errmsg
Summary:          The error messages files required by server and embedded
BuildArch:        noarch
Requires:         %{pkgname}-common = %{sameevr}

# Only conflicts, provides would add %%{_isa} provides for noarch,
# which is not wanted
%conflict_with_other_streams errmsg

%description      -n %{pkgname}-errmsg
The package provides error messages files for the MariaDB daemon and the
embedded server. You will need to install this package to use any of those
MariaDB packages.
%endif


%if %{with galera}
%package          -n %{pkgname}-server-galera
Summary:          The configuration files and scripts for galera replication
Requires:         %{pkgname}-common = %{sameevr}
Requires:         %{pkgname}-server%{?_isa} = %{sameevr}
Requires:         galera >= 26.4.3
BuildRequires:    selinux-policy-%{selinuxtype}
Requires:         selinux-policy-%{selinuxtype}
Requires(post):   (libselinux-utils if selinux-policy-%{selinuxtype})
Requires(post):   (policycoreutils if selinux-policy-%{selinuxtype})
Requires(post):   (policycoreutils-python-utils if selinux-policy-%{selinuxtype})
# wsrep requirements
Requires:         lsof
# Default wsrep_sst_method
Requires:         rsync

%virtual_conflicts_and_provides server-galera

%description      -n %{pkgname}-server-galera
MariaDB is a multi-user, multi-threaded SQL database server. It is a
client/server implementation consisting of a server daemon (mariadbd)
and many different client programs and libraries. This package contains
added files to allow MariaDB server to operate as a Galera cluster
member. MariaDB is a community developed fork originally from MySQL.
%endif


%package          -n %{pkgname}-server
Summary:          The MariaDB server and related files

%if %{with hashicorp}
BuildRequires:    curl-devel
%endif

Requires:         %{pkgname}%{?_isa} = %{sameevr}
Requires:         %{pkgname}-common = %{sameevr}
Requires:         %{pkgname}-errmsg = %{sameevr}
Recommends:       %{pkgname}-server-utils = %{sameevr}
Recommends:       %{pkgname}-backup%{?_isa} = %{sameevr}
%{?with_cracklib:Recommends:   %{pkgname}-cracklib-password-check%{?_isa} = %{sameevr}}
%{?with_gssapi:Recommends:     %{pkgname}-gssapi-server%{?_isa} = %{sameevr}}
%{?with_rocksdb:Suggests:      %{pkgname}-rocksdb-engine%{?_isa} = %{sameevr}}
%{?with_sphinx:Suggests:       %{pkgname}-sphinx-engine%{?_isa} = %{sameevr}}
%{?with_oqgraph:Suggests:      %{pkgname}-oqgraph-engine%{?_isa} = %{sameevr}}
%{?with_connect:Suggests:      %{pkgname}-connect-engine%{?_isa} = %{sameevr}}
%{?with_pam:Suggests:          %{pkgname}-pam%{?_isa} = %{sameevr}}

%{?with_bundled_fmt:Provides: bundled(fmt) = %{fmt_bundled_version}}

Suggests:         mytop
Suggests:         logrotate

%if 0%{?flatpak}
Requires:         mariadb-connector-c-config
%else
Requires:         %{_sysconfdir}/my.cnf
Requires:         %{_sysconfdir}/my.cnf.d
%endif

%virtual_conflicts_and_provides server

# Additional SELinux rules (common for MariaDB & MySQL) shipped in a separate package
# For cases, where we want to fix a SELinux issues in MariaDB sooner than patched selinux-policy-targeted package is released
%if %{with require_mysql_selinux}
# The *-selinux package should only be required on SELinux enabled systems. Therefore the following rich dependency syntax should be used:
Requires:         (mysql-selinux >= 1.0.10 if selinux-policy-%{selinuxtype})
# This ensures that the *-selinux package and all its dependencies are not pulled into containers and other systems that do not use SELinux.
# 
%endif

Requires:         coreutils
# We require this to be present for %%{_tmpfilesdir}
Requires:         systemd
# Make sure it's there when scriptlets run, too
%{?systemd_requires}
# RHBZ#1496131; use 'iproute' instead of 'net-tools'
Requires:         iproute
# The 'wsrep_sst_common' and 'wsrep_sst_rsync_tunnel' calls 'which' utility
%{?with_galera:Requires: which}

%{?with_conflicts_mysql:Conflicts: mysql-server-any}
# Explicitly disallow combination mariadb-server + mysql
%{?with_conflicts_mysql:Conflicts: mysql-any}

%description      -n %{pkgname}-server
MariaDB is a multi-user, multi-threaded SQL database server. It is a
client/server implementation consisting of a server daemon (mariadbd)
and many different client programs and libraries. This package contains
the MariaDB server and some accompanying files and directories.
MariaDB is a community developed fork from MySQL.


%if %{with oqgraph}
%package          -n %{pkgname}-oqgraph-engine
Summary:          The Open Query GRAPH engine for MariaDB
Requires:         %{pkgname}-server%{?_isa} = %{sameevr}
# boost and Judy required for oograph
BuildRequires:    boost-devel >= 1.40.0
BuildRequires:    Judy-devel

%virtual_conflicts_and_provides oqgraph-engine

%description      -n %{pkgname}-oqgraph-engine
The package provides Open Query GRAPH engine (OQGRAPH) as plugin for MariaDB
database server. OQGRAPH is a computation engine allowing hierarchies and more
complex graph structures to be handled in a relational fashion. In a nutshell,
tree structures and friend-of-a-friend style searches can now be done using
standard SQL syntax, and results joined onto other tables.
%endif


%if %{with connect}
%package          -n %{pkgname}-connect-engine
Summary:          The CONNECT storage engine for MariaDB
Requires:         %{pkgname}-server%{?_isa} = %{sameevr}

# As per https://jira.mariadb.org/browse/MDEV-21450
BuildRequires:    libxml2-devel

%virtual_conflicts_and_provides connect-engine

%description      -n %{pkgname}-connect-engine
The CONNECT storage engine enables MariaDB to access external local or
remote data (MED). This is done by defining tables based on different data
types, in particular files in various formats, data extracted from other DBMS
or products (such as Excel), or data retrieved from the environment
(for example DIR, WMI, and MAC tables).
%endif


%if %{with backup}
%package          -n %{pkgname}-backup
Summary:          The mariabackup tool for physical online backups
Requires:         %{pkgname}-server%{?_isa} = %{sameevr}
BuildRequires:    libarchive-devel

%virtual_conflicts_and_provides backup

%description      -n %{pkgname}-backup
MariaDB Backup is an open source tool provided by MariaDB for performing
physical online backups of InnoDB, Aria and MyISAM tables.
For InnoDB, "hot online" backups are possible.
%endif


%if %{with rocksdb}
%package          -n %{pkgname}-rocksdb-engine
Summary:          The RocksDB storage engine for MariaDB
Requires:         %{pkgname}-server%{?_isa} = %{sameevr}
# The version of rocksdb provided is not specified because the mariadb
# upstream provides it as a submodule, which is linked in their github
# https://github.com/MariaDB/server/ inside storage/rocksdb
# the commits linked here don't match the releases made by the rocksdb
# upstream: https://github.com/facebook/rocksdb/
# therefore the release specified here would be rough at best.
# A rough release can also be found inside the source tarball
# inside the storage/rocksdb/rocksdb/include/rocksdb/version.h file
# but it does not match the real release every time
Provides:         bundled(rocksdb)
Conflicts:        rocksdb-tools

%virtual_conflicts_and_provides rocksdb-engine

%description      -n %{pkgname}-rocksdb-engine
The RocksDB storage engine is used for high performance servers on SSD drives.
%endif


%if %{with cracklib}
%package          -n %{pkgname}-cracklib-password-check
Summary:          The password strength checking plugin
Requires:         %{pkgname}-server%{?_isa} = %{sameevr}
BuildRequires:    cracklib-dicts cracklib-devel
Requires:         cracklib-dicts

BuildRequires:    selinux-policy-devel
Requires(post):   (libselinux-utils if selinux-policy-%{selinuxtype})
Requires(post):   (policycoreutils if selinux-policy-%{selinuxtype})
Requires(post):   (policycoreutils-python-utils if selinux-policy-%{selinuxtype})

%virtual_conflicts_and_provides cracklib-password-check

%description      -n %{pkgname}-cracklib-password-check
CrackLib is a password strength checking library. It is installed by default
in many Linux distributions and is invoked automatically (by pam_cracklib.so)
whenever the user login password is modified.
Now, with the cracklib_password_check password validation plugin, one can
also use it to check MariaDB account passwords.
%endif


%if %{with gssapi}
%package          -n %{pkgname}-gssapi-server
Summary:          GSSAPI authentication plugin for server
Requires:         %{pkgname}-server%{?_isa} = %{sameevr}
BuildRequires:    krb5-devel

%virtual_conflicts_and_provides gssapi-server

%description      -n %{pkgname}-gssapi-server
GSSAPI authentication server-side plugin for MariaDB for passwordless login.
This plugin includes support for Kerberos on Unix.
%endif


%if %{with pam}
%package          -n %{pkgname}-pam
Summary:          PAM authentication plugin for the MariaDB server

Requires:         %{pkgname}-server%{?_isa} = %{sameevr}
# This subpackage NEED the 'mysql' user/group (created during mariadb-server %%pre) to be available prior installation
Requires(pre):    %{pkgname}-server%{?_isa} = %{sameevr}

BuildRequires:    pam-devel

%virtual_conflicts_and_provides pam

%description      -n %{pkgname}-pam
PAM authentication server-side plugin for MariaDB.
%endif


%if %{with sphinx}
# MariaDB upstream packages this inside the client sub-package
%package          -n %{pkgname}-sphinx-engine
Summary:          The Sphinx storage engine for MariaDB
Requires:         %{pkgname}-server%{?_isa} = %{sameevr}
BuildRequires:    sphinx libsphinxclient-devel
Requires:         sphinx libsphinxclient

%virtual_conflicts_and_provides sphinx-engine

%description      -n %{pkgname}-sphinx-engine
The Sphinx storage engine for MariaDB.
%endif


%if %{with s3}
%package          -n %{pkgname}-s3-engine
Summary:          The S3 storage engine for MariaDB
Requires:         %{pkgname}-server%{?_isa} = %{sameevr}

BuildRequires:    curl-devel

%virtual_conflicts_and_provides s3-engine

%description      -n %{pkgname}-s3-engine
The S3 read only storage engine allows archiving MariaDB tables in Amazon S3,
or any third-party public or private cloud that implements S3 API,
but still have them accessible for reading in MariaDB.
%endif


%package          -n %{pkgname}-server-utils
BuildArch:        noarch
Summary:          Non-essential server utilities for MariaDB/MySQL applications
Requires:         %{pkgname}-server = %{sameevr}
# mysqlhotcopy needs DBI/DBD support
Requires:         perl(DBI) perl(DBD::MariaDB)

# Only conflicts, provides would add %%{_isa} provides for noarch,
# which is not wanted
%conflict_with_other_streams server-utils

%{?with_conflicts_mysql:Conflicts: mysql-server-any}

%description      -n %{pkgname}-server-utils
This package contains all non-essential server utilities and scripts for
managing databases. It also contains all utilities requiring Perl and it is
the only MariaDB sub-package with the corresponding client-utils one, except
test subpackage, that depends on Perl.


%if %{with devel}
%package          -n %{pkgname}-devel
Summary:          Files for development of MariaDB/MySQL applications
%{?with_clibrary:Requires:         %{pkgname}-libs%{?_isa} = %{sameevr}}
Requires:         openssl-devel
%if %{without clibrary}
Requires:         mariadb-connector-c-devel >= 3.0
%endif

%virtual_conflicts_and_provides devel

%{?with_conflicts_mysql:Conflicts: mysql-devel-any}

%description      -n %{pkgname}-devel
MariaDB is a multi-user, multi-threaded SQL database server.
MariaDB is a community developed branch of MySQL.
%if %{with clibrary}
This package contains everything needed for developing MariaDB/MySQL client
and server plugins and applications.
%else
This package contains everything needed for developing MariaDB/MySQL server
plugins and applications. For developing client applications, use
mariadb-connector-c package.
%endif
%endif


%if %{with embedded}
%package          -n %{pkgname}-embedded
Summary:          MariaDB as an embeddable library
Requires:         %{pkgname}-common = %{sameevr}
Requires:         %{pkgname}-errmsg = %{sameevr}

%virtual_conflicts_and_provides embedded

%description      -n %{pkgname}-embedded
MariaDB is a multi-user, multi-threaded SQL database server. This
package contains a version of the MariaDB server that can be embedded
into a client application instead of running as a separate process.
MariaDB is a community developed fork from MySQL.


%package          -n %{pkgname}-embedded-devel
Summary:          Development files for MariaDB as an embeddable library
Requires:         %{pkgname}-embedded%{?_isa} = %{sameevr}
Requires:         %{pkgname}-devel%{?_isa} = %{sameevr}
# embedded-devel should require libaio-devel (rhbz#1290517)
Requires:         libaio-devel

%virtual_conflicts_and_provides embedded-devel

%description      -n %{pkgname}-embedded-devel
MariaDB is a multi-user, multi-threaded SQL database server.
MariaDB is a community developed fork from MySQL.
This package contains files needed for developing and testing with
the embedded version of the MariaDB server.
%endif


%if %{with test}
%package          -n %{pkgname}-test
Summary:          The test suite distributed with MariaDB
Requires:         %{pkgname}%{?_isa} = %{sameevr}
Requires:         %{pkgname}-common = %{sameevr}
Requires:         %{pkgname}-server%{?_isa} = %{sameevr}
Requires:         patch
Requires:         perl(Env)
Requires:         perl(Exporter)
Requires:         perl(Fcntl)
Requires:         perl(File::Temp)
Requires:         perl(Data::Dumper)
Requires:         perl(Getopt::Long)
Requires:         perl(IPC::Open3)
Requires:         perl(Socket)
Requires:         perl(Sys::Hostname)
Requires:         perl(Test::More)
Requires:         perl(Time::HiRes)

%virtual_conflicts_and_provides test

%{?with_conflicts_mysql:Conflicts: mysql-test-any}

%description      -n %{pkgname}-test
MariaDB is a multi-user, multi-threaded SQL database server.
MariaDB is a community developed fork from MySQL.
This package contains the regression test suite distributed with the MariaDB
sources.
%endif


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%if %{with bundled_pcre}
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
%endif
%setup -q -n %{majorname}-%{version}

# Remove bundled code that is unused (all cases in which we use the system version of the library instead)
# as required by https://docs.fedoraproject.org/en-US/packaging-guidelines/#bundling
rm -r zlib libmariadb/external/zlib
rm -r win libmariadb/win
rm -r extra/wolfssl
rm -r storage/columnstore
rm -r debian

%if %{with bundled_fmt}
mkdir -p %{_vpath_builddir}/extra/libfmt/
mv %{SOURCE1} %{_vpath_builddir}/extra/libfmt/
sed -i 's|"https://github.com/fmtlib/fmt/releases/download/%{fmt_bundled_version}/fmt-%{fmt_bundled_version}.zip"|"file:///%{_vpath_builddir}/extra/libfmt/fmt-%{fmt_bundled_version}.zip"|' cmake/libfmt.cmake
%endif
%if %{with bundled_pcre}
mkdir -p %{_vpath_builddir}/extra/pcre2/
mv %{SOURCE4} %{_vpath_builddir}/extra/pcre2/
%endif

# Remove JAR files that upstream puts into tarball
find . -name "*.jar" -type f -exec rm --verbose -f {} \;
# Remove testsuite for the mariadb-connector-c
rm -r libmariadb/unittest
%if %{without rocksdb}
rm -r storage/rocksdb/
%endif


%patch -P4 -p1
%patch -P7 -p1
%patch -P9 -p1
%patch -P14 -p1
%patch -P15 -p1
%patch -P16 -p1
%patch -P17 -p1

# generate a list of tests that fail, but are not disabled by upstream
cat %{SOURCE50} | tee -a mysql-test/unstable-tests

# disable some tests failing on different architectures
%ifarch %{arm} aarch64
cat %{SOURCE51} | tee -a mysql-test/unstable-tests
%endif

%ifarch s390 s390x
cat %{SOURCE52} | tee -a mysql-test/unstable-tests
%endif

%ifarch ppc ppc64 ppc64p7 ppc64le
cat %{SOURCE53} | tee -a mysql-test/unstable-tests
%endif

cp %{SOURCE2} %{SOURCE3} %{SOURCE10} %{SOURCE11} %{SOURCE12} \
   %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE18} %{SOURCE70} %{SOURCE73} scripts

# Create a sysusers.d config file
# We no longer enforce the hardcoded UID/GID 27.
cat > support-files/%{majorname}.sysusers.conf << EOF
u mysql 27 'MariaDB and MySQL Server' %{dbdatadir} -
EOF

%if %{with galera}
# prepare selinux policy
sed 's/mariadb-server-galera/%{majorname}-server-galera/' %{SOURCE72} > %{majorname}-server-galera.cil
%endif


# Get version of PCRE, that upstream use
pcre_version=`grep -e "URL \"" cmake/pcre.cmake | sed -r "s;.*pcre2-([[:digit:]]+\.[[:digit:]]+).*;\1;" `

# Check if the PCRE version in macro 'pcre_bundled_version', used in Provides: bundled(...), is the same version as upstream actually bundles
%if %{with bundled_pcre}
if [ %{pcre_bundled_version} != "$pcre_version" ] ; then
  echo -e "\n Error: Bundled PCRE version is not correct. \n\tBundled version number: %{pcre_bundled_version} \n\tUpstream version number: $pcre_version\n"
  exit 1
fi
%else
# Check if the PCRE version that upstream use, is the same as the one present in system
pcre_system_version=`pkgconf /usr/%{_lib}/pkgconfig/libpcre2-*.pc --modversion 2>/dev/null | head -n 1`

if [ "$pcre_system_version" != "$pcre_version" ] ; then
  echo -e "\n Warning: Error: System version of PCRE differs from the version used by the MariaDB upstream. \n\tSystem version number: $pcre_system_version \n\tUpstream version number: $pcre_version\n"
fi
%endif



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


# Adjust the compliation flags:
# First initialize the distribution default values
%{set_build_flags}
# Add custom tweaks
CFLAGS="$CFLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE"
# Force the 'PIC' mode so that we can build libmysqld.so
CFLAGS="$CFLAGS -fPIC"

# When making a debug build, remove all optimizations
%if %{with debug}
# -D_FORTIFY_SOURCE requires optimizations enabled. Disable the fortify.
%undefine _fortify_level
CFLAGS=`echo "$CFLAGS" | sed -r 's/-O[0123]//'`
CFLAGS="$CFLAGS -O0 -g"
%endif

# Apply the updated values
CXXFLAGS="$CFLAGS"; CPPFLAGS="$CFLAGS"; export CFLAGS CXXFLAGS CPPFLAGS


# The INSTALL_xxx macros have to be specified relative to CMAKE_INSTALL_PREFIX
# so we can't use %%{_datadir} and so forth here.
%cmake \
         -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
         -DBUILD_CONFIG=mysql_release \
         -DFEATURE_SET="community" \
         -DWITH_SBOM=0 \
         -DINSTALL_LAYOUT=RPM \
         -DDAEMON_NAME="%{daemon_name}" \
         -DDAEMON_NO_PREFIX="%{daemon_no_prefix}" \
         -DLOG_LOCATION="%{logfile}" \
         -DPID_FILE_DIR="%{pidfiledir}" \
         -DNICE_PROJECT_NAME="MariaDB" \
         -DRPM="%{?rhel:rhel%{rhel}}%{!?rhel:fedora%{fedora}}" \
         -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
         -DINSTALL_SYSCONFDIR="%{_sysconfdir}" \
         -DINSTALL_SYSCONF2DIR="%{_sysconfdir}/my.cnf.d" \
         -DINSTALL_DOCDIR="share/doc/%{majorname}" \
         -DINSTALL_DOCREADMEDIR="share/doc/%{majorname}" \
         -DINSTALL_INCLUDEDIR=include/mysql \
         -DINSTALL_INFODIR=share/info \
         -DINSTALL_LIBDIR="%{_lib}" \
         -DINSTALL_MANDIR=share/man \
         -DINSTALL_MYSQLSHAREDIR=share/%{majorname} \
         -DINSTALL_MYSQLTESTDIR=%{?with_test:share/mariadb-test}%{!?with_test:} \
         -DINSTALL_PLUGINDIR="%{_lib}/%{majorname}/plugin" \
         -DINSTALL_SBINDIR=libexec \
         -DINSTALL_SCRIPTDIR=bin \
         -DINSTALL_SUPPORTFILESDIR=share/%{majorname} \
         -DMYSQL_DATADIR="%{dbdatadir}" \
         -DTMPDIR=%{_localstatedir}/tmp \
         -DINSTALL_SYSTEMD_TMPFILESDIR="" \
         -DINSTALL_SYSTEMD_SYSUSERSDIR="" \
         -DGRN_DATA_DIR=share/%{majorname}-server/groonga \
         -DGROONGA_NORMALIZER_MYSQL_PROJECT_NAME=%{majorname}-server/groonga-normalizer-mysql \
         -DENABLED_LOCAL_INFILE=ON \
         -DENABLE_DTRACE=ON \
         -DSECURITY_HARDENED=OFF \
         -DWITH_PCRE=%{?with_bundled_pcre:bundled}%{!?with_bundled_pcre:system} \
         -DWITH_WSREP=%{?with_galera:ON}%{!?with_galera:OFF} \
         -DWITH_INNODB_DISALLOW_WRITES=%{?with_galera:ON}%{!?with_galera:OFF} \
         -DWITH_EMBEDDED_SERVER=%{?with_embedded:ON}%{!?with_embedded:OFF} \
         -DWITH_MARIABACKUP=%{?with_backup:ON}%{!?with_backup:NO} \
         -DWITH_UNIT_TESTS=%{?with_test:ON}%{!?with_test:NO} \
         -DCONC_WITH_SSL=%{?with_clibrary:ON}%{!?with_clibrary:NO} \
         -DWITH_SSL=system \
         -DWITH_ZLIB=system \
         -DWITH_LIBFMT=%{?with_bundled_fmt:bundled}%{!?with_bundled_fmt:system} \
         -DPLUGIN_PROVIDER_LZ4=%{?with_lz4:DYNAMIC}%{!?with_lz4:NO} \
         -DWITH_ROCKSDB_LZ4=%{?with_lz4:ON}%{!?with_lz4:OFF} \
         -DPLUGIN_PROVIDER_BZIP2=%{?with_bzip2:DYNAMIC}%{!?with_bzip2:NO} \
         -DWITH_ROCKSDB_BZip2=%{?with_bzip2:ON}%{!?with_bzip2:OFF} \
         -DPLUGIN_PROVIDER_LZMA=%{?with_lzma:DYNAMIC}%{!?with_lzma:NO} \
         \
         -DPLUGIN_MROONGA=%{?with_mroonga:DYNAMIC}%{!?with_mroonga:NO} \
         -DPLUGIN_OQGRAPH=%{?with_oqgraph:DYNAMIC}%{!?with_oqgraph:NO} \
         -DPLUGIN_CRACKLIB_PASSWORD_CHECK=%{?with_cracklib:DYNAMIC}%{!?with_cracklib:NO} \
         -DPLUGIN_ROCKSDB=%{?with_rocksdb:DYNAMIC}%{!?with_rocksdb:NO} \
         -DPLUGIN_SPHINX=%{?with_sphinx:DYNAMIC}%{!?with_sphinx:NO} \
         -DPLUGIN_CONNECT=%{?with_connect:DYNAMIC}%{!?with_connect:NO} \
         -DPLUGIN_S3=%{?with_s3:DYNAMIC}%{!?with_s3:NO} \
         -DPLUGIN_AUTH_GSSAPI=%{?with_gssapi:DYNAMIC}%{!?with_gssapi:NO} \
         -DPLUGIN_AUTH_PAM=%{?with_pam:YES}%{!?with_pam:NO} \
         -DPLUGIN_AUTH_PAM_V1=%{?with_pam:DYNAMIC}%{!?with_pam:NO} \
         -DPLUGIN_COLUMNSTORE=NO \
         -DPLUGIN_CLIENT_ED25519=OFF \
         -DPLUGIN_CACHING_SHA2_PASSWORD=%{?with_clibrary:DYNAMIC}%{!?with_clibrary:OFF} \
         -DPLUGIN_AWS_KEY_MANAGEMENT=OFF \
         -DCONNECT_WITH_MONGO=OFF \
         -DCONNECT_WITH_JDBC=OFF \
         -DPLUGIN_HASHICORP_KEY_MANAGEMENT=%{?with_hashicorp:DYNAMIC}%{!?with_hashicorp:NO} \
%{?with_debug: -DCMAKE_BUILD_TYPE=Debug -DWITH_ASAN=OFF -DWITH_INNODB_EXTRA_DEBUG=ON -DWITH_VALGRIND=ON}

# The -DSECURITY_HARDENED is used to force a set of compilation flags for hardening
# The issue is that the MariaDB upstream level of hardening is lower than expected by Red Hat
# We disable this option to the default compilation flags (which have higher level of hardening) will be used

# Print all cached CMake options values; "-N" means to run in read-only mode; "-LAH" means "List Advanced Help" for each option
cmake -B %{_vpath_builddir} -N -LAH

%cmake_build


%install
%cmake_install

# multilib header support #1625157
for header in mysql/server/my_config.h mysql/server/private/config.h; do
%multilib_fix_c_header --file %{_includedir}/$header
done

ln -s mysql_config.1.gz %{buildroot}%{_mandir}/man1/mariadb_config.1.gz

# multilib support for shell scripts
# we only apply this to known Red Hat multilib arches, per bug #181335
if [ %multilib_capable ]
then
mv %{buildroot}%{_bindir}/mysql_config %{buildroot}%{_bindir}/mysql_config-%{__isa_bits}
install -p -m 0755 %{_vpath_builddir}/scripts/mysql_config_multilib %{buildroot}%{_bindir}/mysql_config
# Copy manual page for multilib mysql_config; https://jira.mariadb.org/browse/MDEV-11961
ln -s mysql_config.1 %{buildroot}%{_mandir}/man1/mysql_config-%{__isa_bits}.1
fi

# Logfile creation
mkdir -p %{buildroot}%{logfiledir}
chmod 0750 %{buildroot}%{logfiledir}
touch %{buildroot}%{logfile}

# PID file directory
# current setting in my.cnf is to use /var/run/mariadb for creating pid file,
# however since my.cnf is not updated by RPM if changed, we need to create mysqld
# as well because users can have odd settings in their /etc/my.cnf
mkdir -p %{buildroot}%{pidfiledir}

# DB datadir
install -p -m 0755 -d %{buildroot}%{dbdatadir}

%if %{with config}
install -D -p -m 0644 %{_vpath_builddir}/scripts/my.cnf %{buildroot}%{_sysconfdir}/my.cnf
%else
rm %{_vpath_builddir}/scripts/my.cnf
rm %{buildroot}%{_sysconfdir}/my.cnf
%endif

# use different config file name for each variant of server (mariadb / mysql)
mv %{buildroot}%{_sysconfdir}/my.cnf.d/server.cnf %{buildroot}%{_sysconfdir}/my.cnf.d/%{majorname}-server.cnf

# Remove upstream SysV init script and a symlink to that, we use systemd
rm %{buildroot}%{_libexecdir}/rcmysql
# Remove upstream Systemd service files
rm -r %{buildroot}%{_datadir}/%{majorname}/systemd

# install systemd unit files and scripts for handling server startup
install -D -p -m 644 %{_vpath_builddir}/scripts/mysql.service %{buildroot}%{_unitdir}/%{daemon_name}.service
install -D -p -m 644 %{_vpath_builddir}/scripts/mysql@.service %{buildroot}%{_unitdir}/%{daemon_name}@.service

# helper scripts for service starting
install -p -m 755 %{_vpath_builddir}/scripts/mariadb-prepare-db-dir %{buildroot}%{_libexecdir}/mariadb-prepare-db-dir
install -p -m 755 %{_vpath_builddir}/scripts/mariadb-check-socket %{buildroot}%{_libexecdir}/mariadb-check-socket
install -p -m 755 %{_vpath_builddir}/scripts/mariadb-check-upgrade %{buildroot}%{_libexecdir}/mariadb-check-upgrade
install -p -m 644 %{_vpath_builddir}/scripts/mariadb-scripts-common %{buildroot}%{_libexecdir}/mariadb-scripts-common

# Install downstream version of tmpfiles
install -D -p -m 0644 %{_vpath_builddir}/scripts/mariadb.tmpfiles.d %{buildroot}%{_tmpfilesdir}/%{majorname}.conf

# Install downstream version of sysusers.d config
install -m0644 -D support-files/%{majorname}.sysusers.conf %{buildroot}%{_sysusersdir}/%{majorname}.conf

# Install additional cracklib selinux policy
%if %{with cracklib}
mkdir -p %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/
mv %{buildroot}%{_datadir}/mariadb/policy/selinux/mariadb-plugin-cracklib-password-check.pp %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{majorname}-plugin-cracklib-password-check.pp
rm %{buildroot}%{_datadir}/mariadb/policy/selinux/mariadb-plugin-cracklib-password-check.te
%endif

%if %{with test}
# mariadb-test includes one executable that doesn't belong under /usr/share, so move it and provide a symlink
mv %{buildroot}%{_datadir}/mariadb-test/lib/My/SafeProcess/my_safe_process %{buildroot}%{_bindir}
ln -s ../../../../../bin/my_safe_process %{buildroot}%{_datadir}/mariadb-test/lib/My/SafeProcess/my_safe_process
# Provide symlink expected by RH QA tests
ln -s unstable-tests %{buildroot}%{_datadir}/mariadb-test/rh-skipped-tests.list
%endif

# Static libraries
rm %{buildroot}%{_libdir}/*.a
# This script creates the MySQL system tables and starts the server.
# Upstream says:
#   It looks like it's just "mysql_install_db && mysqld_safe"
#   I've never heard of anyone using it, I'd say, no need to pack it.
rm %{buildroot}%{_datadir}/%{majorname}/binary-configure
# FS files first-bytes recoginiton
# Not updated by upstream since nobody realy use that
rm %{buildroot}%{_datadir}/%{majorname}/magic

# Upstream ships them because of, https://jira.mariadb.org/browse/MDEV-10797
# In Fedora we use our own systemd unit files and scripts
rm %{buildroot}%{_datadir}/%{majorname}/mysql.server
rm %{buildroot}%{_datadir}/%{majorname}/mysqld_multi.server

# Binary for monitoring MySQL performance
# Shipped as a standalone package in Fedora
rm %{buildroot}%{_bindir}/mytop
rm %{buildroot}%{_mandir}/man1/mytop.1*

# Should be shipped with mariadb-connector-c
rm %{buildroot}%{_mandir}/man1/mariadb_config.1*

# for compatibility with upstream RPMs, create mysqld symlink in sbin
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_libexecdir}/mysqld %{buildroot}%{_sbindir}/mysqld
ln -s %{_libexecdir}/mariadbd %{buildroot}%{_sbindir}/mariadbd

# copy additional docs into build tree so %%doc will find them
install -p -m 0644 %{SOURCE6} %{basename:%{SOURCE6}}
install -p -m 0644 %{SOURCE16} %{basename:%{SOURCE16}}

%if %{with galera}
# Add wsrep_sst_rsync_tunnel script
install -p -m 0755 scripts/wsrep_sst_rsync_tunnel %{buildroot}%{_bindir}/wsrep_sst_rsync_tunnel
install -p -m 0644 %{SOURCE8} %{basename:%{SOURCE8}}

# install the clustercheck script
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
touch %{buildroot}%{_sysconfdir}/sysconfig/clustercheck
install -p -m 0755 %{_vpath_builddir}/scripts/clustercheck %{buildroot}%{_bindir}/clustercheck
# clustercheck license
install -p -m 0644 %{SOURCE71} %{basename:%{SOURCE71}}

# install galera config file
sed -i -r 's|^wsrep_provider=none|wsrep_provider=%{_libdir}/galera/libgalera_smm.so|' %{_vpath_builddir}/support-files/wsrep.cnf
install -p -m 0644 %{_vpath_builddir}/support-files/wsrep.cnf %{buildroot}%{_sysconfdir}/my.cnf.d/galera.cnf

# install additional galera selinux policy
install -p -m 644 -D %{majorname}-server-galera.cil %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{majorname}-server-galera.cil

# Fix Galera Replication config file
#   The replication requires cluster address upon startup (which is end-user specific).
#   Disable it entirely, rather than have it failing out-of-the-box.
sed -i 's/^wsrep_on=1/wsrep_on=0/' %{buildroot}%{_sysconfdir}/my.cnf.d/galera.cnf
%endif

# remove duplicate logrotate script
rm %{buildroot}%{_datadir}/mariadb/mariadb.logrotate
# Remove AppArmor files
rm -r %{buildroot}%{_datadir}/%{majorname}/policy/apparmor

# Buildroot does not have symlink /lib64 --> /usr/lib64
%if %{with pam}
mv %{buildroot}/%{_lib}/security %{buildroot}%{_libdir}
%endif

# Disable plugins
%if %{with gssapi}
sed -i 's/^plugin-load-add/#plugin-load-add/' %{buildroot}%{_sysconfdir}/my.cnf.d/auth_gssapi.cnf
%endif
%if %{with cracklib}
sed -i 's/^plugin-load-add/#plugin-load-add/' %{buildroot}%{_sysconfdir}/my.cnf.d/cracklib_password_check.cnf
%endif

%if %{without embedded}
rm %{buildroot}%{_mandir}/man1/{mysql_client_test_embedded,mysqltest_embedded}.1*
rm %{buildroot}%{_mandir}/man1/{mariadb-client-test-embedded,mariadb-test-embedded}.1*
rm %{buildroot}%{_mandir}/man1/{mariadb-,mysql_}embedded.1*
%endif


%if %{without clibrary}
# Client part should be included in package 'mariadb-connector-c'
rm %{buildroot}%{_libdir}/pkgconfig/libmariadb.pc

rm %{buildroot}%{_sysconfdir}/my.cnf.d/client.cnf
# Client library and links
rm %{buildroot}%{_libdir}/libmariadb.so.*
unlink %{buildroot}%{_libdir}/libmysqlclient.so
unlink %{buildroot}%{_libdir}/libmysqlclient_r.so
unlink %{buildroot}%{_libdir}/libmariadb.so
rm %{buildroot}%{_mandir}/man3/*
# Client plugins
rm %{buildroot}%{_libdir}/%{majorname}/plugin/{dialog.so,mysql_clear_password.so,sha256_password.so,parsec.so}
%if %{with gssapi} || %{with hashicorp}
rm %{buildroot}%{_libdir}/%{majorname}/plugin/auth_gssapi_client.so
%endif
%endif

%if %{without clibrary} || %{without devel}
rm %{buildroot}%{_bindir}/mysql_config*
rm %{buildroot}%{_bindir}/mariadb_config
rm %{buildroot}%{_bindir}/mariadb-config
rm %{buildroot}%{_mandir}/man1/mysql_config*.1*
%endif

%if %{without clibrary} && %{with devel}
# This files are already included in mariadb-connector-c
rm %{buildroot}%{_includedir}/mysql/mysql_version.h
rm %{buildroot}%{_includedir}/mysql/{errmsg.h,ma_list.h,ma_pvio.h,mariadb_com.h,\
mariadb_ctype.h,mariadb_dyncol.h,mariadb_stmt.h,mariadb_version.h,ma_tls.h,mysqld_error.h,mysql.h,mariadb_rpl.h}
rm -r %{buildroot}%{_includedir}/mysql/{mariadb,mysql}
%endif

%if %{without devel}
rm -r %{buildroot}%{_includedir}/mysql
rm %{buildroot}%{_datadir}/aclocal/mysql.m4
rm %{buildroot}%{_libdir}/pkgconfig/mariadb.pc
%if %{with clibrary}
rm %{buildroot}%{_libdir}/libmariadb*.so
unlink %{buildroot}%{_libdir}/libmysqlclient.so
unlink %{buildroot}%{_libdir}/libmysqlclient_r.so
%endif
%endif

%if %{without client}
rm %{buildroot}%{_bindir}/msql2mysql
rm %{buildroot}%{_bindir}/my_print_defaults
rm %{buildroot}%{_bindir}/replace
rm %{buildroot}%{_bindir}/{mysql,mariadb}
rm %{buildroot}%{_bindir}/mysql{access,admin,binlog,check,_convert_table_format,dump,dumpslow,_find_rows,hotcopy,import,_plugin,_setpermission,show,slap,_tzinfo_to_sql,_waitpid}
rm %{buildroot}%{_bindir}/mariadb-{access,admin,binlog,check,convert-table-format,dump,dumpslow,find-rows,hotcopy,import,plugin,setpermission,show,slap,tzinfo-to-sql,waitpid}

rm %{buildroot}%{_mandir}/man1/msql2mysql.1*
rm %{buildroot}%{_mandir}/man1/my_print_defaults.1*
rm %{buildroot}%{_mandir}/man1/replace.1*
rm %{buildroot}%{_mandir}/man1/{mysql,mariadb}.1*
rm %{buildroot}%{_mandir}/man1/mysql{access,admin,binlog,check,_convert_table_format,dump,dumpslow,_find_rows,hotcopy,import,_plugin,_setpermission,show,slap,_tzinfo_to_sql,_waitpid}.1*
rm %{buildroot}%{_mandir}/man1/mariadb-{access,admin,binlog,check,convert-table-format,dump,dumpslow,find-rows,hotcopy,import,plugin,setpermission,show,slap,tzinfo-to-sql,waitpid}.1*

rm %{buildroot}%{_sysconfdir}/my.cnf.d/mysql-clients.cnf
%endif

%if %{without common}
rm -r %{buildroot}%{_datadir}/%{majorname}/charsets
rm -r %{buildroot}%{_docdir}/%{majorname}
%endif

%if %{without errmsg}
rm -r %{buildroot}%{_datadir}/%{majorname}/{english,czech,danish,dutch,estonian,\
french,german,greek,hungarian,italian,japanese,korean,norwegian,norwegian-ny,\
polish,portuguese,romanian,russian,serbian,slovak,spanish,swedish,ukrainian,hindi,\
bulgarian,chinese,georgian}
%endif

%if %{without test}
%if %{with embedded}
rm %{buildroot}%{_bindir}/test-connect-t
rm %{buildroot}%{_bindir}/{mysql_client_test_embedded,mysqltest_embedded}
rm %{buildroot}%{_bindir}/{mariadb-client-test-embedded,mariadb-test-embedded}
rm %{buildroot}%{_mandir}/man1/{mysql_client_test_embedded,mysqltest_embedded}.1*
rm %{buildroot}%{_mandir}/man1/{mariadb-client-test-embedded,mariadb-test-embedded}.1*
# endif embedded
%endif
%if %{with pam}
rm %{buildroot}/suite/plugins/pam/mariadb_mtr
rm %{buildroot}/suite/plugins/pam/pam_mariadb_mtr.so
# endif pam
%endif
rm %{buildroot}%{_bindir}/{mysql_client_test,mysqltest}
rm %{buildroot}%{_bindir}/{mariadb-client-test,mariadb-test}
rm %{buildroot}%{_mandir}/man1/{mysql_client_test,mysqltest,my_safe_process}.1*
rm %{buildroot}%{_mandir}/man1/{mariadb-client-test,mariadb-test}.1*
rm %{buildroot}%{_mandir}/man1/{mysql-test-run,mysql-stress-test}.pl.1*
rm %{buildroot}%{_libdir}/%{majorname}/plugin/adt_null.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/auth_0x0100.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/auth_test_plugin.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/debug_key_management.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/dialog_examples.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/example_key_management.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/func_test.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/ha_example.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/ha_test_sql_discovery.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/libdaemon_example.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/mypluglib.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/qa_auth_client.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/qa_auth_interface.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/qa_auth_server.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/test_sql_service.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/test_versioning.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/type_mysql_timestamp.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/type_test.so
rm %{buildroot}%{_libdir}/%{majorname}/plugin/daemon_example.ini
%endif

%if %{without backup}
rm %{buildroot}%{_mandir}/man1/maria{,db-}backup.1*
rm %{buildroot}%{_mandir}/man1/mbstream.1*
%endif

%check
%if %{with test}
%if %runselftest
# The cmake build scripts don't provide any simple way to control the
# options for mysql-test-run, so ignore the make target and just call it
# manually.  Nonstandard options chosen are:
# --force to continue tests after a failure
# no retries please
# test SSL with --ssl
# skip tests that are listed in rh-skipped-tests.list
# avoid redundant test runs with --binlog-format=mixed
# increase timeouts to prevent unwanted failures during mass rebuilds

# Usefull arguments:
#    --do-test=mysql_client_test_nonblock \
#    --skip-rpl
#    --suite=roles
#    --mem for running in the RAM; Not enough space in KOJI for this

(
  set -ex
  cd %{buildroot}%{_datadir}/mariadb-test

  export common_testsuite_arguments=" --port-base=$(( $(date +%s) % 20000 + 10000 )) --parallel=auto --force --retry=2 --suite-timeout=900 --testcase-timeout=30 --mysqld=--binlog-format=mixed --force-restart --shutdown-timeout=60 --max-test-fail=5 "

  # If full testsuite has already been run on this version and we don't explicitly want the full testsuite to be run
  if [[ "%{last_tested_version}" == "%{version}" ]] && [[ %{force_run_testsuite} -eq 0 ]]
  then
    # in further rebuilds only run the basic "main" suite (~800 tests)
    echo -e "\n\nRunning just the base testsuite\n\n"
    perl ./mysql-test-run.pl $common_testsuite_arguments --ssl --suite=main --mem --skip-test-list=unstable-tests
  fi

  # If either this version wasn't marked as tested yet or I explicitly want to run the testsuite, run everything we have (~4000 test)
  if [[ "%{last_tested_version}" != "%{version}" ]] || [[ %{force_run_testsuite} -ne 0 ]]
  then
    echo -e "\n\nRunning the advanced testsuite\n\n"
    perl ./mysql-test-run.pl $common_testsuite_arguments --ssl --big-test --skip-test=spider \
    %if %{ignore_testsuite_result}
      --max-test-fail=9999 || :
    %else
      --skip-test-list=unstable-tests
    %endif

    # Spider tests can't be run in the Fedora KOJI at this moment, see #2291227
    %if 0
    # Second run for the SPIDER suites that fail with SCA (ssl self signed certificate)
    perl ./mysql-test-run.pl $common_testsuite_arguments --skip-ssl --big-test --suite=spider,spider/bg,spider/bugfix \
    %if %{ignore_testsuite_result}
      --max-test-fail=999 || :
    %else
      --skip-test-list=unstable-tests
    %endif
    %endif
  # blank line
  fi

  # There might be a dangling symlink left from the testing, remove it to not be installed
  rm -rf ./var
  # Remove temporary files created by the testsuite execution
  find ./ -type f -name '*~' -exec rm {} +
)

# NOTE: the Spider SE has 2 more hidden testsuites "oracle" and "oracle2".
#       however, all of the tests fail with: "failed: 12521: Can't use wrapper 'oracle' for SQL connection"

%endif
%endif



%post -n %{pkgname}-server
%systemd_post %{daemon_name}.service

%preun -n %{pkgname}-server
%systemd_preun %{daemon_name}.service

%postun -n %{pkgname}-server
%systemd_postun_with_restart %{daemon_name}.service

%if %{with galera}
%post -n %{pkgname}-server-galera
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{majorname}-server-galera.cil

# Allow ports needed for the replication:
# 
if [ $1 -eq 1 ]; then
  # https://mariadb.com/kb/en/library/configuring-mariadb-galera-cluster/#network-ports
  #   Galera Replication Port
  semanage port -a -t mysqld_port_t -p tcp 4567 >/dev/null 2>&1 || :
  semanage port -a -t mysqld_port_t -p udp 4567 >/dev/null 2>&1 || :
  #   IST Port
  semanage port -a -t mysqld_port_t -p tcp 4568 >/dev/null 2>&1 || :
  #   SST Port
  semanage port -a -t mysqld_port_t -p tcp 4444 >/dev/null 2>&1 || :
fi

%postun -n %{pkgname}-server-galera
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{majorname}-server-galera

    # Delete port labeling when the package is removed
    # 
    semanage port -d -t mysqld_port_t -p tcp 4567 >/dev/null 2>&1 || :
    semanage port -d -t mysqld_port_t -p udp 4567 >/dev/null 2>&1 || :
    semanage port -d -t mysqld_port_t -p tcp 4568 >/dev/null 2>&1 || :
    semanage port -d -t mysqld_port_t -p tcp 4444 >/dev/null 2>&1 || :
fi
%endif

%if %{with cracklib}
%post -n %{pkgname}-cracklib-password-check
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{majorname}-plugin-cracklib-password-check.pp

%postun -n %{pkgname}-cracklib-password-check
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{majorname}-plugin-cracklib-password-check
fi
%endif



%if %{with client}
%files -n %{pkgname}
%{_bindir}/{msql2mysql,replace}
%{_bindir}/{mysql,mariadb}
%{_bindir}/mysql{admin,binlog,check,dump,import,_plugin,show,slap,_tzinfo_to_sql,_waitpid}
%{_bindir}/mariadb-{admin,binlog,check,dump,import,plugin,show,slap,tzinfo-to-sql,waitpid}
%{_bindir}/my_print_defaults

%{_mandir}/man1/{msql2mysql,replace}.1*
%{_mandir}/man1/{mysql,mariadb}.1*
%{_mandir}/man1/mysql{access,admin,binlog,check,dump,_find_rows,import,_plugin,show,slap,_tzinfo_to_sql,_waitpid}.1*
%{_mandir}/man1/mariadb-{access,admin,binlog,check,dump,find-rows,import,plugin,show,slap,tzinfo-to-sql,waitpid}.1*
%{_mandir}/man1/my_print_defaults.1*

%config(noreplace) %{_sysconfdir}/my.cnf.d/mysql-clients.cnf

%files -n %{pkgname}-client-utils
%{_bindir}/mysql{access,_convert_table_format,dumpslow,_find_rows,hotcopy,_setpermission}
%{_bindir}/mariadb-{access,convert-table-format,dumpslow,find-rows,hotcopy,setpermission}
%{_mandir}/man1/mysql{access,_convert_table_format,dumpslow,_find_rows,hotcopy,_setpermission}.1*
%{_mandir}/man1/mariadb-{access,convert-table-format,dumpslow,find-rows,hotcopy,setpermission}.1*
%endif

%if %{with clibrary}
%files -n %{pkgname}-libs
%exclude %{_libdir}/{libmysqlclient.so.18,libmariadb.so,libmysqlclient.so,libmysqlclient_r.so}
%{_libdir}/libmariadb.so*
%config(noreplace) %{_sysconfdir}/my.cnf.d/client.cnf
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
%doc %{_docdir}/%{majorname}
%{?with_galera:%exclude %{_docdir}/%{majorname}/MariaDB-server-%{version}/README-wsrep}
%dir %{_datadir}/%{majorname}
%{_datadir}/%{majorname}/charsets
%if %{with clibrary}
%{_libdir}/%{majorname}/plugin/dialog.so
%{_libdir}/%{majorname}/plugin/mysql_clear_password.so
%endif
%endif

%if %{with errmsg}
%files -n %{pkgname}-errmsg
%{_datadir}/%{majorname}/english
%lang(cs) %{_datadir}/%{majorname}/czech
%lang(da) %{_datadir}/%{majorname}/danish
%lang(nl) %{_datadir}/%{majorname}/dutch
%lang(et) %{_datadir}/%{majorname}/estonian
%lang(fr) %{_datadir}/%{majorname}/french
%lang(de) %{_datadir}/%{majorname}/german
%lang(el) %{_datadir}/%{majorname}/greek
%lang(hi) %{_datadir}/%{majorname}/hindi
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
%lang(bg) %{_datadir}/%{majorname}/bulgarian
%lang(zh) %{_datadir}/%{majorname}/chinese
%lang(ka) %{_datadir}/%{majorname}/georgian
%lang(sw) %{_datadir}/%{majorname}/swahili
%endif

%if %{with galera}
%files -n %{pkgname}-server-galera
%doc Docs/README-wsrep
%license LICENSE.clustercheck
%{_bindir}/clustercheck
%{_bindir}/galera_new_cluster
%{_bindir}/galera_recovery
%{_libdir}/%{majorname}/plugin/wsrep_info.so
%{_mandir}/man1/galera_new_cluster.1*
%{_mandir}/man1/galera_recovery.1*
%config(noreplace) %{_sysconfdir}/my.cnf.d/galera.cnf
%attr(0640,root,root) %ghost %config(noreplace) %{_sysconfdir}/sysconfig/clustercheck
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{majorname}-server-galera
%{_datadir}/selinux/packages/%{selinuxtype}/%{majorname}-server-galera.cil
%endif

%files -n %{pkgname}-server

%{_bindir}/aria_{chk,dump_log,ftdump,pack,read_log}
%{_mandir}/man1/aria_{chk,dump_log,ftdump,pack,read_log}.1*

%{_bindir}/myisam{chk,_ftdump,log,pack}
%{_mandir}/man1/myisam{chk,_ftdump,log,pack}.1*

%{_bindir}/mariadb-service-convert
%{_mandir}/man1/mariadb-service-convert.1*
%{_bindir}/mariadb-conv
%{_mandir}/man1/mariadb-conv.1*

%{_bindir}/mysql_{install_db,secure_installation,upgrade}
%{_mandir}/man1/mysql_{install_db,secure_installation,upgrade}.1*
%{_bindir}/mariadb-{install-db,secure-installation,upgrade}
%{_mandir}/man1/mariadb-{install-db,secure-installation,upgrade}.1*
%{_bindir}/{mysqld_,mariadbd-}safe
%{_mandir}/man1/{mysqld_,mariadbd-}safe.1*
%{_bindir}/{mysqld_safe_helper,mariadbd-safe-helper}
%{_mandir}/man1/{mysqld_safe_helper,mariadbd-safe-helper}.1*

%{_bindir}/{innochecksum,perror,resolve_stack_dump,resolveip}
%{_mandir}/man1/{innochecksum,perror,resolve_stack_dump,resolveip}.1*

%if %{with galera}
# wsrep_sst_common should be moved to /usr/share/mariadb: https://jira.mariadb.org/browse/MDEV-14296
%{_bindir}/wsrep_*
%{_mandir}/man1/wsrep_*.1*
%doc README.wsrep_sst_rsync_tunnel
%endif

%config(noreplace) %{_sysconfdir}/my.cnf.d/%{majorname}-server.cnf
%config(noreplace) %{_sysconfdir}/my.cnf.d/enable_encryption.preset
%config(noreplace) %{_sysconfdir}/my.cnf.d/spider.cnf

%{?with_lz4:%config(noreplace) %{_sysconfdir}/my.cnf.d/provider_lz4.cnf}
%{?with_bzip2:%config(noreplace) %{_sysconfdir}/my.cnf.d/provider_bzip2.cnf}
%{?with_lzma:%config(noreplace) %{_sysconfdir}/my.cnf.d/provider_lzma.cnf}
%{?with_lzo:%config(noreplace) %{_sysconfdir}/my.cnf.d/provider_lzo.cnf}
%{?with_snappy:%config(noreplace) %{_sysconfdir}/my.cnf.d/provider_snappy.cnf}

%{?with_hashicorp:%config(noreplace) %{_sysconfdir}/my.cnf.d/hashicorp_key_management.cnf}

%{_sbindir}/mysqld
%{_sbindir}/mariadbd
%{_libexecdir}/{mysqld,mariadbd}

%{_mandir}/man1/mysql.server.1*
%{_mandir}/man8/{mysqld,mariadbd}.8*

%if %{without common}
%dir %{_datadir}/%{majorname}
%endif

%dir %{_libdir}/%{majorname}
%dir %{_libdir}/%{majorname}/plugin

%{_libdir}/%{majorname}/plugin/auth_ed25519.so
%{_libdir}/%{majorname}/plugin/auth_parsec.so
%{_libdir}/%{majorname}/plugin/auth_mysql_sha2.so
%{_libdir}/%{majorname}/plugin/disks.so
%{_libdir}/%{majorname}/plugin/file_key_management.so
%{_libdir}/%{majorname}/plugin/ha_archive.so
%{_libdir}/%{majorname}/plugin/ha_blackhole.so
%{_libdir}/%{majorname}/plugin/ha_federatedx.so
%{_libdir}/%{majorname}/plugin/ha_spider.so
%{_libdir}/%{majorname}/plugin/handlersocket.so
%{?with_hashicorp:%{_libdir}/%{majorname}/plugin/hashicorp_key_management.so}
%{_libdir}/%{majorname}/plugin/locales.so
%{_libdir}/%{majorname}/plugin/metadata_lock_info.so
%{_libdir}/%{majorname}/plugin/password_reuse_check.so
%{?with_bzip2:%{_libdir}/%{majorname}/plugin/provider_bzip2.so}
%{?with_lz4:%{_libdir}/%{majorname}/plugin/provider_lz4.so}
%{?with_lzma:%{_libdir}/%{majorname}/plugin/provider_lzma.so}
%{?with_lzo:%{_libdir}/%{majorname}/plugin/provider_lzo.so}
%{?with_snappy:%{_libdir}/%{majorname}/plugin/provider_snappy.so}
%{_libdir}/%{majorname}/plugin/query_cache_info.so
%{_libdir}/%{majorname}/plugin/query_response_time.so
%{_libdir}/%{majorname}/plugin/server_audit.so
%{_libdir}/%{majorname}/plugin/simple_password_check.so
%{_libdir}/%{majorname}/plugin/sql_errlog.so
%{_libdir}/%{majorname}/plugin/type_mysql_json.so

%{_datadir}/%{majorname}/mini-benchmark
%{_datadir}/%{majorname}/fill_help_tables.sql
%{_datadir}/%{majorname}/maria_add_gis_{sp,sp_bootstrap}.sql
%{_datadir}/%{majorname}/mariadb_{system_tables,system_tables_data,sys_schema,test_data_timezone,performance_tables,test_db}.sql
%if %{with mroonga}
%dir %{_datadir}/%{majorname}/mroonga
%dir %{_datadir}/%{majorname}-server
%dir %{_datadir}/%{majorname}-server/groonga
%dir %{_datadir}/%{majorname}-server/groonga-normalizer-mysql
%{_datadir}/%{majorname}/mroonga/install.sql
%{_datadir}/%{majorname}/mroonga/uninstall.sql
%{_libdir}/%{majorname}/plugin/ha_mroonga.so
%license %{_datadir}/%{majorname}/mroonga/COPYING
%license %{_datadir}/%{majorname}/mroonga/AUTHORS
%license %{_datadir}/%{majorname}-server/groonga-normalizer-mysql/lgpl-2.0.txt
%license %{_datadir}/%{majorname}-server/groonga/COPYING
%doc %{_datadir}/%{majorname}-server/groonga-normalizer-mysql/README.md
%doc %{_datadir}/%{majorname}-server/groonga/README.md
%endif
%if %{with galera}
%{_datadir}/%{majorname}/wsrep.cnf
%{_datadir}/%{majorname}/wsrep_notify
%endif
%dir %{_datadir}/%{majorname}/policy
%dir %{_datadir}/%{majorname}/policy/selinux
%{_datadir}/%{majorname}/policy/selinux/README
%{_datadir}/%{majorname}/policy/selinux/mariadb-server.*
%{_datadir}/%{majorname}/policy/selinux/mariadb.*

# More on socket activation or extra port service at
# https://mariadb.com/kb/en/systemd/
%{_unitdir}/%{daemon_name}.service
%{_unitdir}/mysql{,d}.service
%{_unitdir}/%{daemon_name}@.service
%{_unitdir}/%{daemon_name}.socket
%{_unitdir}/%{daemon_name}@.socket
%{_unitdir}/%{daemon_name}-extra.socket
%{_unitdir}/%{daemon_name}-extra@.socket
%{_unitdir}/%{daemon_name}@bootstrap.service.d

%{_libexecdir}/mariadb-prepare-db-dir
%{_libexecdir}/mariadb-check-socket
%{_libexecdir}/mariadb-check-upgrade
%{_libexecdir}/mariadb-scripts-common

# Remember to also update the mariadb.tmpfiles.d.in file when updating these permissions
%attr(0755,mysql,mysql) %dir %{pidfiledir}
%attr(0755,mysql,mysql) %dir %{dbdatadir}
%attr(0750,mysql,mysql) %dir %{logfiledir}
# This does what it should.
# RPMLint error "conffile-without-noreplace-flag /var/log/mariadb/mariadb.log" is false positive.
%attr(0660,mysql,mysql) %config %ghost %verify(not md5 size mtime) %{logfile}
%config(noreplace) %{logrotateddir}/%{daemon_name}

%{_tmpfilesdir}/%{majorname}.conf
%{_sysusersdir}/%{majorname}.conf

%if %{with cracklib}
%files -n %{pkgname}-cracklib-password-check
%config(noreplace) %{_sysconfdir}/my.cnf.d/cracklib_password_check.cnf
%{_libdir}/%{majorname}/plugin/cracklib_password_check.so
%{_datadir}/selinux/packages/%{selinuxtype}/%{majorname}-plugin-cracklib-password-check.pp
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{majorname}-plugin-cracklib-password-check
%endif

%if %{with backup}
%files -n %{pkgname}-backup
%{_bindir}/maria{,db-}backup
%{_bindir}/mbstream
%{_mandir}/man1/maria{,db-}backup.1*
%{_mandir}/man1/mbstream.1*
%endif

%if %{with rocksdb}
%files -n %{pkgname}-rocksdb-engine
%config(noreplace) %{_sysconfdir}/my.cnf.d/rocksdb.cnf
%{_bindir}/myrocks_hotbackup
%{_bindir}/{mysql_,mariadb-}ldb
%{_bindir}/sst_dump
%{_libdir}/%{majorname}/plugin/ha_rocksdb.so
%{_mandir}/man1/{mysql_,mariadb-}ldb.1*
%{_mandir}/man1/myrocks_hotbackup.1*
%endif

%if %{with gssapi}
%files -n %{pkgname}-gssapi-server
%{_libdir}/%{majorname}/plugin/auth_gssapi.so
%config(noreplace) %{_sysconfdir}/my.cnf.d/auth_gssapi.cnf
%endif

%if %{with pam}
%files -n %{pkgname}-pam
%{_libdir}/%{majorname}/plugin/{auth_pam_v1.so,auth_pam.so}
%attr(0755,root,root) %dir %{_libdir}/%{majorname}/plugin/auth_pam_tool_dir
# SUID-to-root binary. Access MUST be restricted (https://jira.mariadb.org/browse/MDEV-25126)
%attr(4750,root,mysql) %{_libdir}/%{majorname}/plugin/auth_pam_tool_dir/auth_pam_tool
%{_libdir}/security/pam_user_map.so
%config(noreplace) %{_sysconfdir}/security/user_map.conf
%endif

%if %{with sphinx}
%files -n %{pkgname}-sphinx-engine
%{_libdir}/%{majorname}/plugin/ha_sphinx.so
%endif

%if %{with oqgraph}
%files -n %{pkgname}-oqgraph-engine
%config(noreplace) %{_sysconfdir}/my.cnf.d/oqgraph.cnf
%{_libdir}/%{majorname}/plugin/ha_oqgraph.so
%endif

%if %{with connect}
%files -n %{pkgname}-connect-engine
%config(noreplace) %{_sysconfdir}/my.cnf.d/connect.cnf
%{_libdir}/%{majorname}/plugin/ha_connect.so
%endif

%if %{with s3}
%files -n %{pkgname}-s3-engine
%{_bindir}/aria_s3_copy
%{_mandir}/man1/aria_s3_copy.1*
%config(noreplace) %{_sysconfdir}/my.cnf.d/s3.cnf
%{_libdir}/%{majorname}/plugin/ha_s3.so
%endif

%files -n %{pkgname}-server-utils
# Perl utilities
%{_bindir}/mysql{_fix_extensions}
%{_bindir}/mariadb-{fix-extensions}
%{_bindir}/{mysqld_,mariadbd-}multi

%{_mandir}/man1/mysql{_fix_extensions}.1*
%{_mandir}/man1/mariadb-{fix-extensions}.1*
%{_mandir}/man1/{mysqld_,mariadbd-}multi.1*

%if %{with devel}
%files -n %{pkgname}-devel
%{_includedir}/*
%{_datadir}/aclocal/mysql.m4
%{_libdir}/pkgconfig/*mariadb.pc
%if %{with clibrary}
%{_mandir}/man3/*
%{_libdir}/{libmysqlclient.so.18,libmariadb.so,libmysqlclient.so,libmysqlclient_r.so}
%{_bindir}/mysql_config*
%{_bindir}/mariadb_config*
%{_bindir}/mariadb-config
%{_libdir}/libmariadb.so
%{_libdir}/libmysqlclient.so
%{_libdir}/libmysqlclient_r.so
%{_mandir}/man1/mysql_config*
%endif
%endif

%if %{with embedded}
%files -n %{pkgname}-embedded
%{_libdir}/libmariadbd.so.*
%{_bindir}/{mariadb-,mysql_}embedded
%{_mandir}/man1/{mysql_,mariadb-}embedded.1*

%files -n %{pkgname}-embedded-devel
%{_libdir}/libmysqld.so
%{_libdir}/libmariadbd.so
%endif

%if %{with test}
%files -n %{pkgname}-test
%if %{with embedded}
%{_bindir}/test-connect-t
%{_bindir}/{mysql_client_test_embedded,mysqltest_embedded}
%{_bindir}/{mariadb-client-test-embedded,mariadb-test-embedded}
%{_mandir}/man1/{mysql_client_test_embedded,mysqltest_embedded}.1*
%{_mandir}/man1/{mariadb-client-test-embedded,mariadb-test-embedded}.1*
%endif
%{_bindir}/{mysql_client_test,mysqltest,mariadb-client-test,mariadb-test}
%{_bindir}/my_safe_process
%dir %{_libdir}/%{majorname}/plugin
# shared objects required for testing
%{_libdir}/%{majorname}/plugin/adt_null.so
%{_libdir}/%{majorname}/plugin/auth_0x0100.so
%{_libdir}/%{majorname}/plugin/auth_test_plugin.so
%{_libdir}/%{majorname}/plugin/debug_key_management.so
%{_libdir}/%{majorname}/plugin/dialog_examples.so
%{_libdir}/%{majorname}/plugin/example_key_management.so
%{_libdir}/%{majorname}/plugin/func_test.so
%{_libdir}/%{majorname}/plugin/ha_example.so
%{_libdir}/%{majorname}/plugin/ha_test_sql_discovery.so
%{_libdir}/%{majorname}/plugin/libdaemon_example.so
%{_libdir}/%{majorname}/plugin/mypluglib.so
%{_libdir}/%{majorname}/plugin/qa_auth_client.so
%{_libdir}/%{majorname}/plugin/qa_auth_interface.so
%{_libdir}/%{majorname}/plugin/qa_auth_server.so
%{_libdir}/%{majorname}/plugin/test_sql_service.so
%{_libdir}/%{majorname}/plugin/test_versioning.so
%{_libdir}/%{majorname}/plugin/type_mysql_timestamp.so
%{_libdir}/%{majorname}/plugin/type_test.so
%{_libdir}/%{majorname}/plugin/daemon_example.ini
%attr(-,mysql,mysql) %{_datadir}/mariadb-test
%{_mandir}/man1/{mysql_client_test,mysqltest,mariadb-client-test,mariadb-test}.1*
%{_mandir}/man1/my_safe_process.1*
%{_mandir}/man1/mysql-stress-test.pl.1*
%{_mandir}/man1/mysql-test-run.pl.1*
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3:11.8.6-2
- Import
