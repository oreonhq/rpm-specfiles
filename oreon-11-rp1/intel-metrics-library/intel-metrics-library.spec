%global source0_hash b5d18de1ed2d57338f1e9931dd159588cd36c338a61155ce3c3605827d27a79b
%global upstream_name metrics-library
Name: intel-metrics-library
Version: 1.0.200
Release:        1%{?dist}
Summary:        Shared library for Intel Metrics Library for Metrics Discovery API
License: MIT
ExclusiveArch: x86_64
URL: https://github.com/intel/metrics-library
Source0:        https://github.com/intel/%{upstream_name}/archive/%{upstream_name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
Intel Metrics Library for Metrics Discovery API is a user-mode driver helper
library that provides access to GPU performance counters.

%package         devel
Summary:         Development files for %{name}
Requires:        %{name} = %{version}-%{release}
%description     devel
Intel Metrics Library for Metrics Discovery API is a user-mode driver helper
library that provides access to GPU performance counters.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstream_name}-%{upstream_name}-%{version}

%build

%cmake \
   -DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n intel-metrics-library-devel -f %{oreon_filedir}/intel-metrics-library-devel.list

%changelog

%autochangelog
