# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c06d7efe860dbe9687cf637dacd5d6bea50de054533057df77d6f638a4587bbd
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: opencsd
Version: 1.8.4
Release: 1%{?dist}
Summary: An open source CoreSight(tm) Trace Decode library
License: BSD-3-Clause
URL: https://github.com/Linaro/OpenCSD
Source0: https://github.com/Linaro/OpenCSD/archive/v%{version}.tar.gz#/OpenCSD-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: make
BuildRequires: python3

%description
This library provides an API suitable for the decode of ARM(r)
CoreSight(tm) trace streams.

%package devel
Summary: Development files for the CoreSight(tm) Trace Decode library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The opencsd-devel package contains headers and libraries needed
to develop CoreSight(tm) trace decoders.

%prep
%oreon_sha256
%autosetup -p1 -n OpenCSD-%{version}

%build
cd decoder/build/linux
export CFLAGS="%{build_cflags}"
export CXXFLAGS="%{build_cxxflags}"
export LDFLAGS="%{build_ldflags}"
LIB_PATH=%{_lib} %make_build MASTER_CC=%{__cc} MASTER_CXX=%{__cxx} MASTER_LINKER=%{__cxx}

%install
cd decoder/build/linux
PREFIX=%{buildroot}%{_prefix} LIB_PATH=%{_lib} make MASTER_CC=%{__cc} MASTER_CXX=%{__cxx} MASTER_LINKER=%{__cxx} install install_man DISABLE_STATIC=1 DEF_SO_PERM=755

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{python3} decoder/tests/run_pkt_decode_tests.py --bin-dir %{buildroot}%{_bindir}

%files
%license LICENSE
%doc HOWTO.md README.md
%{_libdir}/libopencsd.so.1*
%{_libdir}/libopencsd_c_api.so.1*
%{_bindir}/trc_pkt_lister
%{_mandir}/man1/trc_pkt_lister.1*

%files devel
%doc decoder/docs/prog_guide/*
%{_includedir}/opencsd/
%{_libdir}/libopencsd.so
%{_libdir}/libopencsd_c_api.so

%changelog
%autochangelog
