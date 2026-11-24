# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f29508c335c83d8703f943ffc9ca783ac39aca84e851357f13a55af0f8143137
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libmysofa
Version:        1.3.5
Release:        1%{?dist}
Summary:        C functions for reading HRTFs

License:        BSD-3-Clause
URL:            https://github.com/hoene/libmysofa
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(zlib)
BuildRequires: make
%{?!_without_tests:BuildRequires: nodejs, /usr/bin/node}

%description
This is a simple set of C functions to read AES SOFA files, if they
contain HRTFs stored according to the AES69-2015 standard.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n mysofa
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n mysofa
Tools for %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%cmake \
  -DBUILD_STATIC_LIBS=OFF \
  -DCODE_COVERAGE=OFF \
  -DCMAKE_VERBOSE_MAKEFILE=ON

%cmake_build

%install
%cmake_install

%{?!_without_tests:
%check
export MYSOFA2JSON=%{_builddir}/%{buildsubdir}/%{_vpath_builddir}/src/mysofa2json
%ctest
}

%files
%license LICENSE
%doc README.md
%{_libdir}/libmysofa.so.1*

%files -n mysofa
%{_bindir}/mysofa2json
%dir %{_datadir}/libmysofa
%{_datadir}/libmysofa/default.sofa
%{_datadir}/libmysofa/MIT_KEMAR_normal_pinna.sofa

%files devel
%doc CODE_OF_CONDUCT.md
%{_includedir}/mysofa.h
%{_includedir}/mysofa_export.h
%{_libdir}/libmysofa.so
%{_libdir}/pkgconfig/libmysofa.pc
%dir %{_libdir}/cmake/mysofa
%{_libdir}/cmake/mysofa/mysofaConfig.cmake
%{_libdir}/cmake/mysofa/mysofaConfigVersion.cmake
%{_libdir}/cmake/mysofa/mysofaTargets-noconfig.cmake
%{_libdir}/cmake/mysofa/mysofaTargets.cmake

%changelog
%autochangelog
