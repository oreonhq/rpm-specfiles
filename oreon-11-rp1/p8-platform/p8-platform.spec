%global source0_hash 064f8d2c358895c7e0bea9ae956f8d46f3f057772cb97f2743a11d478a0f68a0
Summary:        Platform support library used by libcec
Name:           p8-platform
Version:        2.1.0.1
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/Pulse-Eight/platform
Source0:        https://github.com/Pulse-Eight/platform/archive/refs/tags/p8-platform-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         p8-platform-cmake4.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
p8-platform is a small, portable platform abstraction library (threads,
sockets, atomics) written by Pulse-Eight, used to build libcec.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Headers, pkgconfig and CMake config files for building against p8-platform.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir platform-p8-platform-%{version}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n p8-platform-devel -f %{oreon_filedir}/p8-platform-devel.list

%changelog

%autochangelog
