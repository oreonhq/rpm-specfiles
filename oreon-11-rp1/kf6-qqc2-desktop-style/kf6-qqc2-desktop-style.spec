%global source1_hash 5e051fd9e66788b27b7834e8c095d50265d49bcecdb667266316b4beb4ef6252
%global source0_hash 74c6402fa697a76254e1c68ebd86136be49e03fad86482e86a27e5478f662c41
%global framework qqc2-desktop-style
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary:        QtQuickControls2 style for consistency between QWidget and QML apps
License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KFQF-Accepted-GPL
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:      kf6-sonnet
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(xkbcommon)
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
