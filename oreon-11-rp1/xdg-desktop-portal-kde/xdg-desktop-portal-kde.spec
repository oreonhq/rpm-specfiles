%global source0_hash bb4b955e2f52a832f221d3fb7182cebf920653a0ad1e3201abd29f134d4c33f3

%global stable_kf6 stable


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    xdg-desktop-portal-kde
Version:        6.7.4
Release: 1%{?dist}
Summary: KDE backend implementation for xdg-desktop-portal

License: GPL-2.0-or-later
URL:     https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  wayland-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-static
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  xdg-desktop-portal-devel

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KWayland)
BuildRequires:  cmake(PlasmaWaylandProtocols)

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  wayland-protocols-devel

Requires:       kf6-filesystem
Requires:       xdg-desktop-portal%{?_isa}

%description
A KDE backend implementation for xdg-desktop-portal using Qt and KDE
Frameworks. It provides desktop portal interfaces for Plasma sessions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%license LICENSES/*
%{_libexecdir}/xdg-desktop-portal-kde
%{_datadir}/xdg-desktop-portal/portals/kde.portal
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.kde.service
%{_datadir}/applications/org.freedesktop.impl.portal.desktop.kde.desktop
%{_userunitdir}/plasma-xdg-desktop-portal-kde.service
%{_kf6_datadir}/knotifications6/xdg-desktop-portal-kde.notifyrc
%{_kf6_datadir}/qlogging-categories6/xdp-kde.categories

%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-1
- Add xdg-desktop-portal-kde package for Plasma portal backend
