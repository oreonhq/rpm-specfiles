%global source0_hash ac5feb1f49db0ee47ac9b1e607ac6ec4582316aed761d9f0b4625ebd25bd97ab

Name:    libkmahjongg
Summary: Common code, backgrounds and tile sets for games using Mahjongg tiles
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/games/%{name}
Source:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6I18n)

Requires: %{name}-data = %{version}-%{release}

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

%autosetup -p1

%build
%cmake_kf6

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%files
%doc README
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/libkmahjong*
%{_kf6_libdir}/libKMahjongg6.so.6{,.*}

%files devel
%{_kf6_libdir}/libKMahjongg6.so
%{_kf6_libdir}/cmake/KMahjongglib6/
%{_includedir}/KMahjongg6/

%files data -f %{name}.lang
%{_kf6_datadir}/kmahjongglib/

%changelog
%autochangelog
