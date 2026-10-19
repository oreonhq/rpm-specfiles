%global source0_hash f1658b0562a56255b157b7ffbb81e53e78e2571db1962262e55db6ca01733907
Name:		x86-simd-sort
Version:	7.0
Release:        1%{?dist}
Summary:        C++ template library for high performance SIMD based sorting algorithms
License:	BSD-3-Clause
URL:		https://github.com/intel/x86-simd-sort
Source0:        https://github.com/intel/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:	x86_64
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  meson
# /oreon:deps
%description
C++ template library for high performance SIMD based sorting routines for 
16-bit, 32-bit and 64-bit data types. The sorting routines are accelerated
using AVX-512/AVX2 when available. The library auto picks the best version
depending on the processor it is run on.
	
%package devel
Summary: Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test -v
%files -f %{oreon_filedir}/main.list
%files -n x86-simd-sort-devel -f %{oreon_filedir}/x86-simd-sort-devel.list

%changelog

%autochangelog
