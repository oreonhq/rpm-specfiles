%global stable_kf6 stable
%global source0_hash 5b46b0841757ee498fd3c55ad3d01d5e3d3f40d0c8039b3b2e16a9e459dd9b4b
Name:           kweathercore
Version:        26.04.3
Release:        1%{?dist}
License:        LGPL-2.0-or-later
Summary:        Library to facilitate retrieval of weather information
Url:            https://invent.kde.org/libraries/kweathercore
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
Get weather forecast and alerts anywhere on the earth easy. KWeatherCore
provides you a highly abstracted library for things related to weather:
Get local weather forecast, get weather of a location by name or coordinate,
get sunrise/set moonrise/set and many more informations about a location.

%package devel
Summary:        Development headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang kweathercore6
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kweathercore-devel -f %{oreon_filedir}/kweathercore-devel.list

%changelog

%autochangelog

