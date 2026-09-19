%global source0_hash 3f35ebfb67867fb5b583a03e480f900206af637efe7179b32294a6a0cf806f37

%{!?tcl_version: %global tcl_version %((echo 0; echo 'puts $tcl_version' | tclsh8) | tail -1)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

# This package is old and only kept for compatibility.
# There is no real benefit to modernizing the code to support C23.
%global optflags %{optflags} -std=gnu17

# Same logic for not updating to TCL9.

Name:           sqlite2
Version:        2.8.17
Release:        48%{?dist}

Summary:        Embeddable SQL engine in a C library
License:        blessing AND LicenseRef-Fedora-Public-Domain
URL:            http://www.sqlite.org/
Source0:        http://www.sqlite.org/sqlite-%{version}.tar.gz
Patch1:         sqlite-2.8.15.rpath.patch
Patch2:         sqlite-2.8.15-makefile.patch
Patch3:         sqlite-2.8.3.test.rh9.patch
Patch4:         sqlite-64bit-fixes.patch
Patch5:         sqlite-2.8.15-arch-double-differences.patch
Patch6:         sqlite-2.8.17-test.patch
Patch7:         sqlite-2.8.17-tcl.patch
Patch8:         sqlite-2.8.17-ppc64.patch
Patch9:         sqlite-2.8.17-format-security.patch
Patch10:        sqlite-2.8.17-tcl86.patch
Patch11:        sqlite-2.8.17-cleanup-temp-c.patch
Patch12:        sqlite-2.8.17-suse-cleanups.patch
Patch13:        sqlite-2.8.17-suse-detect-sqlite3.patch
Patch14:        sqlite-2.8.17-CVE-2007-1888.patch
Patch15:        sqlite-2.8.17-lemon-snprintf.patch
Patch16:        sqlite-2.8.17-fix-sort-syntax.patch
Patch17:        sqlite-2.8.17-ldflags.patch
Patch18:        sqlite-2.8.17-fix-unsigned-FTBFS.patch
Patch19:        sqlite-2.8.17-gcc10.patch
Patch20:        sqlite2-configure-c99.patch
Patch21:        sqlite2-lemon-c99.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel, readline-devel, tcl8-devel
Obsoletes:      sqlite < 3

%description
SQLite is a small, fast, embeddable SQL database engine that supports
most of SQL92, including transactions with atomic commit and rollback,
subqueries, compound queries, triggers, and views. A complete database
is stored in a single cross-platform disk file. The native C/C++ API
is simple and easy to use. Bindings for other languages are also
available.

%package        devel
Summary:        Development files for SQLite
Requires:       %{name}%{?_isa} = %{version}-%{release}, pkgconfig
Obsoletes:      sqlite-devel < 3

%description    devel
SQLite is a small, fast, embeddable SQL database engine that supports
most of SQL92, including transactions with atomic commit and rollback,
subqueries, compound queries, triggers, and views.
This package contains static library and header files for developing
applications using sqlite.

%package        tcl
Summary:        Tcl bindings for sqlite
%if 0%{?rhel}%{?fedora} > 5
Requires:       tcl(abi) = %{tcl_version}
%else
Requires:       tcl%{?_isa} >= %{tcl_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      sqlite-tcl < 3

%description    tcl
SQLite is a small, fast, embeddable SQL database engine that supports
most of SQL92, including transactions with atomic commit and rollback,
subqueries, compound queries, triggers, and views.
This package contains tcl bindings for sqlite.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n sqlite-%{version}
find . -type d -name CVS -print0 | xargs -0 rm -r
%patch -P1 -p1 -b .rpath
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1 -b .cleanup-tempc
%patch -P12 -p1 -b .suse
%patch -P13 -p1 -b .detect-sqlite3
%patch -P14 -p1 -b .CVE-2007-1888
%patch -P15 -p1 -b .snprintf
%patch -P16 -p1 -b .fix-sort-syntax
%patch -P17 -p1 -b .ldflags
%patch -P18 -p1 -b .unsigned-fix
%patch -P19 -p1 -b .gcc10
%patch -P20 -p1
%patch -P21 -p1
sed -i.rpath 's!__VERSION__!%{version}!g' Makefile.in
# Patch additional /usr/lib locations where we don't have $(libdir)
# to substitute with.
sed -i.lib 's!@exec_prefix@/lib!%{_libdir}!g' Makefile.in

sed -i 's!tclsh !tclsh8 !g' Makefile.in

%build
CFLAGS="$RPM_OPT_FLAGS -DNDEBUG=1"
%configure --enable-utf8 --disable-static --disable-rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make
make tclsqlite libtclsqlite.la doc

%check
#obs. make test doesn't like root
LD_LIBRARY_PATH=./.libs make test

%install
rm -rf $RPM_BUILD_ROOT
DIRECTORY=$RPM_BUILD_ROOT%{_libdir}/sqlite-%{version}
install -d $DIRECTORY
echo 'package ifneeded sqlite 2 [list load [file join $dir libtclsqlite.so]]' > $DIRECTORY/pkgIndex.tcl

%makeinstall
install -D -m 0644 sqlite.1 $RPM_BUILD_ROOT%{_mandir}/man1/sqlite.1
mkdir -p $RPM_BUILD_ROOT%{tcl_sitearch}
mv -f $DIRECTORY $RPM_BUILD_ROOT%{tcl_sitearch}/sqlite2

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{_bindir}/tclsqlite

%ldconfig_scriptlets

%files
%{_bindir}/sql*
%{_libdir}/libsql*.so.*
%{_mandir}/man1/*

%files devel
%doc README doc/*
%{_libdir}/libsql*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%files tcl
%doc doc/tclsqlite.html
%{tcl_sitearch}/sqlite2/

%changelog
%autochangelog
