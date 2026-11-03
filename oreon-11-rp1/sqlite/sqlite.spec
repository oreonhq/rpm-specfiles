%global sqlite_ver 3540100
%global source0_hash 926ef8d3eab93fbf6e06011901273eec076b25594a4e1cdadd50c987f4f6d64e
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: sqlite
Version: 3.54.1
Release: 4%{?dist}
Summary: SQL database engine
License: blessing
URL: https://www.sqlite.org/
Source0: https://www.sqlite.org/2026/sqlite-autoconf-%{sqlite_ver}.tar.gz
Requires: sqlite-libs%{?_isa} = %{version}-%{release}

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: readline-devel
BuildRequires: zlib-devel
BuildRequires: patchelf

%description
SQLite is a C library that implements a small, fast, self-contained SQL database engine.

%package libs
Summary: Shared library for SQLite

%description libs
The SQLite shared library.

%package devel
Summary: SQL database engine
Requires: sqlite-libs%{?_isa} = %{version}-%{release}

%description devel
SQLite is a C library that implements a small, fast, self-contained SQL database engine.

%prep
%oreon_sha256
%autosetup -n sqlite-autoconf-%{sqlite_ver} -p1

%build
%oreon_configure --disable-static --disable-rpath --enable-fts5 --enable-rtree --enable-threadsafe
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_docdir}
lib=%{buildroot}%{_libdir}/libsqlite3.so.%{version}
patchelf --set-soname libsqlite3.so.0 "$lib"
rm -f %{buildroot}%{_libdir}/libsqlite3.so.0 %{buildroot}%{_libdir}/libsqlite3.so
mv "$lib" %{buildroot}%{_libdir}/libsqlite3.so.0
ln -s libsqlite3.so.0 %{buildroot}%{_libdir}/libsqlite3.so

%ldconfig_scriptlets libs

%files
%{_bindir}/sqlite3
%{_mandir}/man1/sqlite3.1*

%files libs
%{_libdir}/libsqlite3.so.0

%files devel
%{_includedir}/sqlite3.h
%{_includedir}/sqlite3ext.h
%{_libdir}/libsqlite3.so
%{_libdir}/pkgconfig/sqlite3.pc
