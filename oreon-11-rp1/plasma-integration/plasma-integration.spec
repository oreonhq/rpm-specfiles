%global source1_hash 21cba56b029dcd6cb3872a33601a591eca230da17e1d098750d8d0db3b2e7bf2
%global source0_hash 0786c49f2f357744e0f4cfda49f55284faa1a97da85a667ca6cf1d8ab07aff89
%global stable_kf6 stable
%bcond_without kf5
Name:    plasma-integration
Summary:        Qt Platform Theme integration plugin for Plasma
Version:        6.7.5
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
%if %{with kf5}
Requires:       (%{name}-qt5 if qt5-qtbase-gui)
%endif
Requires:       plasma-breeze%{?_isa}
Requires:       breeze-cursor-theme
Requires:       breeze-icon-theme
Recommends:     plasma-workspace
Requires:       qqc2-breeze-style%{?_isa}
Requires:       kf6-qqc2-desktop-style%{?_isa}
# oreon:deps
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt6QuickControls2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  wayland-devel
# /oreon:deps
%description
%{summary}.

%if %{with kf5}
%package        qt5
Summary:        Qt5 support for %{name}
Requires:       qqc2-desktop-style%{?_isa}
%description    qt5
%{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%global _vpath_builddir %{_target_platform}-qt6
%cmake_kf6 -DBUILD_QT5=OFF -DBUILD_QT6=ON
%cmake_build
%if %{with kf5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake_kf5 -DBUILD_QT5=ON  -DBUILD_QT6=OFF
%cmake_build
%endif
%install
%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
%if %{with kf5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
%endif
%find_lang plasmaintegration5
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n plasma-integration-qt5 -f %{oreon_filedir}/plasma-integration-qt5.list

%changelog

%autochangelog
