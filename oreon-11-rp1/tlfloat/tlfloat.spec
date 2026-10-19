%global source0_hash f96a19273111de3c8818965dc3d68cbd66edaba62f03bcd2c06525a22197c97b
%bcond exhaustive 0
Name:           tlfloat
Version:        1.15.0
%global so_version 1
Release:        1%{?dist}
Summary:        C++ template library for floating point operations
License:        BSL-1.0
SourceLicense:  %{license} AND CC-BY-SA-4.0
URL:            https://github.com/shibatch/tlfloat
Source0:        https://github.com/shibatch/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
%ifarch %{x86_64}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mpfr-devel
BuildRequires:  ninja-build
# /oreon:deps
%description
This library implements C++ classes with which half, single, double, quadruple
and octuple precision IEEE 754 floating point numbers can be operated.

Internally, these classes are implemented as class templates on top of
arbitrary-precision integer class templates so that the templates are expanded
as arbitrary precision floating-point operations by just changing the template
parameters, rather than implementing each floating-point operation for each
precision. The arbitrary-precision integer class templates are also included in
this library.

%package devel
Summary:        Development files for TLFloat
Requires:       tlfloat%{?_isa} = %{version}-%{release}
%description devel
The tlfloat-devel package contains libraries and header files for
developing applications that use TLFloat.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# BUILD_UTILS: These utilities (genmathcoef,  mkrpitab) are intended for
#   library maintainers, and are not installed, so we do not build them.
%cmake \
    -GNinja \
%if %{with exhaustive}
    -DBUILD_EXHAUSTIVE_TESTING:BOOL=TRUE \
    -DENABLE_EXHAUSTIVE_TESTING:BOOL=TRUE \
%endif
    -DBUILD_UTILS:BOOL=FALSE

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest %{?with_exhaustive:--timeout 604800}
%files -f %{oreon_filedir}/main.list
%files -n tlfloat-devel -f %{oreon_filedir}/tlfloat-devel.list

%changelog

%autochangelog
