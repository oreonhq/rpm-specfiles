# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 10053dbc2fa342516b780a6bbf6e7b2a2360b8d49c5ac426936bf3df82526732

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global with_check 1

Name:    libb2
Summary: C library providing BLAKE2b, BLAKE2s, BLAKE2bp, BLAKE2sp
Version:        0.98.1
Release:        1%{?dist}
License: CC0-1.0 OR Apache-1.0 OR Apache-2.0
URL:     https://blake2.net/
Source0:        https://github.com/BLAKE2/libb2/archive/v%{version}/libb2-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: automake
BuildRequires: libtool
BuildRequires: make
BuildRequires:  oreon-rpm-macros

%description
C library providing BLAKE2b, BLAKE2s, BLAKE2bp, BLAKE2sp.

BLAKE2 is a cryptographic hash function faster than MD5, SHA-1, SHA-2,
and SHA-3, yet is at least as secure as the latest standard SHA-3.

%package        devel
Summary:        Development files for the Blake2 library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}.

%prep
%oreon_sha256

%autosetup -n libb2-%{version}

sed -e 's|CFLAGS=-O3|CFLAGS="%{optflags}"|g' -i configure.ac
autoreconf -ivf

%build
%configure --disable-silent-rules --enable-static=no --enable-native=no
%make_build

%if 0%{with_check}
%check
make check
%endif

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/libb2.so.1
%{_libdir}/libb2.so.1.*

%files devel
%{_libdir}/libb2.so
%{_libdir}/pkgconfig/libb2.pc
%{_includedir}/blake2.h

