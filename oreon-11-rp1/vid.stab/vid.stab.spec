# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6b51f3efd6b8500c92f3c5d25e158f813d3be078c31c9b480c7ea791b6725e5e
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%undefine __cmake_in_source_build
%global commit 05829db776069b7478dd2d90b6e0081668a41abc
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20230603

Name:           vid.stab
Version:        1.1.1
Release:        1%{?dist}
Summary:        Video stabilize library for fmpeg, mlt or transcode
License:        GPL-2.0-or-later
URL:            http://public.hronopik.de/vid.stab
Source0:        https://github.com/georgmartius/vid.stab/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  orc-devel
Requires:       glibc
Provides:	%{name}-libs = %{version}-%{release}
Obsoletes:	%{name}-libs < %{version}-%{release}

%description
Vidstab is a video stabilization library which can be plugged-in with Ffmpeg
and Transcode.

%package devel
Summary:        Development files for vid.stab
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development files (library and header files).

%prep
%oreon_sha256
%setup -q -n %{name}-%{commit}
sed -i 's|-DUSE_SSE2 -msse2||' tests/CMakeLists.txt
sed -i 's|-Wall -O0|-Wall -O|' tests/CMakeLists.txt
sed -i 's|return units_failed==0;|return units_failed>0;|' tests/testframework.c

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

pushd tests
%cmake
%cmake_build
popd

%install
%cmake_install

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} tests/tests || :

%ldconfig_scriptlets -n %{name}

%files
%doc README.md
%license LICENSE
%{_libdir}/libvidstab.so.*

%files devel
%{_includedir}/vid.stab/
%{_libdir}/libvidstab.so
%{_libdir}/pkgconfig/vidstab.pc

%changelog
%autochangelog
