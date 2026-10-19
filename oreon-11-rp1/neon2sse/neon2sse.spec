%global source0_hash 7999d2b85eec8b0bfcad33bbcf1ea8577fa103967b2d84a5c6a43eadae5c7685
%global debug_package %{nil}
%global gitdate 20240908
%global commit 504231850f206696faa58e3511e305a67fd4e565
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		neon2sse
Version:	0.0^%{gitdate}git%{shortcommit}
Release:        1%{?dist}
Summary:        Library intended to simplify ARM->IA32 porting
License:	BSD-2-Clause
URL:		https://github.com/intel/ARM_NEON_2_x86_SSE
Source0:        https://github.com/intel/ARM_NEON_2_x86_SSE/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:	test.c
BuildArch:	noarch
ExclusiveArch:	x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
The platform independent header allowing to compile any C/C++ code containing
ARM NEON intrinsic functions for x86 target systems using SIMD up to SSE4
intrinsic functions.

The NEON_2_SSE.h file is intended to simplify ARM->IA32 porting

%package devel
Summary:	Development files for %{name}
Provides:	%{name}-static = %{version}-%{release}
%description devel
The platform independent header allowing to compile any C/C++ code containing
ARM NEON intrinsic functions for x86 target systems using SIMD up to SSE4
intrinsic functions.

The NEON_2_SSE.h file is intended to simplify ARM->IA32 porting

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ARM_NEON_2_x86_SSE-%{commit}

cp %{SOURCE1} .

# fix path
sed -i 's/lib\/cmake/%{_lib}\/cmake/g' CMakeLists.txt

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

$CC -o test test.c -I%{buildroot}%{_includedir}
./test
%files -f %{oreon_filedir}/main.list
%files -n neon2sse-devel -f %{oreon_filedir}/neon2sse-devel.list

%changelog

%autochangelog
