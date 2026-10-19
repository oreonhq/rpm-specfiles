%global source0_hash 1be0f36485366dcf54eac6d1a9ebc373eb3884d76df9df135bcd60e66bd40fb6
%global __cmake_in_source_build 1
Name:		xbase
Summary:        XBase compatible database library
Version:	4.3.0
Release:        1%{?dist}
License:	LGPL-3.0-or-later
URL:		http://linux.techass.com/projects/xdb/
Source0:        http://downloads.sourceforge.net/xdb/%{name}64-%{version}.tar.gz
Patch0:		xbase-4.2.6-fix-sover.patch
Patch1:		xbase-4.2.6-no-local-no-namespace.patch
Patch2:		xbase-4.2.6-fix-mandir.patch
Patch3:		xbase-4.2.6-missing-includes.patch
Provides:	xbase64 = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
XBase is an xbase (i.e. dBase, FoxPro, etc.) compatible C++ class library
originally by Gary Kunkel and others (see the AUTHORS file).

XBase is useful for accessing data in legacy dBase 3 and 4 database files as
well as a general light-weight database engine.  It includes support for
DBF (dBase version 3 and 4) data files, NDX and NTX indexes, and DBT
(dBase version 3 and 4).  It supports file and record locking under *nix
OS's.

%package devel
Summary:	XBase development libraries and headers
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	xbase64-devel = %{version}-%{release}
%description devel
Headers and libraries for compiling programs that use the XBase library.

%package utils
Summary:	XBase utilities / tools
License:	GPL-3.0-or-later
Provides:	xbase64-utils = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description utils
This package contains various utilities for working with X-Base files:
checkndx (check an NDX file), copydbf (copy a DBF file structure), deletall
(mark all records for deletion), dumphdr (print an X-Base file header),
dumprecs (dump records for an X-Base file), packdbf (pack a database file),
reindex (rebuild an index), undelall (undeletes all deleted records in a file),
zap (remove all records from a DBF file).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}64-%{version}
%patch -P0 -p1 -b .fix-sover
%patch -P1 -p1 -b .no-local-no-namespace
%patch -P2 -p1 -b .fix-mandir
%patch -P3 -p1 -b .missing-includes

chmod -x NEWS README docs/html/*

%build

cd build/linux64
%cmake .
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
pushd build/linux64
%cmake_install
popd
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
touch -r COPYING docs/html/*.html
pushd $RPM_BUILD_ROOT%{_libdir}
ln -s libxbase64.so.%{version} libxbase.so.%{version}
ln -s libxbase64.so.4 libxbase.so.4
ln -s libxbase64.so libxbase.so
popd
pushd $RPM_BUILD_ROOT%{_includedir}
ln -s Xbase64 xbase
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd build/linux64
make test
popd
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n xbase-devel -f %{oreon_filedir}/xbase-devel.list
%files -n xbase-utils -f %{oreon_filedir}/xbase-utils.list

%changelog

%autochangelog
