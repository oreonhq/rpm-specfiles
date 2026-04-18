%global plasmaver %{version}

Name:           kf6-kglobalacceld
Version:        6.6.3
Release:        3%{?dist}
Summary:        Plasma daemon for global keyboard shortcuts
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
URL:            https://invent.kde.org/plasma/kglobalacceld
Source0:        https://download.kde.org/stable/plasma/%{plasmaver}/kglobalacceld-%{plasmaver}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  ninja-build
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  systemd-rpm-macros

Requires:       kf6-filesystem
Provides:       kglobalacceld = %{version}-%{release}

%description
Daemon and platform plugin for KGlobalAccel on Plasma 6.


%prep
%autosetup -n kglobalacceld-%{plasmaver} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%{_sysconfdir}/xdg/autostart/kglobalacceld.desktop
%{_kf6_datadir}/qlogging-categories6/kglobalacceld.categories
%{_userunitdir}/plasma-kglobalaccel.service
%{_kf6_qtplugindir}/org.kde.kglobalacceld.platforms/
%{_libexecdir}/kglobalacceld


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-2
- Add Plasma kglobalacceld for kwin and session
