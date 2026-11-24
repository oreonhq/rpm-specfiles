# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7fa616e3046edfa7a28a32d5f9eacfd23f92900fe1f8ccd988c1662f30454562
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           cjson
Version:        1.7.19
Release:        %{autorelease}
Summary:        Ultralightweight JSON parser in ANSI C

License:        MIT
URL:            https://github.com/DaveGamble/cJSON
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch:          0001-upgrade-version-of-cmake_minimum_required-986.patch
 
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  cmake

%description
cJSON aims to be the dumbest possible parser that you can get your job
done with. It's a single file of C, and a single header file.
 
%package devel
Summary:        Development files for cJSON
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       cmake-filesystem
  
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use cJSON.
  
%prep
%oreon_sha256
%autosetup -p 1 -n cJSON-%{version}

%build
%cmake -DENABLE_CJSON_TEST=ON -DENABLE_TARGET_EXPORT=ON
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_libdir}/*.{la,a}

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libcjson.so.1{,.*}
 
%files devel
%doc CHANGELOG.md CONTRIBUTORS.md
%{_libdir}/libcjson.so
%{_libdir}/pkgconfig/libcjson.pc
%{_libdir}/cmake/cJSON/
%{_includedir}/cjson/

%changelog
%autochangelog
