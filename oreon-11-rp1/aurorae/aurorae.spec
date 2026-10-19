%global source1_hash 8dc67296be6956b3955e6d9cdbf4fb9dac2fc5aff8ac7e01005d20528eb84644
%global stable_kf6 stable
%global source0_hash 7e4305d4e28698024fcd797554ccad84bfd4ed4e5bdcb0f42b5da77fab244416
ExcludeArch: %{ix86}
Name:           aurorae
Summary:        Aurorae is a themeable window decoration for KWin
Version:        6.7.5
Release:        1%{?dist}
License:        GPL-2.0-or-later AND MIT AND CC0-1.0
URL:            https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Conflicts:     kwin < 6.3.90
Supplements:   kwin%{?_isa} >= %{version}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
Aurorae is a themeable window decoration for KWin.
It supports theme files consisting of several SVG files for
decoration and buttons. Themes can be installed and selected
directly in the configuration module of KWin decorations.
Please have a look at theme-description on how to write a theme file.

%package devel
Summary: Development libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles aurorae-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n aurorae-devel -f %{oreon_filedir}/aurorae-devel.list

%changelog

%autochangelog
