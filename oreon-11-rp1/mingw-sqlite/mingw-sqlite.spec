%global source0_hash none

%{?mingw_package_header}

%global name1 sqlite

%define realver %(echo %{version} | awk -F. '{printf "%d%02d%02d00", $1, $2, $3}')

# bcond default logic is nicely backwards...
%bcond_with tcl
%global tclversion 8.6

Name:           mingw-%{name1}
Version:        3.51.2
Release:        1%{?dist}
Summary:        MinGW Windows port of sqlite embeddable SQL database engine

License:        blessing
URL:            http://www.sqlite.org/
Source0:        http://www.sqlite.org/2026/%{name1}-src-%{realver}.zip

BuildArch:      noarch

# sqlite uses some home baked configure mechanism. Don't make unknown options fatal
Patch0:         sqlite-unknown-option.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  tcl

BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-pdcurses
BuildRequires:  mingw32-readline
BuildRequires:  mingw32-termcap

BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-pdcurses
BuildRequires:  mingw64-readline
BuildRequires:  mingw64-termcap


%if %{with tcl}
BuildRequires:  mingw32-tcl
BuildRequires:  mingw64-tcl
%endif


%description
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

This package contains cross-compiled libraries and development tools
for Windows.


# Win32
%package -n mingw32-%{name1}
Summary:        MinGW Windows port of sqlite embeddable SQL database engine
Requires:       pkgconfig

%description -n mingw32-%{name1}
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

This package contains cross-compiled libraries and development tools
for Windows.

%package -n mingw32-%{name1}-static
Summary:        Static version of MinGW Windows port of sqlite library
Requires:       mingw32-%{name1} = %{version}-%{release}

%description -n mingw32-%{name1}-static
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

This package contains static cross-compiled library

# Win64
%package -n mingw64-%{name1}
Summary:        MinGW Windows port of sqlite embeddable SQL database engine
Requires:       pkgconfig

%description -n mingw64-%{name1}
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

This package contains cross-compiled libraries and development tools
for Windows.

%package -n mingw64-%{name1}-static
Summary:        Static version of MinGW Windows port of sqlite library
Requires:       mingw64-%{name1} = %{version}-%{release}

%description -n mingw64-%{name1}-static
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

This package contains static cross-compiled library


%{?mingw_debug_package}


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name1}-src-%{realver}


%build
# add compile flags to enable rtree, fts3
export MINGW32_CFLAGS="%{mingw32_cflags} -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_DISABLE_DIRSYNC=1 -DSQLITE_ENABLE_FTS3=3 -DSQLITE_ENABLE_RTREE=1 -fno-strict-aliasing"
export MINGW64_CFLAGS="%{mingw64_cflags} -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_DISABLE_DIRSYNC=1 -DSQLITE_ENABLE_FTS3=3 -DSQLITE_ENABLE_RTREE=1 -fno-strict-aliasing"

%mingw_configure %{!?with_tcl:--disable-tcl} --enable-all --enable-load-extension
%mingw_make_build


%install
%mingw_make_install

chmod 0644 %{buildroot}%{mingw32_libdir}/libsqlite3.dll.a
chmod 0644 %{buildroot}%{mingw64_libdir}/libsqlite3.dll.a

%if %{with tcl}
install -d -m755 %{buildroot}%{mingw32_datadir}/tcl%{tclversion}/sqlite3/
mv %{buildroot}%{_datadir}/tcl%{tclversion}/sqlite3/pkgIndex.tcl %{buildroot}%{mingw32_datadir}/tcl%{tclversion}/sqlite3/

install -d -m755 %{buildroot}%{mingw64_datadir}/tcl%{tclversion}/sqlite3/
mv %{buildroot}%{_datadir}/tcl%{tclversion}/sqlite3/pkgIndex.tcl %{buildroot}%{mingw64_datadir}/tcl%{tclversion}/sqlite3/
%endif

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Drop man pages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}


# Win32
%files -n mingw32-%{name1}
%doc README.md VERSION
%{mingw32_bindir}/sqlite3.exe
%{mingw32_bindir}/libsqlite3-0.dll
%{mingw32_libdir}/libsqlite3.dll.a
%{mingw32_includedir}/sqlite3.h
%{mingw32_includedir}/sqlite3ext.h
%{mingw32_libdir}/pkgconfig/sqlite3.pc
%if %{with tcl}
%{mingw32_datadir}/tcl%{tclversion}/sqlite3/
%{mingw32_datadir}/tcl%{tclversion}/sqlite3/pkgIndex.tcl
%endif

%files -n mingw32-%{name1}-static
%{mingw32_libdir}/libsqlite3.a

# Win64
%files -n mingw64-%{name1}
%doc README.md VERSION
%{mingw64_bindir}/sqlite3.exe
%{mingw64_bindir}/libsqlite3-0.dll
%{mingw64_libdir}/libsqlite3.dll.a
%{mingw64_includedir}/sqlite3.h
%{mingw64_includedir}/sqlite3ext.h
%{mingw64_libdir}/pkgconfig/sqlite3.pc
%if %{with tcl}
%{mingw64_datadir}/tcl%{tclversion}/sqlite3/
%{mingw64_datadir}/tcl%{tclversion}/sqlite3/pkgIndex.tcl
%endif

%files -n mingw64-%{name1}-static
%{mingw64_libdir}/libsqlite3.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.51.2-1
- Prepare for Oreon 11 (RP1)
