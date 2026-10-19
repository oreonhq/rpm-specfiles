%global source0_hash 244be102465cf6f9867a0eface321fd4a97fe198be683538c876d579adf75ceb
%global framework kactivities-stats
Name:    kf5-%{framework}
Summary:        A KDE Frameworks 5 Tier 3 library for accessing the usage data collected by the activities system
Version: 5.116.0
Release:        1%{?dist}
License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kactivities-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
# /oreon:deps
%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf5 \
  -DBUILD_TESTING=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest ||:
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kf5-kactivities-stats-devel -f %{oreon_filedir}/kf5-kactivities-stats-devel.list

%changelog

%autochangelog
