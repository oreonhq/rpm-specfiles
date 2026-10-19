%global source0_hash eca1591c33d37a8fc97a4729ad4ec905055d2d8774feccbfe4078392ac1ae711
Name:          kwin-zones
Version:       1.0.12
Release:        1%{?dist}
Summary:        Wayland ext-zones for KWin
License:       BSD-3-Clause AND GPL-2.0-or-later AND CC0-1.0 AND MIT
URL:           https://invent.kde.org/automotive/%{name}
Source0:        https://invent.kde.org/automotive/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KWin)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(qt6waylandscannertools)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
