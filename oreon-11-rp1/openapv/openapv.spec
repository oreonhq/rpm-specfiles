# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 38f841ce44e80c40b682a5323b4f3ebc6e339b6071965bc1c705a17d46ab2fc8
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global abi 11

Name:          openapv
Release:        %{autorelease}
Version:       1.1.3.0
Summary:       Open Advanced Professional Video Codec
License:       BSD-3-Clause
URL:           https://github.com/AcademySoftwareFoundation/openapv
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: cmake
BuildRequires: ninja-build
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

%description
OpenAPV provides the reference implementation of the APV codec which can
be used to record professional-grade video and associated metadata
without quality degradation.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The openapv-devel package contains the header files needed
to develop programs that use openapv.

%package libs
Summary: Shared libraries for openapv

%description libs
The openapv-libs package contains the shared library files

%prep
%oreon_sha256
%autosetup -p1

%build
%cmake \
        -G Ninja \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_SKIP_INSTALL_RPATH=ON \
        -DOAPV_APP_STATIC_BUILD=OFF

%cmake_build

%install
%cmake_install
rm -v %{buildroot}%{_libdir}/liboapv.a

%check
%ctest

%files
%{_bindir}/oapv_app_dec
%{_bindir}/oapv_app_enc

%files devel
%{_libdir}/liboapv.so
%{_libdir}/pkgconfig/oapv.pc
%{_includedir}/oapv/

%files libs
%license LICENSE
%doc README.md
%{_libdir}/liboapv.so.%{abi}{,.*}

%changelog
%autochangelog
