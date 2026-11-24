# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b0e5af6b54c274b9670c7e32ddbf6c802d88c896062d760267695dd0aa7014ff
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: Implementation of the JPEG-2000 standard, Part 1
Name:    jasper
Version: 4.2.9
Release: %{autorelease}

License: JasPer-2.0
URL:     http://www.ece.uvic.ca/~frodo/jasper/
Source0: https://github.com/jasper-software/%{name}/archive/refs/tags/version-%{version}.tar.gz

Patch100: jasper-2.0.2-test-ppc64-disable.patch
Patch101: jasper-2.0.2-test-ppc64le-disable.patch
Patch102: jasper-4.1.0-test-i686-disable.patch

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: freeglut-devel
BuildRequires: libGLU-devel
BuildRequires: libjpeg-devel
BuildRequires: libXmu-devel
BuildRequires: libXi-devel
BuildRequires: pkgconfig
BuildRequires: doxygen
BuildRequires: mesa-libGL-devel

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: clang
BuildRequires: gcc
BuildRequires: make

%description
This package contains an implementation of the image compression
standard JPEG-2000, Part 1. It consists of tools for conversion to and
from the JP2 and JPC formats.

%package devel
Summary: Header files, libraries and developer documentation
Provides: libjasper-devel = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: libjpeg-devel
Requires: pkgconfig
%description devel
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Conflicts: jasper < 1.900.1-4
%description libs
%{summary}.

%package utils
Summary: Nonessential utilities for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description utils
%{summary}, including jiv and tmrdemo.

%prep
%oreon_sha256
%setup -q -n %{name}-version-%{version}

%if "%{_arch}" == "ppc64"
%patch 100 -p1 -b .test-ppc64-disable
%endif

%if "%{_arch}" == "ppc64le"
%patch 101 -p1 -b .test-ppc64le-disable
%endif

%ifarch %ix86
%patch 102 -p1 -b .test-i686-disable
%endif

%build
%cmake \
  -DJAS_ENABLE_DOC:BOOL=OFF \
  -DALLOW_IN_SOURCE_BUILD:BOOL=ON \

%cmake_build 

%install
%cmake_install

rm -f doc/README
rm -f %{buildroot}%{_libdir}/lib*.la

%check
%ctest 

%ldconfig_scriptlets libs

%files
%{_bindir}/imgcmp
%{_bindir}/imginfo
%{_bindir}/jasper
%{_mandir}/man1/img*
%{_mandir}/man1/jasper.1*
%{_docdir}/JasPer/*

%files devel
%doc doc/*
%{_includedir}/jasper/
%{_libdir}/libjasper.so
%{_libdir}/pkgconfig/jasper.pc

%files libs
%doc README.md
%license COPYRIGHT.txt LICENSE.txt
%{_libdir}/libjasper.so.7*

%files utils
%{_bindir}/jiv
%{_mandir}/man1/jiv.1*

%changelog
%autochangelog
