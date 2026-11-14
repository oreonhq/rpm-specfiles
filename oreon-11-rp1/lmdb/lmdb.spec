# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: OLDAP-2.8

%global source0_hash 7d55c3cbc1ef55f9b0076d3ddb16d0d9996d05b9caa7ca889ce10430ac677b90

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: lmdb
Version: 0.9.36
Release: 1%{?dist}
Summary: Lightning Memory-Mapped Database
License: OLDAP-2.8
URL: https://www.symas.com/lmdb
Source0: https://github.com/LMDB/lmdb/archive/refs/tags/LMDB_%{version}.tar.gz#/lmdb-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make

%description
LMDB is a Btree-based database management library with memory-mapped files.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: lmdb-devel%{?_isa} = %{version}-%{release}
Provides: pkgconfig(lmdb) = %{version}

%description devel
Headers and libraries for %{name}.

%prep
%oreon_sha256
%autosetup -n lmdb-LMDB_%{version} -p1

%build
%make_build -C libraries/liblmdb CC="%{__cc}" CFLAGS="%{optflags}"

%install
%make_install -C libraries/liblmdb prefix=%{_prefix} libdir=%{_libdir} mandir=%{_mandir}
# drop static
rm -f %{buildroot}%{_libdir}/liblmdb.a

%check
%make_build -C libraries/liblmdb test

%files
%license libraries/liblmdb/LICENSE
%doc libraries/liblmdb/CHANGES libraries/liblmdb/intro.doc
%{_bindir}/mdb_copy
%{_bindir}/mdb_dump
%{_bindir}/mdb_load
%{_bindir}/mdb_stat
%{_libdir}/liblmdb.so.*
%{_mandir}/man1/mdb_*.1*

%files devel
%{_includedir}/lmdb.h
%{_libdir}/liblmdb.so

%changelog
%autochangelog
