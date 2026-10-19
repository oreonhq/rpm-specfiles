%global source0_hash 20138d2e452b190c48db192e0247448f7df64b7d26fbed7e133237859596b649
Name:           treeland-protocols
Version:        0.6.0
Release:        1%{?dist}
Summary:        Wayland protocol extensions for treeland
License:        Apache-2.0 OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
URL:            https://github.com/linuxdeepin/treeland-protocols
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
Wayland protocol extensions for treeland.

%package        devel
Summary:        Development files for %{name}
%description    devel
Wayland protocol extensions for treeland.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n treeland-protocols-devel -f %{oreon_filedir}/treeland-protocols-devel.list

%changelog

%autochangelog
