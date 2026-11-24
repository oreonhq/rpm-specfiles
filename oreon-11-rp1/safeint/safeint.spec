# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 489abb253514f819adb7e3aab3273b184c484dfe082fbe2166de2fd3a88dfb2b
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global debug_package %{nil}

Name:           safeint
Version:        3.0.27
Release:        %{autorelease}
Summary:        Class library for C++ that manages integer overflows

License:        MIT
URL:            https://github.com/dcleblanc/SafeInt
Source0:        https://github.com/dcleblanc/SafeInt/archive/%{version}/SafeInt-%{version}.tar.gz

Patch0:         safeint-3.0.27-gcc13_fix.patch
Patch1:         safeint-3.0.27-gcc98_test_rm.patch
Patch2:         safeint-3.0.27-gcc14_test_fix.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake

ExcludeArch: %{ix86}

%global _description %{expand:
An integer overflow library that was originally created in Microsoft
Office in 2003, and later was made open source on CodePlex using the MS-PL
license. After CodePlex was deprecated, the project was moved to github
and the license was changed to the MIT license.}

%description
%{_description}

%package devel
Summary: %{summary}
Provides: %{name}-static = %{version}-%{release}

%description devel
%{_description}

%prep
%oreon_sha256
%autosetup -p1 -n SafeInt-%{version}

%check
%cmake
%cmake_build
%ctest

%build

%install
install -d %{buildroot}%{_includedir}/SafeInt
install -D -p SafeInt.hpp -t %{buildroot}%{_includedir}/SafeInt/
install -D -p safe_math.h -t %{buildroot}%{_includedir}/SafeInt/
install -D -p safe_math_impl.h -t %{buildroot}%{_includedir}/SafeInt/

%files devel
%license LICENSE
%doc README.md
%dir %{_includedir}/SafeInt
%{_includedir}/SafeInt/SafeInt.hpp
%{_includedir}/SafeInt/safe_math.h
%{_includedir}/SafeInt/safe_math_impl.h

%changelog
%autochangelog
