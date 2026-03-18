%global framework kactivities-stats

Name:    kf5-%{framework}
Summary: A KDE Frameworks 5 Tier 3 library for accessing the usage data collected by the activities system
Version: 5.116.0
Release: 5%{?dist}

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream patches

BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf5-kactivities-devel >= %{version}
BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-rpm-macros >= %{version}
BuildRequires:  pkgconfig

BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtbase-devel

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel
%description devel
%{summary}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf5 \
  -DBUILD_TESTING=ON

%cmake_build


%install
%cmake_install


# Currently includes no tests
%check
%ctest ||:


%ldconfig_scriptlets

%files
%doc MAINTAINER README.developers TODO
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5ActivitiesStats.so.*

%files devel
%{_kf5_libdir}/libKF5ActivitiesStats.so
%{_kf5_includedir}/KActivitiesStats/

%{_kf5_libdir}/cmake/KF5ActivitiesStats/
%{_kf5_libdir}/pkgconfig/libKActivitiesStats.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_KActivitiesStats.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
