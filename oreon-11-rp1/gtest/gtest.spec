# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 65fab701d9829d38cb77c14acdc431d2108bfdbf8979e40eb8ae567edf10b27c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: gtest
Version: 1.17.0
Release: 1%{?dist}
Summary: Google C++ testing framework
License: BSD-3-Clause AND Apache-2.0
URL: https://github.com/google/googletest
Source0: https://github.com/google/googletest/archive/v%{version}/googletest-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: make
BuildRequires: python3-devel

%description
Framework for writing C++ tests on a variety of platforms. Based on the xUnit
architecture. Supports automatic test discovery, a rich set of assertions,
user-defined assertions, death tests, fatal and non-fatal failures, various
options for running the tests, and XML test report generation.

%package -n gtest-devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gmock%{?_isa} = %{version}-%{release}
Provides: cmake(GTest) = %{version}
Provides: pkgconfig(gtest) = %{version}
Provides: pkgconfig(gtest_main) = %{version}

%description -n gtest-devel
This package contains development files for %{name}.

%package -n gmock
Summary: Google C++ Mocking Framework
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n gmock
Google Mock is a library for writing and using C++ mock classes. It lets you
create mock classes with simple macros, supports a rich set of matchers and
actions, and handles unordered, partially ordered, or completely ordered
expectations.

%package -n gmock-devel
Summary: Development files for gmock
Requires: gmock%{?_isa} = %{version}-%{release}
Requires: gtest-devel%{?_isa} = %{version}-%{release}
Provides: pkgconfig(gmock) = %{version}
Provides: pkgconfig(gmock_main) = %{version}

%description -n gmock-devel
This package contains development files for gmock.

%prep
%oreon_sha256
%autosetup -n googletest-%{version} -p1

%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DPYTHON_EXECUTABLE=%{__python3} \
    -Dgtest_build_tests=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%{_libdir}/libgtest.so.%{version}
%{_libdir}/libgtest_main.so.%{version}

%files -n gtest-devel
%doc CONTRIBUTORS README.md
%doc docs/
%doc googletest/samples
%{_includedir}/gtest/
%{_libdir}/libgtest.so
%{_libdir}/libgtest_main.so
%{_libdir}/cmake/GTest/
%{_libdir}/pkgconfig/gtest.pc
%{_libdir}/pkgconfig/gtest_main.pc

%files -n gmock
%license LICENSE
%{_libdir}/libgmock.so.%{version}
%{_libdir}/libgmock_main.so.%{version}

%files -n gmock-devel
%doc CONTRIBUTORS README.md
%doc docs/
%{_includedir}/gmock/
%{_libdir}/libgmock.so
%{_libdir}/libgmock_main.so
%{_libdir}/pkgconfig/gmock.pc
%{_libdir}/pkgconfig/gmock_main.pc

%changelog
%autochangelog
