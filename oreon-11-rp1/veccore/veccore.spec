%global source0_hash 1268bca92acf00acd9775f1e79a2da7b1d902733d17e283e0dd5e02c41ac9666
%global debug_package %{nil}
%global forgeurl https://github.com/root-project/veccore
Version:        0.8.2
%forgemeta
Name:           veccore
Release:        1%{?dist}
Summary:        C++ Library for Portable SIMD Vectorization
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  ninja-build
# /oreon:deps
%description
VecCore is a simple abstraction layer on top of other vectorization libraries.
It provides an architecture-independent API for expressing vector operations on
data. Code written with this API can then be dispatched to one of several
backends implemented using libraries like Vc, UME::SIMD, or a scalar
implementation.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake \
    -GNinja \
    -DBUILD_TESTING=ON \
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n veccore-devel -f %{oreon_filedir}/veccore-devel.list

%changelog

%autochangelog
