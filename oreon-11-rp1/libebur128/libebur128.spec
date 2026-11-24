# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash baa7fc293a3d4651e244d8022ad03ab797ca3c2ad8442c43199afe8059faa613
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond tests 0

Name:           libebur128
Version:        1.2.6
Release:        1%{?dist}
Summary:        A library that implements the EBU R 128 standard for loudness normalization
License:        MIT
URL:            https://github.com/jiixyj/%{name}

Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  cmake >= 2.8.11
BuildRequires:  make
%if %{with tests}
BuildRequires:  pkgconfig(sndfile)
%endif

%description
A library that implements the EBU R 128 standard for loudness normalization.

It implements M, S and I modes, loudness range measurement (EBU - TECH 3342),
true peak scanning and all sample-rates by recalculation of the filter
coefficients.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup

%build
%cmake -DENABLE_TESTS:BOOL=%{?_with_tests:ON}%{!?_with_tests:OFF} -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%if %{with tests}
%check
pushd %{_vpath_builddir}/test
make
LD_LIBRARY_PATH=. ./r128-test-library
%endif

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.%{version}

%files devel
%{_includedir}/ebur128.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
