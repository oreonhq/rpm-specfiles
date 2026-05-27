%global source0_hash 652a98ca833ed638809a52bec225a7f37799f71a995778f9ccb68ad03bd1fc11
%global source1_hash 6f0d517e0c47e6446c74cf5503c87312181b80f04c95743f99f05af3ccc5e5a6
%global source2_hash f6b50b0c103392af32a8be15b2b9d25959de9a00a70c3979128aafeaa5338b3f

# bcond default logic is nicely backwards...
%bcond_without tcl
%bcond_without tools
%bcond_with static
%bcond_without check

%define majorver 3
%define realver 3520000
%define docver 3520000
%define rpmver 3.52.0
%define year 2026

Summary: Library that implements an embeddable SQL database engine
Name: sqlite
Version: %{rpmver}
Release: 1%{?dist}
License: blessing
URL: http://www.sqlite.org/

Source0: http://www.sqlite.org/%{year}/sqlite-src-%{realver}.zip
Source1: http://www.sqlite.org/%{year}/sqlite-doc-%{docver}.zip
Source2: http://www.sqlite.org/%{year}/sqlite-autoconf-%{realver}.tar.gz
# Support a system-wide lemon template
Patch1: sqlite-3.6.23-lemon-system-template.patch
Patch2: sqlite-3.49.0-fix-lemon-missing-cflags.patch

BuildRequires: make
BuildRequires: gcc gcc-c++
BuildRequires: ncurses-devel readline-devel glibc-devel
BuildRequires: autoconf
BuildRequires: /usr/bin/tclsh
BuildRequires: zlib-ng-compat-devel
BuildRequires: chrpath
%if %{with tcl}
BuildRequires: tcl-devel
%{!?tcl_version: %global tcl_version 9.0}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%endif

Requires: %{name}-libs = %{version}-%{release}
Provides: %{name}3 = %{version}-%{release}

# Ensure updates from pre-split work on multi-lib systems
Obsoletes: %{name} < 3.11.0-1
Conflicts: %{name} < 3.11.0-1

%description
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server. Version 2 and version 3 binaries
are named to permit each to be installed on a single host

SQLite is built with some non-default settings:
- Additional APIs for table's and query's metadata are enabled 
  (SQLITE_ENABLE_COLUMN_METADATA)
- Directory syncs are disabled (SQLITE_DISABLE_DIRSYNC)
- `secure_delete` defaults to 'on', so deleted content is overwritten
  with zeros (SQLITE_SECURE_DELETE)
- `sqlite3_unlock_notify()` is enabled - this feature allows to register a 
  callback that's invoked when lock is removed (SQLITE_ENABLE_UNLOCK_NOTIFY)
- `dbstat` virtual table with disk space usage is enabled
- `dbpage` virtual table providing direct access to underlying database file
  is enabled (SQLITE_ENABLE_DBPAGE_VTAB)
- Threadsafe mode is set to 1 - Serialized, so it is safe to use in a 
  multithreaded environment (SQLITE_THREADSAFE=1)
- FTS3, FTS4 and FTS5 are enabled so versions 3 to 5 of the full-text search
  engine are available (SQLITE_ENABLE_FTS3, SQLITE_ENABLE_FTS4, 
  SQLITE_ENABLE_FTS5)
- Pattern parser in FTS3 extension supports nested parenthesis and operators
  `AND`, `OR` (SQLITE_ENABLE_FTS3_PARENTHESIS)
- R*Tree index extension is enabled (SQLITE_ENABLE_RTREE)
- Extension loading is enabled
- Sessions (sqlite-session feature) is enabled
- Preupdate hook is enabled

It is also important to note that shell has some extensions as its dependencies,
so some extensions are enabled by default in SQLite shell, but not in the system
libraries. Only the aforementioned extensions are available in the libraries:
FTS3, FTS4, FTS5, R*Tree


%package devel
Summary: Development tools for the sqlite3 embeddable SQL database engine
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files and development documentation 
for %{name}. If you like to develop programs using %{name}, you will need 
to install %{name}-devel.

%package libs
Summary: Shared library for the sqlite3 embeddable SQL database engine.

# Ensure updates from pre-split work on multi-lib systems
Obsoletes: %{name} < 3.11.0-1
Conflicts: %{name} < 3.11.0-1

%description libs
This package contains the shared library for %{name}.

%package doc
Summary: Documentation for sqlite
BuildArch: noarch

%description doc
This package contains most of the static HTML files that comprise the
www.sqlite.org website, including all of the SQL Syntax and the 
C/C++ interface specs and other miscellaneous documentation.

%package -n lemon
Summary: A parser generator

%description -n lemon
Lemon is an LALR(1) parser generator for C or C++. It does the same
job as bison and yacc. But lemon is not another bison or yacc
clone. It uses a different grammar syntax which is designed to reduce
the number of coding errors. Lemon also uses a more sophisticated
parsing engine that is faster than yacc and bison and which is both
reentrant and thread-safe. Furthermore, Lemon implements features
that can be used to eliminate resource leaks, making is suitable for
use in long-running programs such as graphical user interfaces or
embedded controllers.


%package debug
Summary: SQLite shell configured for development and debugging purposes

%description debug
This version of SQLite shell contains features that are useful for
debugging purposes. These features are not present in a normal SQLite shell
because some have negative impact on a non-developer user experience.

Current list of modification from normal SQLite shell (in sqlite package):
- Ability to enable .scanstats for metrics regarding query speeds


%if %{with tools}
%package tools
Summary: %{name} tools
Group: Development/Tools

%description tools
%{name} related tools. Contains sqldiff and sqlite3_rsync.
- sqldiff: The sqldiff binary is a command-line utility program
  that displays the differences between SQLite databases.
- sqlite3_rsync: A command-line utility that efficiently creates
  or updates a copy of an SQLite database using rsync.
%endif

%if %{with tcl}
%package tcl
Summary: Tcl module for the sqlite3 embeddable SQL database engine
Requires: %{name} = %{version}-%{release}
Requires: tcl(abi) = %{tcl_version}

%description tcl
This package contains the tcl modules for %{name}.

%package analyzer
Summary: An analysis program for sqlite3 database files
Requires: %{name} = %{version}-%{release}
Requires: tcl(abi) = %{tcl_version}

%description analyzer
This package contains the analysis program for %{name}.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%(test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; })
%setup -q -a1 -n %{name}-src-%{realver}
%patch -P 1 -p1
%patch -P 2 -p1

# The atof test is failing on the i686 architecture, when binary configured with
# --enable-rtree option. Failing part is text->real conversion and
# text->real->text conversion in lower significant values after decimal point in a number.
# func4 tests fail for i686 on float<->int conversions.
%ifarch == i686
rm test/atof1.test
rm test/func4.test
%endif

# Remove backup-file
rm -f %{name}-doc-%{docver}/sqlite.css~ || :

#autoupdate
#autoconf # Rerun with new autoconf to add support for aarm64

%build
# First build executable for debug subpackage
# following CFLAGS are not possible to set via the configure script
export CFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS \
               -DSQLITE_ENABLE_COLUMN_METADATA=1 \
               -DSQLITE_DISABLE_DIRSYNC=1 \
               -DSQLITE_SECURE_DELETE=1 \
               -DSQLITE_ENABLE_UNLOCK_NOTIFY=1 -DSQLITE_ENABLE_DBSTAT_VTAB=1 \
               -DSQLITE_ENABLE_FTS3_PARENTHESIS=1 \
               -DSQLITE_ENABLE_STMT_SCANSTATUS \
               -DSQLITE_ENABLE_DBPAGE_VTAB \
               -DSQLITE_ENABLE_SESSION \
               -DSQLITE_ENABLE_PREUPDATE_HOOK \
               -Wall -fno-strict-aliasing"

%configure %{!?with_tcl:--disable-tcl} \
           --enable-rtree \
           --enable-fts3 \
           --enable-fts4 \
           --enable-fts5 \
           --enable-threadsafe \
           --enable-load-extension \
           --soname=legacy \
           --disable-static

%make_build

mv sqlite3 sqlite3-debug

make clean

# Now rebuild rest of the packages normally
export CFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS \
               -DSQLITE_ENABLE_COLUMN_METADATA=1 \
               -DSQLITE_DISABLE_DIRSYNC=1 \
               -DSQLITE_SECURE_DELETE=1 \
               -DSQLITE_ENABLE_UNLOCK_NOTIFY=1 -DSQLITE_ENABLE_DBSTAT_VTAB=1 \
               -DSQLITE_ENABLE_FTS3_PARENTHESIS=1 \
               -DSQLITE_ENABLE_DBPAGE_VTAB \
               -DSQLITE_ENABLE_SESSION \
               -DSQLITE_ENABLE_PREUPDATE_HOOK \
               -Wall -fno-strict-aliasing"

%configure %{!?with_tcl:--disable-tcl} \
           --enable-rtree \
           --enable-fts3 \
           --enable-fts4 \
           --enable-fts5 \
           --enable-threadsafe \
           --enable-load-extension \
           --soname=legacy \
           --disable-static

%make_build

# Build sqlite3_analyzer
# depends on tcl
%if %{with tcl}
%make_build sqlite3_analyzer
%endif

# Build tools
%if %{with tools}
%make_build sqldiff
%make_build sqlite3_rsync
%endif

%install
mkdir -p ${RPM_BUILD_ROOT}%{tcl_sitearch}
%make_install

install -D -m0644 sqlite3.1 $RPM_BUILD_ROOT/%{_mandir}/man1/sqlite3.1
install -D -m0755 lemon $RPM_BUILD_ROOT/%{_bindir}/lemon
install -D -m0644 tool/lempar.c $RPM_BUILD_ROOT/%{_datadir}/lemon/lempar.c
install -D -m0755 sqlite3-debug $RPM_BUILD_ROOT/%{_bindir}/sqlite3-debug

%if %{with tcl}
# fix up permissions to enable dep extraction
install -d $RPM_BUILD_ROOT%{tcl_sitearch}
mv $RPM_BUILD_ROOT%{_datadir}/tcl%{tcl_version}/sqlite* $RPM_BUILD_ROOT%{tcl_sitearch}/
chmod 0755 ${RPM_BUILD_ROOT}/%{tcl_sitearch}/sqlite*/*.so
# Install sqlite3_analyzer
install -D -m0755 sqlite3_analyzer $RPM_BUILD_ROOT/%{_bindir}/sqlite3_analyzer
%endif

# Install tools
%if %{with tools}
install -D -m0755 sqldiff $RPM_BUILD_ROOT/%{_bindir}/sqldiff
install -D -m0755 sqlite3_rsync $RPM_BUILD_ROOT/%{_bindir}/sqlite3_rsync
%endif

%if ! %{with static}
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.{la,a}
%endif

# This is needed since rpath removal using sed won't work for tcl library for some reason
chrpath --delete $RPM_BUILD_ROOT/%{tcl_sitearch}/sqlite*/*.so
chrpath --delete $RPM_BUILD_ROOT/%{_libdir}/*.so.%{version}

chrpath --delete $RPM_BUILD_ROOT/%{_bindir}/sqlite3
chrpath --delete $RPM_BUILD_ROOT/%{_bindir}/sqlite3-debug
chrpath --delete $RPM_BUILD_ROOT/%{_bindir}/sqldiff
chrpath --delete $RPM_BUILD_ROOT/%{_bindir}/sqlite3_rsync
chrpath --delete $RPM_BUILD_ROOT/%{_bindir}/sqlite3_analyzer

%if %{with check}
%check
# XXX shell tests are broken due to loading system libsqlite3, work around...
export LD_LIBRARY_PATH=`pwd`/.libs
export MALLOC_CHECK_=3

# csv01 hangs on all non-intel archs i've tried
%ifarch x86_64 %{ix86}
%else
rm test/csv01.test
%endif

make test
%endif
# ends %%{with check} if

%ldconfig_scriptlets libs

%files
%{_bindir}/sqlite3
%{_mandir}/man?/*

%files libs
%license LICENSE.md
%doc README.md
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.0

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%if %{with static}
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%endif

%files doc
%doc %{name}-doc-%{docver}/*

%files -n lemon
%{_bindir}/lemon
%{_datadir}/lemon

%files debug
%{_bindir}/sqlite3-debug

%if %{with tcl}
%files tcl
%{tcl_sitearch}/sqlite*

%if %{with tools}
%files tools
%{_bindir}/sqldiff
%{_bindir}/sqlite3_rsync
%endif

%files analyzer
%{_bindir}/sqlite3_analyzer
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{rpmver}-1
- Prepare for Oreon 11 (RP1)
