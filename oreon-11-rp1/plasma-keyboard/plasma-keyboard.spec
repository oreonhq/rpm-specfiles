%global source0_hash 3bb8be109cc449af54d03f28cc1c1a9e4d4150cb01b9af916a5516ed64740671

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-keyboard
Version: 6.6.5
Release: 1%{?dist}
Summary: Virtual keyboard for Plasma based on Qt Virtual Keyboard

License: BSD-2-Clause
URL:     https://invent.kde.org/plasma/%{name}

# download.kde.org can redirect to mirrors that fail on Plasma tarballs
Source0:        https://download.kde.org/stable/plasma/%{version}/plasma-keyboard-%{version}.tar.xz

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
BuildRequires:  desktop-file-utils

Requires:       kf6-filesystem
Requires:       qt6-qtvirtualkeyboard%{?_isa}

%description
Plasma virtual keyboard implementation for Wayland sessions, including
keyboard layouts, styles and KCM configuration integration.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{name}-v%{version} -p1
# Tag still asks for ECM/KF6 6.22 while this branch is Plasma 6.6.x on distro KF 6.6
sed -i 's/set(KF6_MIN_VERSION "6.22.0")/set(KF6_MIN_VERSION "6.6.0")/' CMakeLists.txt


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
# .desktop is not a script; brp removes +x and warns if left executable
chmod a-x %{buildroot}%{_kf6_datadir}/applications/org.kde.plasma.keyboard.desktop 2>/dev/null || :
chmod a-x %{buildroot}%{_kf6_datadir}/applications/kcm_plasmakeyboard.desktop 2>/dev/null || :
%find_lang %{name} --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.plasma.keyboard.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kcm_plasmakeyboard.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/plasma-keyboard
%{_kf6_datadir}/applications/org.kde.plasma.keyboard.desktop
%{_kf6_datadir}/applications/kcm_plasmakeyboard.desktop
%{_kf6_metainfodir}/org.kde.plasma.keyboard.metainfo.xml
%{_kf6_datadir}/plasma/keyboard/
%{_kf6_qmldir}/org/kde/plasma/keyboard/
%{_kf6_qmldir}/org/kde/plasma/keyboard/lib/
%{_kf6_qmldir}/QtQuick/VirtualKeyboard/Styles/Breeze/
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_plasmakeyboard.so


%changelog
* Mon May 25 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.6.5-1
- Update to KDE Plasma 6.6.5

* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-3
- Use kf6-kcmutils-devel instead of bogus cmake(KF6KCMUtilsQuick) for KCM QML deps

* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-2
- Relax KF6 min in CMakeLists for KF 6.6 stack, pull in kf6-kconfig-devel for KCM ConfigGui

* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-1
- Add plasma-keyboard package for virtual keyboard support in Plasma
