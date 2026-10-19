%global stable_kf6 stable
%global source0_hash ac5feb1f49db0ee47ac9b1e607ac6ec4582316aed761d9f0b4625ebd25bd97ab
Name:    libkmahjongg
Summary:        Common code, backgrounds and tile sets for games using Mahjongg tiles
Version: 25.12.3
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://invent.kde.org/games/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires: %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Gui)
Requires: cmake(KF6ConfigWidgets)
%description devel
%{summary}.

%package data
Summary:  Common data for %{name}
BuildArch: noarch
%description data
%{summary}, including backgrounds and tilesets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libkmahjongg-devel -f %{oreon_filedir}/libkmahjongg-devel.list
%files -n libkmahjongg-data -f %{oreon_filedir}/libkmahjongg-data.list

%changelog

%autochangelog
