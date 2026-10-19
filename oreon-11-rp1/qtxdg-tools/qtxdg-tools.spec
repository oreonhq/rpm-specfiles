%global source0_hash 7dcbbd787606e522f874bf98305421d3c0c7d0550980ea2f4f39e718f3a28b2e
Name:    qtxdg-tools
Summary:        User tools for libqtxdg
Version: 4.4.0
Release:        1%{?dist}
License: LGPL-2.0-or-later
URL:     https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt6Xdg)
BuildRequires:  pkgconfig(glib-2.0)
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
