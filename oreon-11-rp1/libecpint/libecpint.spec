%global source0_hash e9c60fddb2614f113ab59ec620799d961db73979845e6e637c4a6fb72aee51cc
%ifarch s390x
%bcond libcerf 0
%else
%bcond libcerf 1
%endif
Name:           libecpint
Version:        1.0.7
Release:        17%{?dist}
Summary:        Efficient evaluation of integrals over ab initio effective core potentials
License:        MIT
Url:            https://github.com/robashaw/libecpint
Source0:        https://github.com/robashaw/libecpint/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:          libecpint-cerf3.patch
%if %{with libcerf}
%else
Provides:       bundled(Faddeeva}
%endif
Requires:       %{name}-common = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libcerf-devel
BuildRequires:  pugixml-devel
BuildRequires:  python3
BuildRequires:  sphinx
# /oreon:deps
%description
Libecpint is a C++ library for the efficient evaluation of integrals over ab
initio effective core potentials, using a mixture of generated, recursive
code and Gauss-Chebyshev quadrature. It is designed to be standalone and
generic.

%package common
Summary:        Architecture independent data files for libecpint
BuildArch:      noarch
%description common
This package contains architecture independent data files for libecpint

%package devel
Summary:        Devel package for libecpint
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libcerf-devel >= 1.17
%description devel
This package contains development headers and libraries for libecpint.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# gtest 1.17.0 requires C++17 or later
# https://github.com/robashaw/libecpint/issues/58
sed -r -i 's/\b(CMAKE_CXX_STANDARD[[:blank:]]+)11\b/\117/' CMakeLists.txt

%build

%cmake %{?with_libcerf:-DLIBECPINT_USE_CERF=ON}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest %{?testargs}
%files -f %{oreon_filedir}/main.list
%files -n libecpint-common -f %{oreon_filedir}/libecpint-common.list
%files -n libecpint-devel -f %{oreon_filedir}/libecpint-devel.list

%changelog

%autochangelog
