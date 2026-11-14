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
BuildRequires: libtool
BuildRequires: apr-devel
BuildRequires: openssl-devel
BuildRequires: expat-devel
BuildRequires: sqlite-devel
BuildRequires: libuuid-devel
BuildRequires: libxcrypt-devel

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
export CFLAGS="%{optflags}"
export LDFLAGS="%{build_ldflags}"
%configure --with-apr=%{_prefix} --with-openssl --with-crypto --with-sqlite3 --with-expat=%{_prefix} --disable-static
find . -type f \( -name Makefile -o -name '*.mk' -o -name 'libtool' -o -name '*.la' -o -name 'apu-*-config' \) -print0 \
  | xargs -0 sed -i \
    -e 's/^CC *=.*/CC = clang/' \
    -e 's|^LIBTOOL *=.*|LIBTOOL = %{_bindir}/libtool|' \
    -e 's|-specs=/usr/lib/rpm/redhat/[^[:space:]]*||g' \
    -e 's|%{_libdir}/libapr-1\.la|-lapr-1|g' \
    -e 's|/usr/lib/libapr-1\.la|-lapr-1|g'
%{make_build} CC=clang CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" APRUTIL_LDFLAGS="%{build_ldflags}" LIBTOOL="%{_bindir}/libtool"

%install
%make_install LIBTOOL="%{_bindir}/libtool"
rm -f %{buildroot}%{_libdir}/libaprutil-1.la
%oreon_filelist_devel

%check
make check CC=clang CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" APRUTIL_LDFLAGS="%{build_ldflags}" LIBTOOL="%{_bindir}/libtool"

%files -f %{_builddir}/%{name}.files
%files devel -f %{_builddir}/%{name}-devel.files
