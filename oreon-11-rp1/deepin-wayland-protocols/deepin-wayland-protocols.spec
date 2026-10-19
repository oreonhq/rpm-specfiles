%global source0_hash b36c3e6e875b3b9d8d0388b7f1338a813bb2b8194e9db9b17157cac6919f9c13
%global debug_package %{nil}
Name:           deepin-wayland-protocols
Epoch:          1
Version:        1.10.0.32
Release:        1%{?dist}
Summary:        Deepin Specific Protocols for Wayland
License:        LGPL-2.1-or-later AND MIT-CMU AND BSD-3-Clause
URL:            https://github.com/linuxdeepin/deepin-wayland-protocols
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
# /oreon:deps
%description
%{name} contains Deepin-specific Wayland protocols, which adds
functionality not available in the Wayland core protocol.

%package        devel
Summary:        Development files for %{name}
%description    devel
%{name} contains Deepin-specific Wayland protocols, which
adds functionality not available in the Wayland core protocol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n deepin-wayland-protocols-devel -f %{oreon_filedir}/deepin-wayland-protocols-devel.list

%changelog

%autochangelog
