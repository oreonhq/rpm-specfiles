%global source1_hash 5e051fd9e66788b27b7834e8c095d50265d49bcecdb667266316b4beb4ef6252

%global source0_hash 74c6402fa697a76254e1c68ebd86136be49e03fad86482e86a27e5478f662c41

%global framework qqc2-desktop-style

%global stable_kf6 stable
%global majmin_ver_kf6 6.30


Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary: QtQuickControls2 style for consistency between QWidget and QML apps
License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KFQF-Accepted-GPL
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig


BuildRequires: extra-cmake-modules >= %{version}
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6ConfigWidgets) >= %{version}
BuildRequires: cmake(KF6KirigamiPlatform) >= %{version}
BuildRequires: cmake(KF6IconThemes) >= %{version}
BuildRequires: cmake(KF6ColorScheme) >= %{version}
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: cmake(KF6Sonnet) >= %{version}
BuildRequires: pkgconfig(xkbcommon)

# Doesn't need qtbase-private-devel, but private stuff from qtdeclarative
# so we still need to rebuild it
#BuildRequires: qt6-qtbase-private-devel

Requires:      kf6-sonnet

%description
This is a style for QtQuickControls 2 that uses QWidget's QStyle for
painting, making possible to achieve an higher degree of consistency
between QWidget-based and QML-based apps.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-man --with-qt

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/cmake/KF6QQC2DesktopStyle/
%{_qt6_qmldir}/org/kde/desktop/
%{_qt6_qmldir}/org/kde/qqc2desktopstyle/
%{_kf6_plugindir}/kirigami/platform/org.kde.desktop.so

%changelog
%autochangelog
