%global framework qqc2-desktop-style

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:    kf6-%{framework}
Version: 6.24.0
Release:	2%{?dist}
Summary: QtQuickControls2 style for consistency between QWidget and QML apps
License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KFQF-Accepted-GPL
URL:     https://invent.kde.org/frameworks/%{framework}
Source0: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires: extra-cmake-modules >= %{version}
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: cmake(KF6Sonnet)
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
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6 \
    -DQDOC_BIN=/bin/true
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
* Fri Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Pass -DQDOC_BIN=/bin/true to work around qdoc segfault until kf6-rpm-macros is deployed

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
