%global source0_hash 27b28823254aa489c094c40a314ce1575fd7906eeb521e636bb8fd2dc2981f2f
%global stable_kf6 stable
Name:    libplasma
Summary:        Plasma is the foundation of the KDE user interface (v6)
Version:        6.7.5
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND Qt-LGPL-exception-1.1
URL:     https://invent.kde.org/plasma/libplasma
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Requires:       kf6-filesystem
Requires:       qt6-qt5compat%{?_isa}
Requires:       qt6qml(org.kde.config)
Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.ksvg)
Obsoletes:      kf6-plasma < 1:%{version}-%{release}
Provides:       kf6-plasma = 1:%{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Qml)
Requires:       cmake(Qt6Gui)
Requires:       cmake(KF6Package)
Requires:       cmake(KF6KirigamiPlatform)
Requires:       cmake(KF6WindowSystem)
Obsoletes:      kf6-plasma-devel < 1:%{version}-%{release}
Provides:       kf6-plasma-devel = 1:%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6 -DBUILD_QCH=OFF
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-man --all-name
mkdir -p %{buildroot}%{_kf6_datadir}/plasma/plasmoids
mkdir -p %{buildroot}%{_kf6_qmldir}/org/kde/private
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libplasma-devel -f %{oreon_filedir}/libplasma-devel.list

%changelog

* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-1
- Add libplasma (Plasma 6.6.3, matches plasma-workspace stack)
