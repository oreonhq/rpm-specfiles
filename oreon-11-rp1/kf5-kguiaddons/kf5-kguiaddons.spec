%global source0_hash 5c10d56cb02cb60710c2412d4a3d02671cad74f25d1e9889c6c741f6e833fce6
%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]
%global framework kguiaddons
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with various classes on top of QtGui
License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
Requires:       kf5-filesystem >= %{majmin}
%if %{with kf6_compat}
Recommends:     kf6-%{framework}%{?_isa}
%endif
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtwayland-devel
BuildRequires:  qt5-qtx11extras-devel
# /oreon:deps
%description
KDBusAddons provides convenience classes on top of QtGui.

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

%cmake_kf5 %{?with_kf6_compat:-DBUILD_GEO_SCHEME_HANDLER=OFF}
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kguiaddons-devel -f %{oreon_filedir}/kf5-kguiaddons-devel.list

%changelog

%autochangelog
