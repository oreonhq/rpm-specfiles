# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-keyboard
Version: 6.6.3
Release: 3%{?dist}
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
BuildRequires:  kf6-kconfig-devel
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  kf6-kcmutils-devel

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
# Tag still asks for ECM/KF6 6.22 while this branch is Plasma 6.6.x on distro KF 6.6
sed -i 's/set(KF6_MIN_VERSION "6.22.0")/set(KF6_MIN_VERSION "6.6.0")/' CMakeLists.txt


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
* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-3
- Use kf6-kcmutils-devel instead of bogus cmake(KF6KCMUtilsQuick) for KCM QML deps

* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-2
- Relax KF6 min in CMakeLists for KF 6.6 stack, pull in kf6-kconfig-devel for KCM ConfigGui

* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-1
- Add plasma-keyboard package for virtual keyboard support in Plasma
