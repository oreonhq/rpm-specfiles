%global source0_hash 706f44ef35dc9182021847c9c9348d0cab2812bd4ba0d9050a71783c6fb74997
%global framework kidletime
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 1 integration module for idle time detection
License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$
Requires:       kf5-filesystem >= %{majmin}
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtwayland-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
# /oreon:deps
%description
KDE Frameworks 5 Tier 1 integration module for idle time detection.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kidletime-devel -f %{oreon_filedir}/kf5-kidletime-devel.list

%changelog

%autochangelog
