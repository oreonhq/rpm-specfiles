%global source0_hash 94d0038ef92bb65b86d08f004197c56f8d81f82f9ac7a25c202a88afd653a30b
Name:           intel-gmmlib
Version:        22.10.2
Release:        1%{?dist}
Summary:        Intel Graphics Memory Management Library
License:        MIT AND BSD-3-Clause
URL:            https://github.com/intel/gmmlib
Source0:        https://github.com/intel/gmmlib/archive/%{name}-%{version}.tar.gz
ExcludeArch:  s390x ppc64le
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
The Intel Graphics Memory Management Library provides device specific
and buffer management for the Intel Graphics Compute Runtime for OpenCL
and the Intel Media Driver for VAAPI.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n gmmlib-intel-gmmlib-%{version}
# Fix license perm
chmod -x LICENSE.md README.rst
# Fix source code perm
find Source -name "*.cpp" -exec chmod -x {} ';'
find Source -name "*.h" -exec chmod -x {} ';'

%build

%cmake \
  -DRUN_TEST_SUITE:BOOL=False
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n intel-gmmlib-devel -f %{oreon_filedir}/intel-gmmlib-devel.list

%changelog

%autochangelog
