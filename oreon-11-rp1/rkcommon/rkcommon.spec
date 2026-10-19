%global source0_hash 79334ef3dadddb03ec0483fbf49bf690fb8902d5c2732d977b2c116651484cc6
Name:		rkcommon
Version:	1.15.4
Release:        1%{?dist}
Summary:        Intel renderKit common C++/CMake infrastructure
License:	Apache-2.0
URL:		https://github.com/Renderkit/rkcommon
Source0:        https://github.com/Renderkit/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		test-rsqrt-overload.patch
ExclusiveArch:	x86_64 aarch64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  tbb-devel
# /oreon:deps
%description
This project represents a common set of C++ infrastructure and CMake utilities
used by various components of Intel oneAPI rendering toolkit.

%package devel
Summary:	Development file for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n rkcommon-devel -f %{oreon_filedir}/rkcommon-devel.list

%changelog

%autochangelog
