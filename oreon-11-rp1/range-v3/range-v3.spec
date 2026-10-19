%global source0_hash 015adb2300a98edfceaf0725beec3337f542af4915cec4d0b89fa0886f4ba9cb
%global debug_package %{nil}
Name: range-v3
Summary:        Experimental range library for C++11/14/17
Version: 0.12.0
Release:        1%{?dist}
License: BSL-1.0
URL: https://github.com/ericniebler/%{name}
Source0:        https://github.com/ericniebler/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DRANGES_ENABLE_WERROR:BOOL=OFF \
    -DRANGES_MODULES:BOOL=OFF \
    -DRANGES_NATIVE:BOOL=OFF \
    -DRANGE_V3_DOCS:BOOL=OFF \
    -DRANGE_V3_EXAMPLES:BOOL=OFF \
    -DRANGE_V3_PERF:BOOL=OFF \
    -DRANGE_V3_TESTS:BOOL=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n range-v3-devel -f %{oreon_filedir}/range-v3-devel.list

%changelog

%autochangelog
