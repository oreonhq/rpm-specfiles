%global source0_hash e60e1e47a3dee93518647d66393c21e2406f7779e9e9e4382d7cea68cebbfb7b

%global stable_kf6 stable


Name:           plasma5support
Version: 6.7.0
Release:        6%{?dist}
Summary:        Compatibility and migration support between KDE Frameworks 5 and 6
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://invent.kde.org/plasma/plasma5support
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libksysguard-devel
BuildRequires:  ninja-build
BuildRequires:  libplasma-devel
BuildRequires:  plasma-activities-devel
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6UnitConversion)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KSysGuard)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xkbcommon)

Requires:       kf6-filesystem
Requires:       libplasma%{?_isa}

%description
%{summary}.


%package -n libplasma5support
Summary:        Plasma 5 support shared library

%description -n libplasma5support
%{summary}.

%package -n libplasma5support-devel
Summary:        Development files for plasma5support
Requires:       libplasma5support%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel

%description -n libplasma5support-devel
Headers and CMake files for libplasma5support.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n plasma5support-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-qt --all-name


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/plasma5support.*
%{_kf6_datadir}/plasma5support
%dir %{_kf6_datadir}/plasma/weather_legacy
%{_kf6_datadir}/plasma/weather_legacy/noaa_station_list.xml

%files -n libplasma5support
%{_libdir}/libPlasma5Support.so.*
%{_libdir}/libplasma-geolocation-interface.so.*
%{_libdir}/libweather_ion.so.*
%{_kf6_qmldir}/org/kde/plasma/plasma5support
%{_kf6_qtplugindir}/plasma5support/dataengine/*
%{_kf6_qtplugindir}/plasma5support/geolocationprovider/*

%files -n libplasma5support-devel
%{_includedir}/Plasma5Support
%{_includedir}/plasma5support
%{_includedir}/plasma/geolocation
%{_libdir}/cmake/Plasma5Support
%{_libdir}/libPlasma5Support.so
%{_libdir}/libplasma-geolocation-interface.so
%{_libdir}/libweather_ion.so
%{_datadir}/doc/qt6/Plasma5Support.qch
%{_datadir}/doc/qt6/Plasma5Support.tags


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-2
- Add plasma5support for legacy Plasma QML
