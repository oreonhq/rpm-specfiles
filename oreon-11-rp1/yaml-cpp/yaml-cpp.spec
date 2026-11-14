# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: MIT

%global source0_hash 25cb043240f828a8c51beb830569634bc7ac603978e0f69d6b63558dadefd49a

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: yaml-cpp
Version: 0.9.0
Release: 1%{?dist}
Summary: YAML parser and emitter in C++
License: MIT
URL: https://github.com/jbeder/yaml-cpp
Source0: https://github.com/jbeder/yaml-cpp/archive/refs/tags/yaml-cpp-%{version}.tar.gz#/yaml-cpp-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make

%description
yaml-cpp is a YAML parser and emitter in C++ matching the YAML 1.2 spec.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: pkgconfig(yaml-cpp) = %{version}
Provides: cmake(yaml-cpp) = %{version}

%description devel
Headers and cmake/pkgconfig files for %{name}.

%prep
%oreon_sha256
%autosetup -n yaml-cpp-yaml-cpp-%{version} -p1

%build
%cmake -DYAML_BUILD_SHARED_LIBS=ON -DYAML_CPP_BUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libyaml-cpp.so.*

%files devel
%{_libdir}/libyaml-cpp.so
%{_includedir}/yaml-cpp/
%{_libdir}/cmake/yaml-cpp/
%{_libdir}/pkgconfig/yaml-cpp.pc

%changelog
%autochangelog
