# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f2672a0381cb59196e9c246bf8bcc43d5568bc457700a697f1a1df762b9af884
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: numactl
Summary: Library for tuning for Non Uniform Memory Access machines
Version: 2.0.19
Release: 1%{?dist}
License: GPL-2.0-only
URL: https://github.com/numactl/numactl
Source0: %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: make
BuildRequires: libtool
BuildRequires: automake
BuildRequires: autoconf
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

ExcludeArch: s390 %{arm}

%description
Simple NUMA policy support. It consists of a numactl program to run
other programs with a specific NUMA policy.

%package libs
Summary: libnuma libraries
License: LGPL-2.1-only AND GPL-2.0-only

%description libs
numactl-libs provides libnuma, a library to do allocations with
NUMA policy in applications.

%package devel
Summary: Development package for building Applications that use numa
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
License: LGPL-2.1-only AND GPL-2.0-only

%description devel
Provides development headers for numa library calls.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/libnuma.la

%files
%license LICENSE.GPL2
%doc README.md
%{_bindir}/numactl
%{_bindir}/numademo
%{_bindir}/numastat
%{_bindir}/memhog
%{_bindir}/migspeed
%{_bindir}/migratepages
%{_mandir}/man8/*.8*
%exclude %{_mandir}/man2/*.2*

%files libs
%license LICENSE.LGPL2.1
%{_libdir}/libnuma.so.1.0.0
%{_libdir}/libnuma.so.1

%files devel
%{_libdir}/libnuma.so
%{_libdir}/pkgconfig/numa.pc
%{_includedir}/numa.h
%{_includedir}/numaif.h
%{_includedir}/numacompat1.h
%{_mandir}/man3/*.3*

%changelog
%autochangelog
