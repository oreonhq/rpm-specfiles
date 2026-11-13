# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a41076e3710746326c3945042994ad9a4fcac0ce0277dd8fea076fec3c9772b5
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: apr-util
Version: 1.6.3
Release: 1%{?dist}
Summary: Apache Portable Runtime Utility library
License: Apache-2.0
URL: https://apr.apache.org/
Source0: https://archive.apache.org/dist/apr/apr-util-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: make
BuildRequires: apr-devel
BuildRequires: openssl-devel
BuildRequires: expat-devel
BuildRequires: sqlite-devel

%description
Apache Portable Runtime Utility library.

%package devel
Summary: Development files for apr-util
Requires: apr-util%{?_isa} = %{version}-%{release}
Requires: apr-devel

%description devel
Headers and libraries for building against apr-util.

%prep
%oreon_sha256
%autosetup -n apr-util-%{version}

%build
export CC=clang
%configure --with-apr=%{_prefix} --with-openssl --with-crypto --with-sqlite3 --with-expat=%{_prefix} --disable-static
# apr-1-config from base apr still injects gcc + fedora -specs
sed -i \
    -e 's/^CC *=.*/CC = clang/' \
    -e 's|-specs=/usr/lib/rpm/redhat/[^[:space:]]*||g' \
    Makefile
%{make_build} CC=clang CFLAGS="%{optflags}"

%install
%make_install
rm -f %{buildroot}%{_libdir}/libaprutil-1.la
%oreon_filelist_devel

%check
make check CC=clang CFLAGS="%{optflags}"

%files -f %{_builddir}/%{name}.files
%files devel -f %{_builddir}/%{name}-devel.files
