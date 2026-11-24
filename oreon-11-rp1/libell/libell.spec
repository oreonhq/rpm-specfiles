# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 39a562f5ab2768e69da1ffbb1f98a8eb3483baffc7d2ef6adc3705e4fd4e53fb
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libell
Version:        0.83
Release:        1%{?dist}
Summary:        Embedded Linux library
License:        LGPL-2.0-or-later
URL:            https://01.org/ell
Source0:        https://www.kernel.org/pub/linux/libs/ell/ell-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  make

%description
The Embedded Linux* Library (ELL) provides core, low-level functionality for
system daemons. It typically has no dependencies other than the Linux kernel, C
standard library, and libdl (for dynamic linking). While ELL is designed to be
efficient and compact enough for use on embedded Linux platforms, it is not
limited to resource-constrained systems.

%package devel
Summary:        Embedded Linux library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers for developing against libell.

%prep
%oreon_sha256
%autosetup -p1 -n ell-%{version}

%build
%configure
%make_build V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/libell.so.*

%files devel
%{_includedir}/ell
%{_libdir}/libell.so
%{_libdir}/pkgconfig/ell.pc

%changelog
%autochangelog
