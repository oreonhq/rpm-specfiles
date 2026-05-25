
# 
ExcludeArch: %{ix86}

Name:    kwayland-integration
Version: 6.6.5
Release: 1%{?dist}
Summary: Provides integration plugins for various KDE Frameworks for Wayland

License: CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only AND LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtwayland-devel

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf6-rpm-macros

BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kwayland-devel

BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  plasma-wayland-protocols-devel

Requires:       kf5-filesystem

%description
%{summary}.


%prep
%autosetup -p1


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/kwindowsystem.kwayland.categories
%{_kf5_plugindir}/kwindowsystem/KF5WindowSystemKWaylandPlugin.so


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.5-1
- Import
