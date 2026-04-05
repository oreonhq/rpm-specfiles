# EPEL10 does not have kf5
%if 0%{?rhel} && 0%{?rhel} >= 10
%bcond_with kf5
%else
%bcond_without kf5
%endif

Name:    plasma-integration
Summary: Qt Platform Theme integration plugin for Plasma
Version: 6.6.2
Release:	2%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  wayland-devel
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.6.0

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)

BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  pkgconfig(Qt6QuickControls2)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6StatusNotifierItem)

%if %{with kf5}
# Qt5 build
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  qt5-qtbase-private-devel
# Qt5ThemeSupport
BuildRequires:  qt5-qtbase-static

BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5GuiAddons)

Requires:       (%{name}-qt5 if qt5-qtbase-gui)
%endif

Requires:       plasma-breeze%{?_isa}
Requires:       breeze-cursor-theme
Requires:       breeze-icon-theme
Recommends:     plasma-workspace

# The default QtQuick styles
Requires:       qqc2-breeze-style%{?_isa}
Requires:       kf6-qqc2-desktop-style%{?_isa}

%description
%{summary}.

%if %{with kf5}
%package        qt5
Summary:        Qt5 support for %{name}
# The default QtQuick style
Requires:       qqc2-desktop-style%{?_isa}
%description    qt5
%{summary}.
%endif

%prep
%autosetup -p1

%build
%global _vpath_builddir %{_target_platform}-qt6
%cmake_kf6 -DBUILD_QT5=OFF -DBUILD_QT6=ON
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%if %{with kf5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake_kf5 -DBUILD_QT5=ON  -DBUILD_QT6=OFF
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%endif


%install
%global _vpath_builddir %{_target_platform}-qt6
%cmake_install_kf6
%if %{with kf5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install_kf6
%endif

%find_lang plasmaintegration5

%files -f plasmaintegration5.lang
%doc README.md
%license LICENSES
%{_qt6_plugindir}/platformthemes/KDEPlasmaPlatformTheme6.so

%if %{with kf5}
%files qt5
%{_qt5_plugindir}/platformthemes/KDEPlasmaPlatformTheme5.so
%endif

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
