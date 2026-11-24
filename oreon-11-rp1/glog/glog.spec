# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 00e4a87e87b7e7612f519a41e491f16623b12423620006f59f5688bfd8d13b08
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           glog
Version:        0.7.1
Release:        1%{?dist}
Summary:        A C++ application logging library
License:        BSD-3-Clause AND Apache-2.0
URL:            https://github.com/google/glog
Source0:        https://github.com/google/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  gmock-devel
BuildRequires:  cmake(gflags)

%description
Google glog is a library that implements application-level
logging. This library provides logging APIs based on C++-style
streams and various helper macros.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup

%conf
%cmake -DWITH_PKGCONFIG=ON

%build
%cmake_build

%install
%cmake_install

%check
%ctest --exclude-regex 'logging|stacktrace|symbolize'

%files
%license COPYING
%doc ChangeLog README.rst
%{_libdir}/libglog.so.%{version}
%{_libdir}/libglog.so.2

%files devel
%{_libdir}/libglog.so
%{_libdir}/pkgconfig/libglog.pc
%{_includedir}/glog
%{_libdir}/cmake/glog

%changelog
%autochangelog
