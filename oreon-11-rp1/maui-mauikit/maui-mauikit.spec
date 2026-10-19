%global source0_hash a5fbc22f5b19b11b569c8a9585c2e3b64d3226f7bf8f4b92014953403d10e1d2
Name:           maui-mauikit
Version:        4.0.0
Release:        1%{?dist}
License:        LGPL-2.0-or-later AND GPL-3.0-or-later AND BSD-3-Clause AND LGPL-3.0-only AND LGPL-2.1-only AND CC0-1.0 AND MIT
Summary:        Kit for developing Maui Apps
Url:            https://invent.kde.org/maui/mauikit
Source0:        https://download.kde.org/stable/maui/mauikit/%{version}/mauikit-%{version}.tar.xz
Requires: kf6-kirigami
Requires: kf6-purpose
Requires: qt6-qtmultimedia
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(MauiMan4)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libxcb-devel
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  qt6-qt5compat-devel
# /oreon:deps
%description
Kit for developing MAUI Apps. MauiKit is a set of utilities
and "templated" controls based on Kirigami and QCC2 that
follow the ongoing work on the Maui HIG. It let you quickly
create a Maui application and access utilities and widgets
shared among the other Maui apps.

%package devel
Summary:        MauiKit development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Required headers to build components based
on the MauKit framework.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mauikit-%{version}
%oreon_prep
%build

%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build
%install
%cmake_install
%find_lang mauikit
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n maui-mauikit-devel -f %{oreon_filedir}/maui-mauikit-devel.list

%changelog

%autochangelog
