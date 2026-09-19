%global source0_hash 5b46b0841757ee498fd3c55ad3d01d5e3d3f40d0c8039b3b2e16a9e459dd9b4b

Name:           kweathercore
Version:        26.04.3
Release:        1%{?dist}
License:        LGPL-2.0-or-later
Summary:        Library to facilitate retrieval of weather information
Url:            https://invent.kde.org/libraries/kweathercore
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Holidays)


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

%autosetup -n %{name}-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang kweathercore6


%files -f kweathercore6.lang
%license LICENSES/*.txt
%{_kf6_libdir}/libKWeatherCore.so.*.*
%{_kf6_libdir}/libKWeatherCore.so.6
%{_kf6_qmldir}/org/kde/weathercore/

%files devel
%license LICENSES/*.txt
%{_includedir}/KWeatherCore/
%{_includedir}/kweathercore_version.h
%{_kf6_libdir}/cmake/KWeatherCore/
%{_kf6_libdir}/libKWeatherCore.so
%{_kf6_archdatadir}/mkspecs/modules/qt_KWeatherCore.pri
%changelog
%autochangelog

