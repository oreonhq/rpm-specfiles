# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-keyboard
Version: 6.6.3
Release: 1%{?dist}
Summary: Virtual keyboard for Plasma based on Qt Virtual Keyboard

License: BSD-2-Clause
URL:     https://invent.kde.org/plasma/%{name}

# download.kde.org can redirect to mirrors that fail on Plasma tarballs
Source0: https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  ninja-build
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  qt6-qtvirtualkeyboard-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KCMUtilsQuick)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6VirtualKeyboard)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6WaylandClientPrivate)

Requires:       kf6-filesystem
Requires:       qt6-qtvirtualkeyboard%{?_isa}

%description
Plasma virtual keyboard implementation for Wayland sessions, including
keyboard layouts, styles and KCM configuration integration.


%prep
%autosetup -n %{name}-v%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-qt --all-name


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/plasma-keyboard
%{_kf6_datadir}/applications/org.kde.plasma.keyboard.desktop
%{_kf6_metainfodir}/org.kde.plasma.keyboard.metainfo.xml
%{_kf6_datadir}/plasma/keyboard/
%{_kf6_qmldir}/org/kde/plasma/keyboard/
%{_kf6_qmldir}/org/kde/plasma/keyboard/lib/
%{_kf6_qmldir}/QtQuick/VirtualKeyboard/Styles/Breeze/
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_plasmakeyboard.so
%{_kf6_datadir}/kpackage/kcms/kcm_plasmakeyboard/


%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-1
- Add plasma-keyboard package for virtual keyboard support in Plasma
