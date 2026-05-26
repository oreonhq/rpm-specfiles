# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 e0a992d740709892e81f9d93f06daf305cf73fb81b545afe72478043172c3628
%global source1_sha256 4220d4ddeb77fb57ba2f37c1aa105d561d3ef85a6fb89c79c3edd735d0e193c6
%global source4_sha256 792e854b402e9e18ccfe6edef97fe86d2d95d24d75c405875d419526a6c114d4
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })} \
%{?source1_sha256:%(test -z "%{source1_sha256}" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_sha256}" || { echo "oreon: Source1 sha256 mismatch" >&2; exit 1; }; })} \
%{?source4_sha256:%(test -z "%{source4_sha256}" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source4_sha256}" || { echo "oreon: Source4 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# This must remain enabled even for RHEL/ELN until all libdb dependencies
# are dropped, then this should be Fedora-only
%bcond_without subpackages

%define __soversion_major 5
%define __soversion %{__soversion_major}.3
%define __tclversion 8.6
%define _converter_version 1.0.3

# The SQLite configure script does not support --runstatedir and is not
# regenerated.
%undefine _configure_use_runstatedir

Summary: The Berkeley DB database library for C
Name: libdb
Version: 5.3.28
Release: 67%{?dist}
Source0: http://download.oracle.com/berkeley-db/db-%{version}.tar.gz
Source1: http://download.oracle.com/berkeley-db/db.1.85.tar.gz
# For mt19937db.c
Source2: http://www.gnu.org/licenses/lgpl-2.1.txt
# Man pages from Fedora libdb SRPM (not in Oracle db tarball); kept next to spec for CI
# e.g. libdb-5.3.28-67.fc44.src.rpm on dl.fedoraproject.org
Source3: libdb-5.3.28-manpages.tar.gz
Source4: https://github.com/fila43/db_converter/archive/refs/tags/v%{_converter_version}.tar.gz
Patch0: libdb-multiarch.patch
# db-1.85 upstream patches
# Former Oracle URLs are dead; files vendored next to spec (same as Fedora libdb lookaside)
Patch10:        http://www.oracle.com/technology/products/berkeley-db/db/update/1.85/patch.1.1
Patch11:        http://www.oracle.com/technology/products/berkeley-db/db/update/1.85/patch.1.2
Patch12:        http://www.oracle.com/technology/products/berkeley-db/db/update/1.85/patch.1.3
Patch13:        http://www.oracle.com/technology/products/berkeley-db/db/update/1.85/patch.1.4
# other patches
Patch20: db-1.85-errno.patch
Patch22: db-4.6.21-1.85-compat.patch
Patch24: db-4.5.20-jni-include-dir.patch
# License clarification patch
# http://devel.trisquel.info/gitweb/?p=package-helpers.git;a=blob;f=helpers/DATA/db4.8/007-mt19937db.c_license.patch;h=1036db4d337ce4c60984380b89afcaa63b2ef88f;hb=df48d40d3544088338759e8bea2e7f832a564d48
Patch25: 007-mt19937db.c_license.patch
# memp_stat fix provided by upstream (rhbz#1211871)
Patch27: db-5.3.21-memp_stat-upstream-fix.patch
# fix for mutexes not being released provided by upstream (rhbz#1277887)
Patch28: db-5.3.21-mutex_leak.patch
# fix for overflowing hash variable inside bundled lemon
Patch29: db-5.3.28-lemon_hash.patch
# upstream patch adding the ability to recreate libdb's environment on version mismatch
# or when libpthread.so is modified (rhbz#1394862)
Patch30: db-5.3.28-condition_variable.patch
# additional changes to the upstream patch to address rhbz#1460003
Patch31: db-5.3.28-condition-variable-ppc.patch
# downstream patch that adds a check for rpm transaction lock in order to be able to update libdb
# FIXME: remove when able
Patch32: db-5.3.28-rpm-lock-check.patch
# downstream patch to hotfix rhbz#1464033, sent upstream
Patch33: db-5.3.28-cwd-db_config.patch
Patch34: libdb-5.3.21-region-size-check.patch
# Patch sent upstream
Patch35: checkpoint-opd-deadlock.patch
Patch36: db-5.3.28-atomic_compare_exchange.patch
# CDB race (rhbz #1099509)
Patch37: libdb-cbd-race.patch
# Limit concurrency to max 1024 CPUs (rhbz#1245410)
# A fix for the issue should be in an upstream release already
# https://community.oracle.com/message/13274780#13274780
Patch38: libdb-limit-cpu.patch
# rhbz#1608749 Patch sent upstream
# Expects libdb-5.3.21-mutex_leak.patch applied
Patch39: libdb-5.3.21-trickle_cpu.patch
# cve-2019-2708 fixed by mmuzila
Patch40: db-5.3.28_cve-2019-2708.patch
# Prevents high CPU usage
Patch41: db-5.3.28-mmap-high-cpu-usage.patch

Patch42: libdb-1.85-c99.patch
Patch43: libdb-c99.patch
Patch44: libdb-configure-c99.patch
Patch45: libdb-sqlite-c99.patch
# Fix build with tcl8
Patch46: libdb-sqlite-tcl8.patch

URL: http://www.oracle.com/database/berkeley-db/
License: BSD-3-Clause AND LGPL-2.1-only AND Sleepycat
BuildRequires: gcc gcc-c++
BuildRequires: perl-interpreter libtool
BuildRequires: tcl-devel < 1:9.0
BuildRequires: chrpath
BuildRequires: zlib-devel
BuildRequires: make gdbm-devel lmdb-devel
Conflicts: filesystem < 3

# libdb was marked as deprecated in F33:
# https://fedoraproject.org/wiki/Changes/Libdb_deprecated
Provides:  deprecated()

%description
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. The Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching, and database
recovery. The Berkeley DB supports C, C++, and Perl APIs. It is
used by many applications, including Python and Perl, so this should
be installed on all systems.

%package utils
Summary: Command line tools for managing Berkeley DB databases
Requires: %{name}%{?_isa} = %{version}-%{release}

Provides:  deprecated()

%description utils
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching, and database
recovery. DB supports C, C++ and Perl APIs.

%package devel
Summary: C development files for the Berkeley DB library
Requires: %{name}%{?_isa} = %{version}-%{release}

Provides:  deprecated()

%description devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. This package contains the header files,
libraries, and documentation for building programs which use the
Berkeley DB.

%package devel-doc
Summary: C development documentation files for the Berkeley DB library
Requires: %{name} = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
BuildArch: noarch

Provides:  deprecated()

%description devel-doc
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. This package contains the header files,
libraries, and documentation for building programs which use the
Berkeley DB.

%package devel-static
Summary: Berkeley DB static libraries
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

Provides:  deprecated()

%description devel-static
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. This package contains static libraries
needed for applications that require static linking of
Berkeley DB.

%package cxx
Summary: The Berkeley DB database library for C++
Requires: %{name}%{?_isa} = %{version}-%{release}

Provides:  deprecated()

%description cxx
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. The Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching, and database
recovery. The Berkeley DB supports C, C++, and Perl APIs. It is
used by many applications, including Python and Perl, so this should
be installed on all systems.

%package cxx-devel
Summary: The Berkeley DB database library for C++
Requires: %{name}-cxx%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

Provides:  deprecated()

%description cxx-devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. The Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching, and database
recovery. The Berkeley DB supports C, C++, and Perl APIs. It is
used by many applications, including Python and Perl, so this should
be installed on all systems.

%package tcl
Summary: Development files for using the Berkeley DB with tcl
Requires: %{name}%{?_isa} = %{version}-%{release}

Provides:  deprecated()

%description tcl
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. This package contains the libraries
for building programs which use the Berkeley DB in Tcl.

%package tcl-devel
Summary: Development files for using the Berkeley DB with tcl
Requires: %{name}-tcl%{?_isa} = %{version}-%{release}

Provides:  deprecated()

%description tcl-devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. This package contains the libraries
for building programs which use the Berkeley DB in Tcl.

%package sql
Summary: Development files for using the Berkeley DB with sql
Requires: %{name}%{?_isa} = %{version}-%{release}

Provides:  deprecated()

%description sql
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. This package contains the libraries
for building programs which use the Berkeley DB in SQL.

%package sql-devel
Summary: Development files for using the Berkeley DB with sql
Requires: %{name}-sql%{?_isa} = %{version}-%{release}

Provides:  deprecated()

%description sql-devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. This package contains the libraries
for building programs which use the Berkeley DB in SQL.

%package convert-util
Summary: Development files for using the Berkeley DB with sql

%description convert-util
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. This package contains the libraries
for building programs which use the Berkeley DB in SQL.


%prep
%oreon_verify_sources
%setup -q -n db-%{version} -a 1
cp %{SOURCE2} .
tar -xf %{SOURCE3}
# db_converter
tar -xf %{SOURCE4}


%patch -P0 -p1
pushd db.1.85/PORT/linux
%patch -P10 -p0
popd
pushd db.1.85
%patch -P11 -p0
%patch -P12 -p0
%patch -P13 -p0
%patch -P20 -p1
popd

%patch -P22 -p1
%patch -P24 -p1
%patch -P25 -p1
%patch -P27 -p1
%patch -P28 -p1
%patch -P29 -p1
%patch -P30 -p1
%patch -P31 -p1
%patch -P32 -p1
%patch -P33 -p1
%patch -P34 -p1
%patch -P35 -p1
%patch -P36 -p1
%patch -P37 -p1
%patch -P38 -p1
%patch -P39 -p1
%patch -P40 -p1 -b .cve-2019-2708
%patch -P41 -p1
%patch -P42 -p1
%patch -P43 -p1
%patch -P44 -p1
%patch -P45 -p1
%patch -P46 -p1

cd dist
./s_config
cd ..

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -std=gnu99"
CFLAGS="$CFLAGS -DSHAREDSTATEDIR='\"%{_sharedstatedir}\"' -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_DISABLE_DIRSYNC=1 -DSQLITE_ENABLE_FTS3=3 -DSQLITE_ENABLE_RTREE=1 -DSQLITE_SECURE_DELETE=1 -DSQLITE_ENABLE_UNLOCK_NOTIFY=1 -I../../../lang/sql/sqlite/ext/fts3/"
export CFLAGS

# Build the old db-185 libraries.
make -C db.1.85/PORT/%{_os} OORG="$CFLAGS"

test -d dist/dist-tls || mkdir dist/dist-tls
# Static link db_dump185 with old db-185 libraries.
/bin/sh libtool --tag=CC --mode=compile	%{__cc} $RPM_OPT_FLAGS -Idb.1.85/PORT/%{_os}/include -D_REENTRANT -c util/db_dump185.c -o dist/dist-tls/db_dump185.lo
/bin/sh libtool --tag=CC --mode=link %{__cc} $RPM_LD_FLAGS -o dist/dist-tls/db_dump185 dist/dist-tls/db_dump185.lo db.1.85/PORT/%{_os}/libdb.a

# Update config files to understand aarch64
for dir in dist lang/sql/sqlite lang/sql/jdbc lang/sql/odbc; do
  cp /usr/lib/rpm/redhat/config.{guess,sub} "$dir"
done

pushd dist/dist-tls
%define _configure ../configure
%configure -C \
	--enable-compat185 --enable-dump185 \
	--enable-shared --enable-static \
	--enable-tcl --with-tcl=/usr/%{_lib} TCLSH_CMD=$(which tclsh%{__tclversion}) \
	--enable-cxx --enable-sql \
	--enable-test \
	--disable-rpath

# Remove libtool predep_objects and postdep_objects wonkiness so that
# building without -nostdlib doesn't include them twice.  Because we
# already link with g++, weird stuff happens if you don't let the
# compiler handle this.
perl -pi -e 's/^predep_objects=".*$/predep_objects=""/' libtool
perl -pi -e 's/^postdep_objects=".*$/postdep_objects=""/' libtool
perl -pi -e 's/-shared -nostdlib/-shared/' libtool

%make_build

# Run some quick subsystem checks
echo "source ../../test/tcl/test.tcl; r env; r mut; r memp" | tclsh%{__tclversion}
popd

pushd db_converter-%{_converter_version}
# libdb-5.3.a is part of static package, build produces libdb.a
sed -i 's/-ldb-5.3/-ldb/g' Makefile
# Set path to headers and library to previously built files
# since this tool is intended to build statically
make LDFLAGS="-I../dist/dist-tls -L../dist/dist-tls -Wl,-z,now $RPM_LD_FLAGS" CFLAGS="-g -fPIC %build_cflags" static
popd

%install
%if %{with subpackages}
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
%make_install STRIP=/bin/true -C dist/dist-tls

# XXX Nuke non-versioned archives and symlinks
rm -f ${RPM_BUILD_ROOT}%{_libdir}/{libdb.a,libdb_cxx.a,libdb_tcl.a,libdb_sql.a}

chmod +x ${RPM_BUILD_ROOT}%{_libdir}/*.so*

# Move the header files to a subdirectory, in case we're deploying on a
# system with multiple versions of DB installed.
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/%{name}
mv ${RPM_BUILD_ROOT}%{_includedir}/*.h ${RPM_BUILD_ROOT}%{_includedir}/%{name}/

# Create symlinks to includes so that "use <db.h> and link with -ldb" works.
for i in db.h db_cxx.h db_185.h; do
	ln -s %{name}/$i ${RPM_BUILD_ROOT}%{_includedir}
done

# Eliminate installed doco
rm -rf ${RPM_BUILD_ROOT}%{_prefix}/docs

# XXX Avoid Permission denied. strip when building as non-root.
chmod u+w ${RPM_BUILD_ROOT}%{_bindir} ${RPM_BUILD_ROOT}%{_bindir}/*

# remove unneeded .la files (#225675)
rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.la

# remove RPATHs
chrpath -d ${RPM_BUILD_ROOT}%{_libdir}/*.so ${RPM_BUILD_ROOT}%{_bindir}/*

# unify documentation and examples, remove stuff we don't need
rm -rf docs/csharp
rm -rf examples/csharp
rm -rf docs/installation
mv examples docs
mv man/* ${RPM_BUILD_ROOT}%{_mandir}/man1

%ldconfig_scriptlets
%ldconfig_scriptlets cxx
%ldconfig_scriptlets sql
%ldconfig_scriptlets tcl
%else
mkdir -p %{buildroot}%{_bindir}
%endif
install -m 0755 db_converter-%{_converter_version}/db_converter %{buildroot}/%{_bindir}/db_converter

%files
%license LICENSE lgpl-2.1.txt
%if %{with subpackages}
%doc README
%{_libdir}/libdb-%{__soversion}.so
%{_libdir}/libdb-%{__soversion_major}.so
%else
%{_bindir}/db_converter
%endif

%if %{with subpackages}
%files devel
%{_libdir}/libdb.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/db.h
%{_includedir}/%{name}/db_185.h
%{_includedir}/db.h
%{_includedir}/db_185.h
%endif

%if %{with subpackages}
%files devel-doc
%doc	docs/*
%endif

%if %{with subpackages}
%files devel-static
%{_libdir}/libdb-%{__soversion}.a
%{_libdir}/libdb_cxx-%{__soversion}.a
%{_libdir}/libdb_tcl-%{__soversion}.a
%{_libdir}/libdb_sql-%{__soversion}.a
%endif

%if %{with subpackages}
%files utils
%{_bindir}/db*_archive
%{_bindir}/db*_checkpoint
%{_bindir}/db*_deadlock
%{_bindir}/db*_dump*
%{_bindir}/db*_hotbackup
%{_bindir}/db*_load
%{_bindir}/db*_printlog
%{_bindir}/db*_recover
%{_bindir}/db*_replicate
%{_bindir}/db*_stat
%{_bindir}/db*_upgrade
%{_bindir}/db*_verify
%{_bindir}/db*_tuner
%{_mandir}/man1/db_*
%endif

%if %{with subpackages}
%files convert-util
%{_bindir}/db_converter
%endif

%if %{with subpackages}
%files cxx
%{_libdir}/libdb_cxx-%{__soversion}.so
%{_libdir}/libdb_cxx-%{__soversion_major}.so
%endif

%if %{with subpackages}
%files cxx-devel
%{_includedir}/%{name}/db_cxx.h
%{_includedir}/db_cxx.h
%{_libdir}/libdb_cxx.so
%endif

%if %{with subpackages}
%files tcl
%{_libdir}/libdb_tcl-%{__soversion}.so
%{_libdir}/libdb_tcl-%{__soversion_major}.so
%endif

%if %{with subpackages}
%files tcl-devel
%{_libdir}/libdb_tcl.so
%endif

%if %{with subpackages}
%files sql
%{_libdir}/libdb_sql-%{__soversion}.so
%{_libdir}/libdb_sql-%{__soversion_major}.so
%endif

%if %{with subpackages}
%files sql-devel
%{_bindir}/dbsql
%{_libdir}/libdb_sql.so
%{_includedir}/%{name}/dbsql.h
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.3.28-67
- Prepare for Oreon 11 (RP1)
